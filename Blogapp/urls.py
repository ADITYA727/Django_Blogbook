from django.urls import path, include
from .views import *
from django.contrib.auth import views




urlpatterns = [
    path('', Homeview.as_view(), name='home'),
    path('term/', term, name='term'),
    path('home/', include('django.contrib.auth.urls')),
    path('contact/', contact, name='contact'),
    path('python/', python, name='python'),
    path('home/signup/', signup, name='signup'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('password/', change_password, name='cword'),
    path('editprofile/', editprofile, name='editprofile'),




]
