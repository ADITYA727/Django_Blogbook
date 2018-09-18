
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
    ('draft','draft'),
    ('published','published'),
    )

    title  =   models.CharField(max_length=100)
    slug   =   models.SlugField(max_length=120)
    user   =   models.ForeignKey(User, related_name='blog_post', on_delete=models.CASCADE)
    comment =  models.CharField(max_length=100)
    created =  models.DateTimeField(auto_now_add='True')
    updated =  models.DateTimeField(auto_now='True')
    status =  models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title


class LoggedInUser(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='logged_in_user',  on_delete=models.CASCADE)


class profile(models.Model):
    STATUS_marr = (
    ('single','single'),
    ('marriage','marriage'),
    )
    STATUS_gen = (
    ('male','male'),
    ('female','female'),
    )

    userprofile = models.OneToOneField(User, on_delete=models.CASCADE)
    education=models.CharField(max_length=120)
    dob=models.DateTimeField(null=True, blank=True)
    hobbies=models.CharField(max_length=120)
    study=models.CharField(max_length=120)
    Gender= models.CharField(max_length=10, choices=STATUS_gen, default='-----')
    marriage = models.CharField(max_length=10, choices=STATUS_marr, default='unmarriage')
    photo = models.ImageField( blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
