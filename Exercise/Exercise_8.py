
# ? Create module to text to speech

from gtts import gTTS
import pygame
import os

shout_out_names = ["Kaif", "Wasim", "Harry", "Niraj"]

mytext="Welcome all of you,  here are the legends that have completed their task, \n "
for name in shout_out_names:
    mytext = mytext + f"Shout out to {name}\n "

mytext = mytext + "\n Thank you all of you !"
print(mytext)
# Language in which you want to convert
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)


myobj.save("output.mp3")

file_path = './output.mp3'

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(file_path)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue

pygame.quit()
