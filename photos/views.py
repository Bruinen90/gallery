from django.shortcuts import render, get_object_or_404, redirect
# import PIL.Image
from random import shuffle

from photos.choices import *
from .models import Photo
from .forms import AddPhoto


cat_list = dict((x, y) for x, y in CATEGORIES)


def photos_grid(request):
    global cat_list
    photos = Photo.objects.order_by('aspect_ratio')
    output = {'photos': photos, 'categories': cat_list,}
    return render(request, 'photos/photos_grid.html', output)

def cat_view(request):
    global cat_list
    cat_list = dict((x, y) for x, y in CATEGORIES)
    return render(request, 'photos/cat_list.html', {'categories': cat_list})

def new_photo(request):
    global cat_list
    if request.method == "POST":
        form = AddPhoto(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('photos_grid')

    else:
        form = AddPhoto()
    context = {'form': form, 'categories': cat_list}
    return render(request, 'photos/new_photo.html', context)


def full_photo(request, pk):
    full_photo = get_object_or_404(Photo, pk=pk)
#    img = PIL.Image.open('.'+full_photo.image.url)
#    exif = img._getexif()
    context = {'full_photo': full_photo, 'categories': cat_list}
    return render(request, 'photos/full_photo.html', context)


def category_view(request, selected_category):
    cat_photo_grid = Photo.objects.filter(category=selected_category).order_by('aspect_ratio')
    context = {'selected_category': selected_category, 'cat_photo_grid': cat_photo_grid, 'categories': cat_list,}
    return render(request, 'photos/category.html', context)


def home(request):
    global cat_list
    horiz = Photo.objects.filter(aspect_ratio='horizontal')
    random = [o for o in horiz]
    shuffle(random)
    first = random[:1]
    photos = random[2:6]
    context = {'first': first, 'photos': photos, 'categories': cat_list}
    return render(request, 'photos/index.html', context)
