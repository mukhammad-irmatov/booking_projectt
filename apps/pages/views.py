from django.shortcuts import render


# Create your views here.


def home(request):
    context = {}
    return render(request, 'index.html', context)


def rooms(request):
    context = {}
    return render(request, 'rooms.html', context)


def about(request):
    context = {}
    return render(request, 'about-us.html', context)


def blog(request):
    context = {}
    return render(request, 'blog.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)
