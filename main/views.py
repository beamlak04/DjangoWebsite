from multiprocessing import current_process
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import resolve

# Create your views here.


def index(request):
    current_pg = resolve(request.path_info).url_name
    context = {'current_pg': current_pg}
    return render(request, 'main/index.html', context)


def about(request):
    current_pg = resolve(request.path_info).url_name
    context = {'current_pg': current_pg}
    return render(request, 'main/about.html', context)


def contact(request):
    current_pg = resolve(request.path_info).url_name
    context = {'current_pg': current_pg}
    return render(request, 'main/contact.html', context)


