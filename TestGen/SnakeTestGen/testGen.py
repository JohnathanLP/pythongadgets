import math
import sys

if sys.version_info[0] >= 3:
    raise(Exception("Must be run with Python 2.X"))

from PIL import Image

wide = input("Input width (in cards): ")
#pix = input("Size of cards (in pixels): ")
pix = 12

if wide > 99:
    raise(Exception("Signs larger than 100 cards wide are not supported"))

colors = ()
if wide <= 6:
    colors = ((255,0,0),
              (255,255,0),
              (0,255,0),
              (0,255,255),
              (0,0,255),
              (255,0,255))
else:
    colors = ((255,0,0),
              (255,128,0),
              (255,255,0),
              (128,255,0),
              (0,255,0),
              (0,255,128),
              (0,255,255),
              (0,128,255),
              (0,0,255),
              (128,0,255),
              (255,0,255),
              (255,0,128))

imOut = Image.new("RGBA", (wide*pix,pix*2), "white")
pixOut = imOut.load()

def drawSnake(ind, orientation):
    if orientation == 0:
        for a in range(pix):
            pixOut[ind+(pix/2)-1,a] = (0,0,0)
            pixOut[ind+(pix/2),a] = (0,0,0)
    if orientation == 1:
        for a in range(pix/2+1):
            #vert
            pixOut[ind+(pix/2)-1,a] = (0,0,0)
            pixOut[ind+(pix/2),a] = (0,0,0)
            #horz
            pixOut[ind+a,(pix/2)-1] = (0,0,0)
            pixOut[ind+a,(pix/2)] = (0,0,0)
    if orientation == 2:
        for a in range(pix/2+1):
            #vert
            pixOut[ind+(pix/2)-1,a+(pix/2)-1] = (0,0,0)
            pixOut[ind+(pix/2),a+(pix/2)-1] = (0,0,0)
            #horz
            pixOut[ind+a+(pix/2),(pix/2)-1] = (0,0,0)
            pixOut[ind+a+(pix/2),(pix/2)] = (0,0,0)
    if orientation == 3:
        for a in range(pix/2+1):
            #vert
            pixOut[ind+(pix/2)-1,a+(pix/2)-1] = (0,0,0)
            pixOut[ind+(pix/2),a+(pix/2)-1] = (0,0,0)
            #horz
            pixOut[ind+a,(pix/2)-1] = (0,0,0)
            pixOut[ind+a,(pix/2)] = (0,0,0)
    if orientation == 4:
        for a in range(pix/2+1):
            #vert
            pixOut[ind+(pix/2)-1,a] = (0,0,0)
            pixOut[ind+(pix/2),a] = (0,0,0)
            #horz
            pixOut[ind+a+(pix/2)-1,(pix/2)-1] = (0,0,0)
            pixOut[ind+a+(pix/2)-1,(pix/2)] = (0,0,0)

for i in range(wide):
    for b in range(pix):
        for a in range(pix):
            pixOut[a+(i*pix),b] = colors[i%len(colors)]
    if i%8 == 0:
        drawSnake(i*pix, 1)
    if i%8 == 1:
        drawSnake(i*pix, 0)
    if i%8 == 2:
        drawSnake(i*pix, 0)
    if i%8 == 3:
        drawSnake(i*pix, 2)
    if i%8 == 4:
        drawSnake(i*pix, 3)
    if i%8 == 5:
        drawSnake(i*pix, 0)
    if i%8 == 6:
        drawSnake(i*pix, 0)
    if i%8 == 7:
        drawSnake(i*pix, 4)

imOut.save(str(wide)+"x"+"@"+str(pix)+ "_snake.png")
