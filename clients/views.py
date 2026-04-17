from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def dashboard_pg(request):
    current_url = request.path[1:-1]
    context = {'current_url':current_url}
    return render(request, 'clients/base/index.html', context)

