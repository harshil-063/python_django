from ensurepip import version
from signal import signal
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.db.models.signals import pre_delete,post_delete,pre_save,post_save,pre_migrate,post_migrate
from django.contrib.auth.models import User,Group
from django.dispatch import Signal, receiver
from django.core.signals import request_started,request_finished,got_request_exception
from django.db.backends.signals import connection_created
from django.core.cache import cache

@receiver(user_logged_in,sender =User)
def login_success(sender,request,user, **kwargs):

    ct = cache.get('count',0,version=user.pk)
    newcount = ct+1
    
    cache.set('count',newcount,60*60*24,version=user.pk)

    print(f"user version={user.pk}")
    print(f"your todays login {newcount}")
    print(cache.get('count',version=user.pk))

    ip = request.META.get("REMOTE_ADDR")
    print(ip)
# user_logged_in.connect(login_success,sender=User)



@receiver(user_logged_out,sender =User)
def log_out(sender,request,user, **kwargs):
    print("===========================================================================================")
    print("logged out signal.....run outro......")
    print(f"sender = {sender}")
    print(f"request={request}")
    print(f"user={user}")
    print(f"password={user.password}")
    print(f"kwargs={kwargs}")
# user_logged_out.connect(log_out,sender=User)


@receiver(user_login_failed)
def login_failed(sender,request,credentials, **kwargs):
    print("===========================================================================================")
    print("..............login failed.............")
    print(f"sender = {sender}")
    print(f"username={credentials.get('username','password')}")
    print(f"credentials={credentials}")
    # print(f"Byy {user}")
# user_logged_out.connect(log_out,sender=User)

# pre save signal
# @receiver(pre_save,sender=User)
# def at_beginning_save(sender,instance, **kwargs):
#     print("===========================================================================================")
#     print(".............At Beginning save............")
#     print(f"sender = {sender}")
#     print(f"instance = {instance}")
#     print(f"kwargs={kwargs}")
#pre_save.connect(at_beginning_save,sender=at_beginning_save)

# post save signal
# @receiver(post_save,sender=User)
# def at_ending_save(sender,instance, **kwargs):
#     print("===========================================================================================")
#     print(".............At ending of save............")
#     print(f"sender = {sender}")
#     print(f"instance = {instance}")
#     print(f"kwargs={kwargs}")
#post_save.connect(at_ending_save,sender=User)


# pre delete signal
# @receiver(pre_delete,sender=User)
# def at_beginning_delete(sender,instance, **kwargs):
#     print("===========================================================================================")
#     print(".............At Beginning Delete............")
#     print(f"sender = {sender}")
#     print(f"instance = {instance}")
#     print(f"kwargs={kwargs}")
#pre_delete.connect(at_beginning_delete,sender=User)


# post delete signal
# @receiver(post_delete,sender=Group)
# def at_ending_delete(sender,instance, **kwargs):
#     print("===========================================================================================")
#     print(".............At ending of Delete............")
#     print(f"sender = {sender}")
#     print(f"instance = {instance}")
#     print(f"kwargs={kwargs}")
#post_delete.connect(at_ending_delete,sender=User)


# @receiver(request_started)
# def at_start_request(sender,environ,**kwargs):
#     print("================================================")
#     print("At Starting Request............")
#     print(f"sender={sender}")
#     print(f"environ={environ}")



# @receiver(request_finished)
# def at_ending_request(sender,**kwargs):
#     print("================================================")
#     print("At ending Request............")
#     print(f"sender={sender}")
#     print(f"kwargs={kwargs}")


# @receiver(got_request_exception)
# def at_request_exception(sender,request,**kwargs):
#     print("================================================")
#     print("At Request exception............")
#     print(f"sender={sender}")
#     print(f"request={request}")
#     print(f"Kwargs={kwargs}")


# @receiver(pre_migrate)
# def before_install_app(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
#     print("=====================================================")
#     print("before install app............")
#     print(f"sender ={sender}")
#     print(f"app config= {app_config}")
#     print(f"verbosity={verbosity}")
#     print(f"interactive={interactive}")
#     print(f"using={using}")
#     print(f"plan={plan}")
#     print(f"apps={apps}")
#     print(f"kwargs={kwargs}")
    


# @receiver(post_migrate)
# def at_end_migrate_flush(sender,app_config,verbosity,interactive,using,plan,apps,**kwargs):
#     print("=====================================================")
#     print("at end migrate flush............")
#     print(f"sender ={sender}")
#     print(f"app config= {app_config}")
#     print(f"verbosity={verbosity}")
#     print(f"interactive={interactive}")
#     print(f"using={using}")
#     print(f"plan={plan}")
#     print(f"apps={apps}")
#     print(f"kwargs={kwargs}")
    


# @receiver(connection_created)
# def conn_db(sender,connection,**kwargs):
#     print("=====================================================")
#     print("Initial connection to database............")
#     print(f"sender ={sender}")
#     print(f"connection= {connection}")
#     print(f"kwargs={kwargs}")



# notification = Signal(providing_args=["request", "user"])

# @receiver(notification)
# def show_notification(sender,**kwargs):
#     print(sender)
#     print(f"{kwargs}")
#     print("Notification")