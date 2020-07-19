# Import the required module for text 
# to speech conversion 
import pyttsx3
from  gtts import gTTS

# init function to get an engine instance for the speech synthesis 
engine = pyttsx3.init()
#engine = pyttsx3.init("sapi5")
#engine = pyttsx3.init("dummy")

# Set properties _before_ you add things to say
voices = engine.getProperty('voices')
#for voice in voices:
#    print("Voice: %s" % voice.name)
#    print(" - ID: %s" % voice.id)
#    print(" - Languages: %s" % voice.languages)
#    print(" - Gender: %s" % voice.gender)
#    print(" - Age: %s" % voice.age)
#    print("\n")

engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1
engine.setProperty('voice',voices[0].id)

# Queue up things to say.
# There will be a short break between each one
# when spoken, like a pause between sentences.
engine.say("语音生成准备中")
#engine.say("Hello world")
#engine.say("先生、どうでもいいですよ、いきてるだけ痛いんですよ")

# Flush the say() queue and play the audio
engine.runAndWait()

# Program will not continue execution until
# all speech is done talking

#saving voice to file
#plain = 'e:/document/python/prj02/plain.txt'
#f = open(plain,'r')
#theText = f.read()
#f.close()
#tts = gTTS(text=theText,lang='zh-tw')
#tts.save("e:/document/python/prj02/voice.mp3")
#
#engine.say("语音文件大概生成好了")
#engine.runAndWait()
#engine.stop()

