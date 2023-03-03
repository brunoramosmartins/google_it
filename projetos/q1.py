#!/usr/bin/env python3
import os
from PIL import Image

for image in os.listdir('supplier-data/images'):
    try:
        filename = 'supplier-data/images/' + image
        im = Image.open(filename)
        im.resize((600, 400)).convert('RGB').save('supplier-data/images/' + image[:3] + ".jpeg", 'JPEG')

    except:
        pass
