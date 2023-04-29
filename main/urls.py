from django.urls import path
from .views import home, about, contact

urlpatterns = [
    path('', home, name='main-home'),
    path('about/', about, name='main-about'),
    path('contact/', contact, name='main-contact')
]