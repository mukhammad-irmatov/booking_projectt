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
            message = 'Your first name  is to short'
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
        return render(request, 'registration/login.html', context)

    def post(self, request):
        if request.method == "POST":
            form = UserForm(self.request, data=request.POST)
            if form.is_valid():
                phone = form.cleaned_data.get('phone')
                password = form.cleaned_data.get('password')
                user = authenticate(phone=phone, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {request.user}.")
                    return redirect("home")
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
        form = UserForm()
        return render(request=request, template_name="registration/login.html", context={"login_form": form})
