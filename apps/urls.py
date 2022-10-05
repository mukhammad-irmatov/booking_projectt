from django.urls import path, include

urlpatterns = [
    path('pages/', include('pages.urls')),
    path('user/', include('users.urls')),
]
