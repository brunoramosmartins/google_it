import os
from PIL import Image

for image in os.listdir('images'):
    if image != '.DS_Store':
        string = 'images/' + image
        im = Image.open(string)
        im.rotate(-90).resize((128, 128)).convert('RGB').save('new_images/' + image + ".jpeg", 'JPEG')
