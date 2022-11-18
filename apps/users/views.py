import random

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from apps.users.forms import UserForm, LoginForm
from apps.users.models import User
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
from bookingProject.utils import send_phone_code, send_to_slack_channel


def register(request):
    message = ''
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if len(first_name) < 3:
            message = "Ism 3 ta belgidan ko'p bo'lishi lozim"
        elif len(phone) < 12:
            message = "telefon raqami 12 ta raqamdan kam bo'lishi mumkin emas"
        elif User.objects.filter(phone=phone):
            message = "Bu telefon ro'yhatdan o'tkazib bo'lingan"
        elif len(password1) < 6:
            message = "Parolingiz eng kamida 6 ta belgidan kam bo'lmasin"
        elif password1 != password2:
            message = "2 ta parol bir-biriga to'g'ri kelmadi"
        else:
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                password=make_password(password1),

            )
            code = "".join([str(random.randint(0, 100) % 10) for _ in range(4)])
            print(code)
            print(user.phone)
            # send_phone_code(user.phone, code)
            send_to_slack_channel(user.phone, code)
            selected_phone = request.POST['phone']
            request.session['selected_phone'] = selected_phone
            request.session['selected_code'] = code
            user.is_active = False
            user.is_staff = True
            user.save()
            return redirect('users:confirm')

    return render(request, 'signup/signup.html', {'message': message})


def confirm_view(request):
    selected_phone = request.session.get('selected_phone')
    selected_code = request.session.get('selected_code')
    if request.method == "POST":
        user_code = request.POST['code']
        print(user_code)
        if user_code == selected_code:
            print(True)
            user = User.objects.get(phone=selected_phone)
            user.is_active = True
            user.is_verified = True
            user.save()
            messages.success(request, "Sizning telefon raqamingiz tasdiqlandi.")
        return redirect('users:login')
    else:
        return render(request, 'registration/confirm.html')


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {'form': login_form}

        return render(request, "registration/login.html", context)

    def post(self, request):
        login_form = LoginForm(data=request.POST or None)

        if login_form.is_valid():
            data = login_form.cleaned_data
            user = authenticate(request,
                                phone=data['phone'],
                                password=data['password']
                                )
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "You have successfully logged in.")
                    return redirect('home')
                else:
                    raise Exception({"error": "Sizning profilingiz faol holatda emas"})
            else:
                raise Exception({"error": "Incorrect login or password"})
        else:
            context = {'form': login_form}

        return render(request, 'registration/login.html', context)


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'registration/login.html', {'login_form': form })