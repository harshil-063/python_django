from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/',views.sign_up),
    path('login/',views.user_login),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.user_logout),
    path('changepass/',views.user_change_pass,name='changepass'),
    path('changepass2/',views.user_change_pass2,name='changepass2'),
    path('userdetail/<int:id>',views.user_detail,name='userdetail'),
    path('dashboard/',views.user_dashboard,name='dashboard'),
]
