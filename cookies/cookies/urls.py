"""cookies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from student import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('setc/',views.setcookie),
    path('getc/',views.getcookie),
    path('delc/',views.delcookie),
    path('sets/',views.setsession),
    path('gets/',views.getsession),
    path('dels/',views.delsession),
    path('settc/',views.settestcookie),
    path('checktc/',views.checktestcookie),
    path('deltc/',views.deletetestcookie),
    path('home/',views.home),
    path('course/',cache_page(50)(views.course)),
    path('contact/',views.contact),
    path('profile/',views.profile),
]
