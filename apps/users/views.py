from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from apps.users.forms import UserForm
from apps.users.models import CustomUser
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.

def register(request):
    message = ''
    if request.method == "POST":

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if len(first_name) < 3:
            message = 'Your first  name  is to short'
        elif len(phone) < 12:
            message = 'the number is small, the number should be 12'
        elif CustomUser.objects.filter(phone=phone):
            message = 'This Phone is already taken'
        elif len(password1) < 6:
            message = 'The password must contain 6 symbols'
        elif password1 != password2:
            message = "The password don't match"
        else:
            user = CustomUser.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                password=make_password(password1),

            )
            user.is_active = False
            user.is_staff = False
            user.save()
            return redirect('users:login')

    return render(request, 'signup/signup.html', {'message': message})


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {'form': login_form}

        return render(request, "registration/login.html", context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

            messages.success(request, "You have successfully logged in.")

            return redirect('home')
        else:
            context = {'form': login_form}

        return render(request, 'pages/index.html', context)
