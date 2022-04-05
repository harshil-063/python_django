
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import signupform,edituserprofileform,editadminprofileform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User

# Create your views here.
# signup view function
def sign_up(request):
    if request.method == "POST":
        fm = signupform(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account created successfully')
        
    else:
        fm = signupform()
    return render(request,'enroll/signup.html',{'form':fm})

# login view function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            frm = AuthenticationForm(request=request,data=request.POST)
            if frm.is_valid():
                uname = frm.cleaned_data['username']
                upass = frm.cleaned_data['password']
                users = authenticate(username = uname,password = upass)
                if users: 
                    login(request,users)
                    # return HttpResponseRedirect('/enroll/profile/')
                    return HttpResponseRedirect('/enroll/dashboard/')
        else:
            frm =AuthenticationForm()
        return render(request,'enroll/userlogin.html',{'form':frm})
    else:
        # return HttpResponseRedirect('/enroll/profile')
        return HttpResponseRedirect('/enroll/dashboard')


# profile view
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = editadminprofileform(request.POST,instance=request.user)
                users = User.objects.all()
            else:
                fm =edituserprofileform(request.POST,instance = request.user)
                users=None
            if fm.is_valid():
                messages.success(request,'Profile updated..!!')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = editadminprofileform(request.POST,instance=request.user)
                users = User.objects.all()
            else:
                fm =edituserprofileform(request.POST,instance = request.user)
                users=None
        return render(request,'enroll/profile.html',{'name':request.user,'form':fm,'users':users})
    else:
        return HttpResponseRedirect('/enroll/login')

#  logout user 
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/enroll/login/')


# change password with old password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            frm=PasswordChangeForm(user=request.user,data=request.POST)
            # print(frm)
            if frm.is_valid():
                frm.save()
                # to update session otherwise you redirected to the login page because of session expired
                update_session_auth_hash(request,frm.user)
                messages.success(request,'Password Changed successfully')
                return HttpResponseRedirect('/enroll/profile')
        frm=PasswordChangeForm(user=request.user)
        return render(request,'enroll/changepass.html',{'form':frm})
    else:
        return HttpResponseRedirect('/enroll/login')


# change password without old password
def user_change_pass2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            frm=SetPasswordForm(user=request.user,data=request.POST)
            # print(frm)
            if frm.is_valid():
                frm.save()
                # to update session otherwise you redirected to the login page because of session expired
                update_session_auth_hash(request,frm.user)
                messages.success(request,'Password Changed successfully')
                return HttpResponseRedirect('/enroll/profile')
        frm=SetPasswordForm(user=request.user)
        return render(request,'enroll/changepass.html',{'form':frm})
    else:
        return HttpResponseRedirect('/enroll/login')


def user_detail(request,id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = editadminprofileform(instance=pi)
        return render(request,'enroll/userdetail.html',{'form':fm})
    else:
        return HttpResponseRedirect('/enroll/login/')



def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request,'enroll/dashboard.html')
        # return HttpResponseRedirect('/enroll/dashboard')
    else:
        return HttpResponseRedirect('/enroll/login')

