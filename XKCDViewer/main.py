import tkinter
from tkinter import *
import urllib.request
from PIL import Image

def exit(event):
    root.destroy()

root = tkinter.Tk()
root.geometry("240x240+0+32")

#root.overrideredirect(1)

# get url of current XKCD
site = urllib.request.urlopen("https://xkcd.com/")
text = site.read()

index = (str(text).find("https://imgs.xkcd.com"))
filename = str(text)[index:index+200].split("\"")[0]
print (filename)

# download current XKCD
urllib.request.urlretrieve(filename,"raw.png")

# scale image
raw = Image.open("raw.png")
maxsize=(240,240)
raw.thumbnail(maxsize, Image.ANTIALIAS)
raw.save("final.png")

# display image
canvas = Canvas(root, width=240, height=240)
canvas.pack()
img = PhotoImage(file="final.png")
canvas.create_image(120,0,anchor=N, image=img)
canvas.bind("<Button-1>", exit)

root.mainloop()
