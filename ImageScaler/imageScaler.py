from PIL import Image
imName = raw_input("Image name (without extension):") 
imIn = Image.open(imName + ".png")
pixIn = imIn.load()
print "Image loaded successfully!"
wide, high = imIn.size
print wide, high
scale = input("Scale:") 
print imIn.mode

imOut = Image.new("RGBA", (wide*scale,high*scale), "white")
pixOut = imOut.load()

i = 0
j = 0
while j < high:
  while i < wide: 
    col = pixIn[i,j]
    s = 0
    t = 0
    while s < scale:
      while t < scale:
        pixOut[(i*scale)+t,(j*scale)+s] = col
        t+=1
      t=0
      s+=1
    #print i,j
    print col
    #pixOut[i,j] = col
    i+=1
  i=0
  j+=1

imOut.save(imName + "_scaled_" + str(scale) + ".png")
