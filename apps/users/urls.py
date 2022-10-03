from django.urls import path
from apps.users.views import my_functional_view, confirm_needed

app_name = 'users'

urlpatterns = [
    path('signup/', my_functional_view, name='signup'),
    path('confirm_needed/<int:id>/', confirm_needed, name='confirm_needed'),
]
