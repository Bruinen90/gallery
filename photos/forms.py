from django import forms
from .models import Photo
from photos.choices import *


class AddPhoto(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('title', 'image', 'description', 'category')

