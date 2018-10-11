from gtts import gTTS
import pyglet
import time, os
def speak(text):
    file=gTTS(text, "en")
    filename="temp.mp3"
    file.save(filename)
    music= pyglet.media.load(filename, streaming=False)
    music.play()
    time.sleep(music.duration)
    os.remove(filename)
