from django.shortcuts import render, redirect
from django.views import View

from .models import Contact
from .forms import ContactForm


# Create your views here.


def home(request):
    context = {}
    return render(request, 'pages/index.html', context)


def rooms(request):
    context = {}
    return render(request, 'pages/rooms.html', context)


def about(request):
    context = {}
    return render(request, 'pages/about-us.html', context)


def blog(request):
    context = {}
    return render(request, 'pages/blog.html', context)


class Contact(View):
    def get(self, request):
        contact_form = ContactForm()
        context = {'form': contact_form}
        return render(request, 'pages/contact.html', context)

    def post(request):
        if request.method == "POST":
            contact_form = ContactForm()
            if contact_form.is_valid():
                contact_form.save()
            else:
                context = {'form': contact_form}
                return render(request, 'pages/contact.html', context)
