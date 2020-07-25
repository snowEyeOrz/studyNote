import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
#for voice in voices:
#    print("voice: %s" % voice.name)
#    print(" - ID: %s" % voice.id)
#    print(" - Languages: %s" % voice.languages)
#    print(" - Gender: %s" % voice.name)
#    print(" - Age: %s" % voice.age)
#    print("\n")

engine.setProperty('rate',175)
engine.setProperty('volume',0.9)
#engine.setProperty('voice',voices[39].id)
engine.setProperty('voice',"com.apple.speech.synthesis.voice.ting-ting")

plain = "大家好，欢迎来到菜鸟编程笔记。我是雪瞳。\
         这是我的第一期节目，声音是通过派森将文字转换而来的。"
engine.say(plain)
engine.save_to_file(plain,'test.mp3')
engine.runAndWait()
