# Views.py file

from django.shortcuts import render
from django.template import Template

def homepage(request):
    return render (request,'homepage.html')
    
def contact(request):
    return render (request,'contact.html')
    
def about(request):
    return render (request,'about.html')