from PIL import Image
import imageio as io
import os

spritesheet = Image.open("spritesheet.png")

frameCount = int(raw_input('Number of frames: '))
frameSize  = int(raw_input('Frame size: '))
frameDelay = float(raw_input('Frame delay: '))

frames = []
count = 0
while count<frameCount:
    temp = spritesheet.crop((0+(count*frameSize),0,frameSize+(count*frameSize),frameSize))
    frames.append(temp)
    temp.save("frame_" + str(count) + ".png")
    count += 1

file_names = sorted((fn for fn in os.listdir('.') if fn.startswith('frame_')))
#making animation
with io.get_writer('surface.gif', mode='I', duration=frameDelay) as writer:
        for filename in file_names:
            image = io.imread(filename)
            writer.append_data(image)
            os.remove(filename)
writer.close()
