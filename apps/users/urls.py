from django.urls import path
from apps.users.views import register, LoginView, confirm_view, login_view

app_name = 'users'

urlpatterns = [
    path('signup/', register, name='signup'),
    path('confirm/', confirm_view, name='confirm'),
    # path('login/', LoginView.as_view(), name='login'),
    path('login/', login_view, name='login')

]
