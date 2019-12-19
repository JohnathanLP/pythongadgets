import math
import sys

if sys.version_info[0] >= 3:
    raise(Exception("Must be run with Python 2.X"))

from PIL import Image

numbers = False
lines = False
stagger = False

if  "numbers" in sys.argv:
    numbers = True
if "lines" in sys.argv:
    lines = True
if "stagger" in sys.argv:
    stagger = True

if lines and numbers:
    print ("Numbers and lines is not officially supported, and may cause unexpected results")

def WriteDigit(digit, x, y, large):
    O = False
    X = True

    if not large:
        if digit>9:
            WriteDigit(int(digit/10),x,y,False)
            WriteDigit(int(digit%10),x+4,y,False)
            return

        if digit == 0:
            arr = ((X,X,X),
                   (X,O,X),
                   (X,O,X),
                   (X,O,X),
                   (X,X,X))
        if digit == 1:
            arr = ((O,X,O),
                   (O,X,O),
                   (O,X,O),
                   (O,X,O),
                   (O,X,O))
        if digit == 2:
            arr = ((X,X,X),
                   (O,O,X),
                   (X,X,X),
                   (X,O,O),
                   (X,X,X))
        if digit == 3:
            arr = ((X,X,X),
                   (O,O,X),
                   (X,X,X),
                   (O,O,X),
                   (X,X,X))
        if digit == 4:
            arr = ((X,O,X),
                   (X,O,X),
                   (X,X,X),
                   (O,O,X),
                   (O,O,X))
        if digit == 5:
            arr = ((X,X,X),
                   (X,O,O),
                   (X,X,X),
                   (O,O,X),
                   (X,X,X))
        if digit == 6:
            arr = ((X,X,X),
                   (X,O,O),
                   (X,X,X),
                   (X,O,X),
                   (X,X,X))
        if digit == 7:
            arr = ((X,X,X),
                   (O,O,X),
                   (O,O,X),
                   (O,O,X),
                   (O,O,X))
        if digit == 8:
            arr = ((X,X,X),
                   (X,O,X),
                   (X,X,X),
                   (X,O,X),
                   (X,X,X))
        if digit == 9:
            arr = ((X,X,X),
                   (X,O,X),
                   (X,X,X),
                   (O,O,X),
                   (X,X,X))

        for j in range(5):
            for i in range(3):
                if arr[j][i] == X:
                    pixOut[x+i,y+j] = (0,0,0)

    else:
        if digit>9:
            WriteDigit(int(digit/10),x,y,True)
            WriteDigit(int(digit%10),x+6,y,True)
            return

        if digit == 0:
            arr = ((O,X,X,X,O),
                   (X,O,O,O,X),
                   (X,O,O,O,X),
                   (X,O,O,O,X),
                   (X,O,O,O,X),
                   (X,O,O,O,X),
                   (O,X,X,X,O))
        if digit == 1:
            arr = ((O,O,X,O,O),
                   (O,X,X,O,O),
                   (O,O,X,O,O),
                   (O,O,X,O,O),
                   (O,O,X,O,O),
                   (O,O,X,O,O),
                   (O,O,X,O,O))
        if digit == 2:
            arr = ((O,X,X,X,O),
                   (X,O,O,O,X),
                   (O,O,O,O,X),
                   (O,O,O,X,O),
                   (O,O,X,O,O),
                   (O,X,O,O,O),
                   (X,X,X,X,X))
        if digit == 3:
            arr = ((O,X,X,X,O),
                   (X,O,O,O,X),
                   (O,O,O,O,X),
                   (O,O,X,X,O),
                   (O,O,O,O,X),
                   (X,O,O,O,X),
                   (O,X,X,X,O))
        if digit == 4:
            arr = ((X,O,O,O,X),
                   (X,O,O,O,X),
                   (X,O,O,O,X),
                   (X,X,X,X,X),
                   (O,O,O,O,X),
                   (O,O,O,O,X),
                   (O,O,O,O,X))
        if digit == 5:
            arr = ((X,X,X,X,X),
                   (X,O,O,O,O),
                   (X,O,O,O,O),
                   (X,X,X,X,O),
                   (O,O,O,O,X),
                   (X,O,O,O,X),
                   (O,X,X,X,O))
        if digit == 6:
            arr = ((O,X,X,X,O),
                   (X,O,O,O,X),
                   (X,O,O,O,O),
                   (X,X,X,X,O),
                   (X,O,O,O,X),
                   (X,O,O,O,X),
                   (O,X,X,X,O))
        if digit == 7:
            arr = ((X,X,X,X,X),
                   (O,O,O,O,X),
                   (O,O,O,O,X),
                   (O,O,O,X,O),
                   (O,O,X,O,O),
                   (O,O,X,O,O),
                   (O,O,X,O,O))
        if digit == 8:
            arr = ((O,X,X,X,O),
                   (X,O,O,O,X),
                   (X,O,O,O,X),
                   (O,X,X,X,O),
                   (X,O,O,O,X),
                   (X,O,O,O,X),
                   (O,X,X,X,O))
        if digit == 9:
            arr = ((O,X,X,X,O),
                   (X,O,O,O,X),
                   (X,O,O,O,X),
                   (O,X,X,X,X),
                   (O,O,O,O,X),
                   (X,O,O,O,X),
                   (O,X,X,X,O))

        for j in range(7):
            for i in range(5):
                if arr[j][i] == X:
                    pixOut[x+i,y+j] = (0,0,0)

def WriteComma(x,y):
    pixOut[x+1,y+4] = (0,0,0)
    pixOut[x+1,y+5] = (0,0,0)


wide = input("Input width (in cards): ")
high = input("Input height (in cards): ")
pix = input("Size of cards (in pixels): ")

if wide > 99 or high > 99:
    raise(Exception("Signs larger than 100 cards wide or high are not supported"))

#wide = 48
#high = 1
#pix = 30

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

imOut = Image.new("RGBA", (wide*pix,high*pix), "white")
pixOut = imOut.load()

for j in range(high):
    for i in range(wide):
        for b in range(pix):
            for a in range(pix):
                if stagger:
                    pixOut[a+(i*pix),b+(j*pix)] = colors[(i-j)%len(colors)]
                else:
                    pixOut[a+(i*pix),b+(j*pix)] = colors[i%len(colors)]
#                print(pixOut[a][b])
        if numbers:
            offset = 1
            if lines:
                offset = 2
            if pix > 16:
                WriteDigit(j,(i*pix)+offset,(j*pix)+offset,True)
                #WriteComma((i*pix)+9+offset,(j*pix)+offset+2)
                WriteDigit(i,(i*pix)+offset,(j*pix)+9+offset,True)
            else:
                WriteDigit(i,(i*pix)+offset,(j*pix)+6+offset,False)
                WriteDigit(j,(i*pix)+offset,(j*pix)+offset,False)
                WriteComma((i*pix)+7+offset,(j*pix)+offset)
if lines:
    for j in range(high*pix):
        for i in range(wide*pix):

            # horizontal
            if j%pix == 0 or j%pix == pix-1:
                pixOut[i,j] = (0,0,0)
            # vertical
            if i%pix == 0 or i%pix == pix-1:
                pixOut[i,j] = (0,0,0)


imOut.save(str(wide)+"x"+str(high)+"@"+str(pix)+ ".png")
