from PIL import Image

img = Image.open('./image/msd.jpg')

filter_image = img.convert('L')

filter_image.save('filter.png', 'png')


print(img.format)