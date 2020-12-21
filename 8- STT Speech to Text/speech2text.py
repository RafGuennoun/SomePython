# Install the package SpeechRecognition with the command
# pip install SpeechRecognition
# It's a dependecy that will help us

# Install the package pyaudio with the command
# pip install pyaudio
# For the audio in our python project

# If you have issues try this
# pip install pywin
# pipwin install pyaudio

import pyttsx3
import speech_recognition as sr

def get():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something ...")
        audio = r.listen(source)
        print("Done !")

    try:
        text = r.recognize_google(audio)
        print("You said : "+text)
    except Exception as e:
        print(e)

get()
