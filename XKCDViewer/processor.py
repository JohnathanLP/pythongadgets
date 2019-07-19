import urllib.request
from PIL import Image

# TODO fix this...
number = input("Desired comic number (press enter for most recent):")
print (number)
print ("https://xkcd.com/" + number + "/")

# get url of desired XKCD
site = urllib.request.urlopen("https://xkcd.com/" + number)
text = site.read()
#index = (str(text).find("https://imgs.xkcd.com"))
index = (str(text).find("hotlinking"))
filename = str(text)[index+23:index+100].split("\\n")[0]
print (filename)
#print(str(text))

# download current XKCD
urllib.request.urlretrieve(filename,"xkcd.png")

# scale image
raw = Image.open("xkcd.png")
maxsize=(240,240)
raw.thumbnail(maxsize, Image.ANTIALIAS)
raw.save("xkcd.png")

print ("Done!")
