import logging
import time
from google import genai
from google.genai import errors
from config import Config

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    client = genai.Client(api_key=Config.API_KEY)
except Exception as e:
    logging.error(f"Failed to initialize GenAI client: {e}")
    client = None

def AI_Response(command):
    if not client:
        return "Error: AI client not initialized."

    try:
        response = client.models.generate_content(
            model=Config.MODEL_NAME,
            contents=command
        )
        return response.text
    except errors.ClientError as e:
        if e.code == 429:
            logging.warning("Rate limit exceeded. Waiting for 30 seconds before retrying...")
            time.sleep(30)
            try:
                response = client.models.generate_content(
                    model=Config.MODEL_NAME,
                    contents=command
                )
                return response.text
            except Exception as retry_error:
                logging.error(f"Retry failed: {retry_error}")
                return f"Retry failed: {retry_error}"
        else:
            logging.error(f"API Error: {e}")
            return f"API Error: {e}"
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return f"An unexpected error occurred: {e}"