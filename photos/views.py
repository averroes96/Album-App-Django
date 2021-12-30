from django.shortcuts import redirect, render
from .models import Category,Photo

# Create your views here.

def gallery(request):
    
    categories = Category.objects.all()
    photos = Photo.objects.all()

    if request.method == "GET":
        category = request.GET.get("category")

        if(category != None):
            photos = Photo.objects.filter(category__name=category)

    context = {
        "categories" : categories,
        "photos" : photos
    }
    return render(request, "photos/gallery.html", context)

def add(request):
    categories = Category.objects.all()

    if request.method == "POST" :
        data = request.POST
        image = request.FILES.get("image")
        category = None

        if data["category"] != "none":
            category = Category.objects.get(id=data["category"])
        elif data["new_category"].strip() != "":
            category, created = Category.objects.get_or_create(name=data["new_category"])

        photo = Photo.objects.create(
            category = category,
            description = data["description"],
            image=image
        )

        return redirect("gallery")

    context = {
        "categories" : categories,
    }

    return render(request, "photos/add.html", context)

def photo(request, pk):
    photo = Photo.objects.get(id=pk)
    context = { "photo" : photo }
    return render(request, "photos/photo.html", context)
