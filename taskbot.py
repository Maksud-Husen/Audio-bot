import speech_recognition as sr 
import pyttsx3
import webbrowser
import subprocess as cmd
from ai_api import AI_Response as AR
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def response(command):
    if "youtube" in command.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open code" in command.lower():
        cmd.Popen("code", shell=True)
    elif "open viber" in command.lower():
        cmd.Popen("/opt/viber/Viber -d", shell=True)
    elif "open brave" in command.lower():
        cmd.Popen("brave", shell=True)    
    elif "shutdown" in command.lower():
        cmd.Popen("shutdown now", shell=True)
    elif "restart" in command.lower():
        cmd.Popen("reboot", shell=True)
    elif "open insta" in command.lower() or "open instagram" in command.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open facebook" in command.lower():
        webbrowser.open("https://www.facebook.com")
    elif "exit" in command.lower():
        exit()
    else:
        ai_reply = AR(command)
        speak(ai_reply)
# command = input("You: ")
# response(command)
if __name__ == "__main__":
    speak("Welcome sir!")
    while True:
        #Listen for the wake word
        print("Listening...")
        
        try:
            with sr.Microphone() as source:
                # Adjust for ambient noise
                recognizer.adjust_for_ambient_noise(source, duration=0.5)   #ambient noise ignores the background noise      
                print("Say something!")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
            
            # Recognize speech using Google's speech recognition
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            response(command)
                
        except sr.WaitTimeoutError:
            print("No speech detected, listening again...")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak("Sorry, I'm having trouble with the speech recognition service")
        except Exception as e:
            print(f"Error: {e}")
            