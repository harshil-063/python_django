from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed

from django.contrib.auth.models import User

def login_success(sender,request,user, **kwargs):
    print("======================")
    print("logged in signal.....run intro......")