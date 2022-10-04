from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('user/', include('users.urls')),
]
