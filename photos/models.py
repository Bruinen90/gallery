from django.db import models
from photos.choices import *
from django.utils import timezone
import PIL.Image


class Photo(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(height_field='height', width_field='width')
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    aspect_ratio = models.CharField(max_length=15, blank=True, null=True)
    capture_time = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)
    category = models.IntegerField(choices=CATEGORIES)
    published = models.DateTimeField(default=timezone.now)

    def save(self, **kwargs):
        if float(self.height)/float(self.width) > 1:
            self.aspect_ratio = 'vertical'
        else:
            self.aspect_ratio = 'horizontal'
       # img = PIL.Image.open(self.image.url)
       # exif = img._getexif()
       # self.capture_time = exif[36868]
        super(Photo, self).save(kwargs)

    def __str__(self):
        return self.title