from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.urls import reverse

from authnapp.forms import CustomUserLoginForm, CustomUserRegisterForm

def all_auth(request):
    context = {
        'login_form': CustomUserLoginForm(),
        'register_form': CustomUserRegisterForm()
    }

    return render( request,'authnapp/login.html', context )
    

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))

def login(request):
    login_form = CustomUserLoginForm(data = request.POST or None)
    if request.method == "POST" and login_form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]

    user = auth.authenticate(username=username, password=password)
    if user and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect(reverse("main"))
    return HttpResponseRedirect(reverse("all_auth"))

def register(request):
    
    if request.method == "POST":
        register_form = CustomUserRegisterForm(request.POST or None)
        if  register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse("auth:all_auth"))

    else: 
        return HttpResponseRedirect(reverse("auth:all_auth"))
