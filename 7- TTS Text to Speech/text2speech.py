# Install the package pyttsx3 with the command
# pip install pyttsx3
# It will help us to convert text to speech

# Install the package pywin32 with the command
# pip install pywin32
# It's a dependecy for our module

import pyttsx3


def say(speech):
    # Initializing function
    engine = pyttsx3.init()

    # Pass the variable speech
    engine.say(speech)

    # Let's talk
    engine.runAndWait()

# Enter what the pc is goinig to say
speech = input("Enter what you want your pc to say : \n")

say(speech)