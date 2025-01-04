from tkinter import * #pip install tkinter
from PIL import Image,ImageTk,ImageSequence #pip install Pillow
import time

root = Tk()
root.geometry("1000x500")

def play_gif():
    while True:
        root.lift()
        root.attributes("-topmost",True)
        global img
        img = Image.open("GIF.gif")
        lbl = Label(root)
        lbl.size("")
        lbl.place(x=0,y=0)
        i=0
        # mixer.music.load(#enter the music file address)
        # mixer.music.play()
        
        for img in ImageSequence.Iterator(img):
            img = img.resize((1000,500))
            img = ImageTk.PhotoImage(img)
            lbl.config(image=img)
            root.update()
            time.sleep(0.05)
        root.destroy()

play_gif()
root.mainloop()
