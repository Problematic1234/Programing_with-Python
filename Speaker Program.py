from gtts import gTTS
import os
mytext = "hello"
audio = gTTS(text=mytext, lang="en", slow=False)
audio.save("Hello.mp3")
os.system("Hello.mp3")
