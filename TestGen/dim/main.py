import math
import sys

if sys.version_info[0] < 3:
    raise(Exception("Must be run with Python 3.X"))

from PIL import Image

wide = int(input("Input width (in cards): "))
high = int(input("Input height (in cards): "))
pix = int(input("Size of cards (in pixels): "))

red = -1
blu = -1
grn = -1

while red<0 or red>255:
    red = int(input("Red value (0-255): "))
while grn<0 or grn>255:
    grn = int(input("Green value (0-255): "))
while blu<0 or blu>255:
    blu = int(input("Blue value (0-255): "))

if wide > 99 or high > 99:
    raise(Exception("Signs larger than 100 cards wide or high are not supported"))

imOut = Image.new("RGBA", (wide*pix,high*pix), "white")
pixOut = imOut.load()

for i in range(wide*pix):
    for j in range(high*pix):
        pixOut[i,j] = (red,grn,blu,255)

imOut.save(str(wide)+"x"+str(high)+"@"+str(pix)+ "_solid_" + str(red) + "." + str(grn) + "." + str(blu) + ".png")
