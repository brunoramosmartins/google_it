#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
for image in os.listdir('supplier-data/images'):

    if image[-4:] == 'jpeg':
        print(image)
        filename = 'supplier-data/images/' + image
        with open(filename, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
