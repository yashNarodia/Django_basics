# Views.py file

from django.shortcuts import render
from django.template import Template
from .model import *

def homepage(request):
    return render (request,'homepage.html')
    
def contact(request):
    return render (request,'contact.html')
    
def about(request):
    return render (request,'about.html')

def database(request):
    Student = Students.objects.all()
    context = {'Students':Student ,}
    return render (request,'database.html',context)

