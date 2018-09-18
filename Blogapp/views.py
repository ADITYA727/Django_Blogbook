from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model, update_session_auth_hash
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,  PasswordChangeForm
from django.urls import reverse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.views.generic import TemplateView
from django.contrib.auth.models import User
import requests



# Create your views here.
class Homeview(TemplateView):
    template_name='home.html'

    def post(self, request):
        if request.method == 'POST':
            form = CreatePost(request.POST)
            if form.is_valid():
                post =form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('home')

        else:
            form = CreatePost()
            return render(request, self.template_name, {'form':form})

    def get(self, request):
        form = CreatePost()
        post=Post.objects.all().order_by('-created')
        users=User.objects.all()
        context = {'post':post, 'form':form, 'users': users,}
        return render(request, self.template_name, context)






def term(request):
    return render(request, 'termcon.html')

def python(request):
    return render(request, 'python.html')



def contact(request):
    return render(request, 'contact.html')







def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('home')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            new_user=form.save(commit=False)
            new_user.save()
            profile.objects.create(userprofile = new_user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



def editprofile(request):
    if request.method == 'POST':
        autoform = AutoEditForm(data=request.POST or None, instance=request.user)
        makeform = MakeEditForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)
        if autoform.is_valid() and makeform.is_valid():
            autoform.save()
            makeform.save()
            return redirect('home')

    else:
        autoform = AutoEditForm(instance=request.user)
        makeform = MakeEditForm( instance=request.user.profile)
        context={'autoform':autoform,'makeform':makeform,}
        return render(request, 'profile.html', context)
