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

    def post(self, request):
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']

            user_message = Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message,
            )
            user_message.save()
            return redirect('contact')
        else:
            context = {'form': contact_form}
            return render(request, 'pages/contact.html', context)
