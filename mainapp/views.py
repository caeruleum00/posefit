from django.shortcuts import render,redirect,get_object_or_404
from django.conf import settings

# Create your views here.
# def home(request):
#     return render(request, 'home.html')

def home(request):
    return render(request, 'home.html')

def category(request):
    return render(request, 'category.html')