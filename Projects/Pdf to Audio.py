
#? Pdf to text 

from PyPDF2 import PdfReader
from gtts import gTTS
import pygame
import os


file1 = open('./pdf/pdf1.pdf', 'rb')

reader = PdfReader(file1)
page = reader.pages[0]
mytext = page.extract_text()

# Language in which you want to convert
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)


myobj.save("./Exercise/textToAudio.mp3")

file_path = './Exercise/textToAudio.mp3'

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(file_path)
print("Playing")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue

pygame.quit()

print("Done 🎉")
