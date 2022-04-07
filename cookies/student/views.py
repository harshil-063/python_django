from datetime import datetime, timedelta
from distutils.log import info
from email.policy import default
from ensurepip import version
from multiprocessing import context
from unicodedata import name
from urllib import response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from django.views.decorators.cache import cache_page
from django.core.cache import cache
from student import signals
from django.template.response import TemplateResponse


# Create your views here.
def setcookie(request):
    response =  render(request,'student/setcookie.html')
    # response.set_cookie('name','kumbhani',max_age=60)
    response.set_signed_cookie('name','harshil',salt='nm', expires=datetime.utcnow()+timedelta(days=2))
    return response

def getcookie(request):
    name = request.get_signed_cookie('name',salt='nmm')
    return render(request,'student/getcookie.html',{'name':name})


def delcookie(request):
    delete = render(request,'student/delcookie.html')
    delete.delete_cookie('name')
    return delete

def setsession(request):
    request.session['name'] = 'harshilllllllllk'
    request.session['lname'] = 'kumbhani'
    request.session['langs'] = 'python'
    # request.session.set_expiry()
    return render(request,'student/setsession.html')

def getsession(request):
    if 'name' in request.session:
        name = request.session['name']
        lname = request.session['lname']
        langs = request.session['langs']
        keys = request.session.values()
        # name = request.session.get('name', default='Guest')
        print(request.session.get_session_cookie_age())
        print(request.session.get_expiry_age())
        print(request.session.get_expiry_date())
        print(request.session.get_expire_at_browser_close())
        request.session.modified=True
        return render(request,'student/getsession.html',{'name':name,'lname':lname,'lang':langs,'keys':keys})
    else:
        return HttpResponse('your session is expired...')
def delsession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    # else:
    #     print("there is no session")
    request.session.flush()

    return render(request,'student/delsession.html')


def settestcookie(request):
    request.session.set_test_cookie()
    return render(request,'student/settestcookie.html')

def checktestcookie(request):
    print(request.session.test_cookie_worked())
    return render(request,'student/checktestcookie.html')

def deletetestcookie(request):
    request.session.delete_test_cookie()
    return render(request,'student/deltestcookies.html')

# def home(request):
#    ct = request.session.get('count',0)
#    newcount = ct+1
#    request.session['count'] = newcount
#    return render(request,'student/home.html',{'c':newcount})


# @cache_page(30)
def course(request):
    # mv = cache.get_or_set('fees',3000,10,version=2)
    # mv = cache.get_or_set('fees',3000,10,version=3)
    # cache.delete('fees',version=2)

    data={'name':'kk','roll':101}
    cache.set_many(data,60)
    sv = cache.get_many(data)
    print(sv)

    dv = cache.incr('roll',delta=10)
    dv = cache.decr('roll',delta=10)
    print(dv)

    # cache.delete('name')
    return render(request,'student/course.html',{'fm':sv})

def contact(request):
    return render(request,'student/contact.html')

def profile(request):
    mv=cache.get('movie','has_expired')
    if mv=='has_expired':
        cache.set('movie','RRR',30)
        mv=cache.get('movie')
        return render(request,'student/course.html',{'fm':mv})



# def home(request):
#     # a=10/0
#     # return HttpResponse("hello")
#     signals.notification.send(sender=None,request=request,user=['harshil','kumbhani'])
#     return HttpResponse("this is home page")

def home(request):
    print("this is view")
    return HttpResponse("this is home page")


def user_info(request):
    print("i am user info view")
    info = {'name':'harshil','surname':'patel'}
    print(info.get('name'))
    return TemplateResponse(request,'employee/user.html',info)