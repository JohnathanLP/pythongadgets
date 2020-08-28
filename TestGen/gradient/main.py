import math
import sys

if sys.version_info[0] < 3:
    raise(Exception("Must be run with Python 3.X"))

from PIL import Image

wide = int(input("Input width (in cards): "))
high = int(input("Input height (in cards): "))
pix = int(input("Size of cards (in pixels): "))

#pix = 40
#wide = 8
#high = 8

if wide > 99 or high > 99:
    raise(Exception("Signs larger than 100 cards wide or high are not supported"))

imOut = Image.new("RGBA", (wide*pix,high*pix), "white")
pixOut = imOut.load()

step = 255.0/(wide*pix)
astep = 255.0/(high*pix)
#print(step)
for i in range(wide*pix):
    for j in range(high*pix):
        adj = (i+(wide*pix)/2)%(wide*pix)
        r = int(adj*step*2)
        if r>255:
            r=512-r
        adj = (i+(wide*pix)/6)%(wide*pix)
        g = int(adj*step*2)
        if g>255:
            g=512-g
        adj = (i+(wide*pix*5)/6)%(wide*pix)
        b = int(adj*step*2)
        if b>255:
            b=512-b
        pixOut[i,j]=(r,g,b,int(astep*j))

imOut.save(str(wide)+"x"+str(high)+"@"+str(pix)+ "_gradient.png")
