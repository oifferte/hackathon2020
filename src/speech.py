from gtts import gTTS
import pygame
import os
import shutil

class TtsAPI():

    def __init__(self):
        pygame.init()
        pygame.mixer.pre_init()
        pygame.mixer.init()
        pygame.mixer.get_init()

    def gentts(self, text, filename):
        name = str(filename+".mp3")
        text2speech = gTTS(text=text, lang = 'en')
        text2speech.save(name)
        src = str("/home/owen/cs-courses/hackathon/"+name)
        dest = str("/home/owen/cs-courses/hackathon/assets/voice/"+name)
        shutil.move(src, dest)
        return name
