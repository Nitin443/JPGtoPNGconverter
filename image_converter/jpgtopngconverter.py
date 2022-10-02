import sys
import os
from PIL import Image


# grabing first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check is new/ file exits or not
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# converting jpg to png
for fileName in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{fileName}')
    clean_name = os.path.splitext(fileName)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('All Done !')

# above we use clean name because we just want  file name and then convert into png