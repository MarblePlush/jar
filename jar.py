import speech_recognition as sr
import os
import sys


def talk(words):
    print(words)
    os.system("say " + words)


talk("Hi, how can I help you?")