from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Department, Course
from django.core import serializers
import json
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


# Create your views here.
def home(request):
    return render(request, 'home.html')


@login_required(login_url='/login/', redirect_field_name='next')
def newpage(request):
    return render(request, 'newpage.html')


@login_required(login_url='/login/', redirect_field_name='next')
def form(request):
    template_name = 'form.html'
    deptcontext = Department.objects.all()
    crsecontext = Course.objects.all()

    return render(request, template_name, {'Department': deptcontext, 'Course': crsecontext})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/newpage')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('/login')
