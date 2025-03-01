
import gtts # type: ignore
from MyApp import *
from pygame import mixer
from winsound import *
import os



MainApp = MyApp()
def stuff():
    mixer.music.load("output.mp3")
    mixer.music.play()
def onSubmit():
    try:
        try:
            mixer.music.stop()
            mixer.quit()
           
            os.remove("output.mp3")
            
        except:
            pass
        mixer.init()
        lang = "en"
        data = gtts.gTTS(text=MainApp.inputString.get(), lang=lang, slow=False)
        data.save("output.mp3")
        MainApp.root.after(1, stuff)
        
    except Exception as e:
        MainApp.sendErrorMessage("Error", "Could not play audio, sorry!")
        print(e)
    

MainApp.submitCallback = onSubmit
MainApp.go()
