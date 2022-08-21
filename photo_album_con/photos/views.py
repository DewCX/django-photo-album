from django.shortcuts import render, redirect
from .models import Category, Photo

#For authenticate
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


#Login
def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('gallery')

    return render(request, 'photos/login_register.html', {'page':page})

#Logout
def logoutUser(request):
    logout(request)
    return redirect('login')


#Register
def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(request, username=user.username, password=request.POST['password1'])

            if user is not None:
                login(request, user)
                return redirect('gallery')


    context={
        'form':form,
        'page':page
    }

    return render(request, 'photos/login_register.html', context)




#Homepage
@login_required(login_url='login')
def gallery(request):

#Filter By Categories   
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()    
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {
        'categories':categories,
        'photos':photos
    }


    return render(request, 'photos/gallery.html', context)




#Detail page
@login_required(login_url='login')
def viewPhoto(request, pk):
    photo = Photo.objects.get(id = pk)
    return render(request, 'photos/photo_detail.html', {'photo':photo})


#Adding new photo into gallery
@login_required(login_url='login')
def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data ['category'] != 'none':
            category = Category.objects.get(id = data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description = data['description'],
            image = image,
        )

        return redirect('gallery')


    context = {
        'categories':categories,
    }
    return render(request, 'photos/add_photo.html', context)
