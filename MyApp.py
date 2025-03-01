import tkinter
import tkinter.messagebox
class MyApp:
    def __init__(self):
        self.root = None
        self.submitCallback = lambda: print("")
        self.headerLabel = None
        self.subheaderLabel = None
        self.inputBox = None
        self.inputString = None
    def go(self):
        self.root = tkinter.Tk()
        self.root.resizable(False, False)
        self.root.geometry("500x250")
        self.root.title("TTS Program")

        self.headerLabel = tkinter.Label(self.root)
        self.headerLabel.config(text="Welcome to my TTS software", font="Arial 22 bold")
        self.headerLabel.place(x=250, y=30, anchor="center")

        self.subheaderLabel = tkinter.Label(self.root)
        self.subheaderLabel.config(text="Enter text in the box\n below and press submit to hear it!", font="Arial 16")
        self.subheaderLabel.place(x=250, y=90, anchor="center")

        self.inputString = tkinter.StringVar(self.root)
        self.inputString.set("Text here")

        self.inputBox = tkinter.Entry(self.root)
        self.inputBox.config(textvariable=self.inputString, font="Arial 13")
        self.inputBox.place(x=250, y=150, anchor="center")

        self.submitBtn = tkinter.Button(self.root)
        self.submitBtn.config(text="Submit", font="Arial 13", command=self.submitCallback)
        self.submitBtn.place(x=250, y=200, anchor="center")
        tkinter.mainloop()
    def sendInfoMessage(self,t,c):
        tkinter.messagebox.showinfo(t,c)
    def sendErrorMessage(self,t,c):
        tkinter.messagebox.showerror(t,c)
