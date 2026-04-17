from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def register_pg(request):
    context = {}
    return render(request, 'registration/register.html', context)

def login_pg(request):
    context= {}
    return render(request, 'registration/login.html', context)