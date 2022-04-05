from django.contrib import messages
from unicodedata import name
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import StudentRegestration
from .models import User
# Create your views here.


# this function will add and retrive data from database
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegestration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            reg = User(name=name,email=email,password=password)
            reg.save()
            # messages.add_message(request, messages.SUCCESS,'your account has been created !!!!')
            messages.success(request,'your account has been created !!!!')
            messages.info(request,'now you can log in!!!!')
            # print(messages.get_level(request))
            messages.error(request,'error occured')
            # messages.warning(request,'warning')
            # # messages.set_level(request,messages.DEBUG)
            # # messages.debug(request,'now you can log in!!!!')
            # # print(messages.get_level(request))
            fm = StudentRegestration()
    else:
        fm = StudentRegestration()
    stud = User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})



# this function will update data in database
def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegestration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        stud = User.objects.all()
        return HttpResponseRedirect('/')
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegestration(instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm,'id':id})



# this function will delete data from database
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    # pi = User.objects.get(pk=id)
    # pi.delete()
    # return HttpResponseRedirect('/')