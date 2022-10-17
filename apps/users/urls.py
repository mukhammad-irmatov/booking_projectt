from django.urls import path
from apps.users.views import register, LoginView

app_name = 'users'

urlpatterns = [
    path('signup/', register, name='signup'),
    path('login/', LoginView.as_view(), name='login'),

]
