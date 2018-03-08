import imageio as io
import os
file_names = sorted((fn for fn in os.listdir('.') if fn.startswith('frame')))
#making animation
with io.get_writer('surface.gif', mode='I', duration=0.1) as writer:
        for filename in file_names:
            image = io.imread(filename)
            writer.append_data(image)
writer.close()
