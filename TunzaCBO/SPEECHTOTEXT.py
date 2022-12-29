from gtts import gTTS

import os

mytext="Welcome my name is Peter"

language='en'

myobj.save("welcome.mp3")
os.system("mpg321 welcome.mp3")