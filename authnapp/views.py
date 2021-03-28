from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse


def login(request):
    return render(request, 'authnapp/login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))

# Create your views here.
