# Importing the packages required
import os
from PIL import Image

# Creating the logic to find for photos
for foldername, subfolders, filenames in os.walk('D:\\'):
    photos = 0
    not_photos = 0

    for filename in filenames:
        if not (filename.lower().endswith('jpg') or filename.lower().endswith('png')):
            not_photos += 1
            continue

        try:
            im = Image.open(os.path.join(foldername, filename))
        except OSError:
            continue

        width, height = im.size

        if width > 500 and height > 500:
            photos += 1
        else:
            not_photos += 1

    if photos > not_photos:
        print(os.path.abspath(foldername))