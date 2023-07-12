
from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.

def index (request):

    context = {
        'about_me':settings.DATA["ABOUT"]
    }

    return render(request, 'index.html',context)

def projects(request):

    return render(request,'projects.html',{})

def skills(request):
    context = {}
    return render(request,'skills.html',{})