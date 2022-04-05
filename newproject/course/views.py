from ctypes import Structure
from email.mime import application
from gettext import install
from importlib.metadata import files
from msilib.schema import Directory
import django
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def learn_django(request):
    # return HttpResponse('welcome django')
    return render(request,'course/courseone.html',{'title':'learn django','cname':'django'})

def learn_python(request):
    return render(request,'course/coursetwo.html',{'title':'learn django','cname':'python'})