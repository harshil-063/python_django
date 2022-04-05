import email
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import User
from .forms import StudentRegestration

# Create your views here.

def thankyou(request):
    return render(request,'enroll/success.html')

def show_details(request,year):
    print(year)
    student = {'yr':year}
    # if my_id == 1:
    #     student = {'id':my_id,'name':'harshil'}
    # if my_id == 2:
    #     student = {'id':my_id,'name':'milan'}
    # if my_id == 3:
    #     student = {'id':my_id,'name':'preet'}
    return render(request,'enroll/show.html',student)

# def home(request):
#     return render(request,'enroll/home.html')

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegestration(request.POST)
        # print(fm)
        print('this is from post reuest')
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            # cpassword = fm.cleaned_data['cpassword']
            # agree = fm.cleaned_data['agree']
            # price = fm.cleaned_data['price']
            # roll = fm.cleaned_data['roll']
            # rate = fm.cleaned_data['rate']
            
            print("Name:",name)
            print("Email:",email)
            print("password:",password)
            # print("cpassword:",cpassword)
            
            # for insert the data
            reg = User(id=7,name=name,email=email,password=password)
            reg.save()

            # for update the data
            # reg = User(id=2,name=name,email=email,password=password)
            # reg.save()

            # for delete the data
            reg = User(id=1)
            reg.delete()
            # print("roll:",roll)
            # print("Agree:",agree)
            # print("Price:",price)
            # print("rate:",rate)
            # return render(request,'enroll/success.html',{'nm':name})
            # return HttpResponseRedirect('/enroll/success/')
    else:
        fm = StudentRegestration()
        print('this is from get request')
    return render(request,'enroll/userregestration.html',{'form':fm})