import tkinter
import gtts # type: ignore

root = tkinter.Tk()
root.resizable(False, False)
root.geometry("500x250")
root.title("TTS Program")

def play(input):
    lang = "en"
    data = gtts.gTTS(text=input, lang=lang, slow=False)
    data.save("output.wav")


introLabel = tkinter.Label(root)
introLabel.config(text="Welcome to my TTS software", font="Arial 22 bold")
introLabel.place(x=250, y=30, anchor="center")

introLabel2 = tkinter.Label(root)
introLabel2.config(text="Enter text in the box\n below and press submit to hear it!", font="Arial 16")
introLabel2.place(x=250, y=90, anchor="center")

inputString = tkinter.StringVar(root)
inputString.set("Text here")

inputBox = tkinter.Entry(root)
inputBox.config(textvariable=inputString, font="Arial 13")
inputBox.place(x=250, y=150, anchor="center")

playBtn = tkinter.Button(root)
playBtn.config(text="Submit", font="Arial 13", command=lambda: play(inputString.get()))
playBtn.place(x=250, y=200, anchor="center")

root.mainloop()