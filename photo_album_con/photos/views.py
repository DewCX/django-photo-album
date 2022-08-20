from django.shortcuts import render



#Homepage
def gallery(request):
    return render(request, 'photos/gallery.html')


#Detail page
def viewPhoto(request, pk):
    return render(request, 'photos/photo_detail.html')


#Adding new photo into gallery
def addPhoto(request):
    return render(request, 'photos/add_photo.html')
