from django.urls import path
from .views import home, rooms, about, blog, Contact

urlpatterns = [
    path('home/', home, name='home'),
    path('rooms/', rooms, name='rooms'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('contact/', Contact.as_view(), name='contact'),
]
