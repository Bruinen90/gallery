import random
from django.core.files.images import get_image_dimensions
import PIL.Image

img = PIL.Image.open('IMG_2758.jpg')
exif = img._getexif()
print(exif)
print(exif.get(306))
width, height = get_image_dimensions('IMG_2758.jpg')
print(width)
print(height)
pop = [1, 2, 3, 4, 5]
rand = random.sample(pop, k=2)
print(rand)