from django.urls import path
from .views import home, rooms, about, blog, contact

urlpatterns = [
    path('home/', home, name='home'),
    path('rooms/', rooms, name='rooms'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
]
