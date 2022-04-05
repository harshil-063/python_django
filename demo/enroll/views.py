import email
from unicodedata import name
from django.http import HttpResponseRedirect
from django.shortcuts import render
from enroll.models import Employee, Student
from .forms import StudentRegestration

# Create your views here.

def studentinfo(request):
    stud = Student.objects.all()
    return render(request, 'enroll/studetails.html', {'stu': stud})

def empinfo(request):
    empl = Employee.objects.all()
    return render(request,'enroll/empdetails.html',{'emp':empl})

def thankyou(request):
    return render(request,'enroll/success.html')

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegestration(request.POST)
        if fm.is_valid():
            print("form validated")
            print('NAME:',fm.cleaned_data['name'])
            print('EMAIL:',fm.cleaned_data['email'])
            # print('PASSWORD:',fm.cleaned_data['password'])
            # print('MOBILE:',fm.cleaned_data['mobile'])
            # print('agree:',fm.cleaned_data['agree'])
            # return render(request,'enroll/success.html',{'nm':fm.cleaned_data['name']})
            return HttpResponseRedirect('/enroll/success/')

    else:
        fm = StudentRegestration()
        print("this from get request")
    fm = StudentRegestration()
    return render(request,'enroll/userregestration.html',{'form':fm})



    # fm = StudentRegestration(auto_id=True,label_suffix=' ', initial={'name':'','email':''})
    # fm.order_fields(field_order=['email','name'])
    # return render(request,'enroll/userregestration.html',{'form':fm})