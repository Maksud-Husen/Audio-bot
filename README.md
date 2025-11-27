# Audio-bot
Making a chatbot using gemini ai api  and python that is doing certain task like oping browser(brave),code editor facebook, instagram, etc via voice command and asking some general things via chatbot
##How to run this but?
1. Get gemini ai's API Key from https://aistudio.google.com/api-keys
2. Add that API Key in .env file [API_KEY=<YOUR_API_KEY>]
3. Next make a virtual environment [In terminal:-{python3 -m venv venv}]
4. Open that env file [In treminal:-{source venv/bin/activate}] then you will be in venv
## Install the required dependency from requirement.txt
annotated-types==0.7.0
anyio==4.11.0
beautifulsoup4==4.14.2
cachetools==6.2.2
certifi==2025.11.12
charset-normalizer==3.4.4
dotenv==0.9.9
google-auth==2.43.0
google-genai==1.52.0
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.11
pyasn1==0.6.1
pyasn1_modules==0.4.2
PyAudio==0.2.14
pydantic==2.12.4
pydantic_core==2.41.5
python-dotenv==1.2.1
pyttsx3==2.99
requests==2.32.5
rsa==4.9.1
setuptools==80.9.0
sniffio==1.3.1
soupsieve==2.8
SpeechRecognition==3.14.4
tenacity==9.1.2
typing-inspection==0.4.2
typing_extensions==4.15.0
urllib3==2.5.0
websockets==15.0.1

###You can install manually in your venv 
##OR
###In terminal rub :- {pip install -r requirement.txt}
this will install the dependency in the requirement.txt file

## Running program 
1. TO run program you need to follow the above steps one to one
2. Then [In terminal:- {python3 main.py}]
