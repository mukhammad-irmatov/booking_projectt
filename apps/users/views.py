from django.shortcuts import render, redirect
from apps.users.models import User
from django_email_verification import send_email
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.

def my_functional_view(request):
    message = ''
    if request.method == "POST":

        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if len(username) < 6:
            message = 'Your username is to short'
        elif User.objects.filter(username=username):
            message = 'This username is already taken'
        elif len(email) < 6:
            message = 'Please enter true email address'
        elif User.objects.filter(email=email):
            message = 'Your have already an account according to your email address'
        elif len(password1) < 6:
            message = 'The password must contain 6 symbols'
        elif password1 != password2:
            message = "The password don't match"
        else:
            user = get_user_model().objects.create(
                first_name=name,
                username=username,
                password=make_password(password1),
                email=email
            )
            user.is_active = False
            user.is_staff = False
            send_email(user)
            return redirect('users:confirm_needed', user.id)

    return render(request, 'signup.html', {'message': message})


def confirm_needed(request, id):
    user = User.objects.get(id=id)
    if user.is_active == True:
        return redirect('/login')
    else:
        return render(request, 'confirm_needed.html',)
