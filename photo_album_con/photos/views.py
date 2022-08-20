from django.shortcuts import render
from .models import Category, Photo



#Homepage
def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {
        'categories':categories,
        'photos':photos
    }


    return render(request, 'photos/gallery.html', context)


#Detail page
def viewPhoto(request, pk):
    photo = Photo.objects.get(id = pk)
    return render(request, 'photos/photo_detail.html', {'photo':photo})


#Adding new photo into gallery
def addPhoto(request):
    return render(request, 'photos/add_photo.html')
