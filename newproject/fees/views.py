from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def fees_django(request):
    return render(request,'course/courseone.html',{'title':'fees django','fees':'5000'})

def fees_python(request):
    return render(request,'course/coursetwo.html',{'title':'fees python','fees':'10000'})