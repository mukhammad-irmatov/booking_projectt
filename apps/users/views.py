from django.shortcuts import render, redirect
from apps.users.forms import UserForm
from apps.users.models import CustomUser
from django_email_verification import send_email
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.

def my_functional_view(request):
    message = ''
    if request.method == "POST":

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if len(first_name) < 5:
            message = 'Your username is to short'
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
            send_email(user)
            return redirect('users:confirm_needed', user.id)

    return render(request, 'signup/signup.html', {'message': message})


def confirm_needed(request, id):
    user = UserForm.objects.get(id=id)
    if user.is_active == True:
        return redirect('/login')
    else:
        return render(request, 'signup/confirm_needed.html', )
