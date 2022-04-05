from django.urls import path
from enroll import views

urlpatterns = [
    path('stud/',views.studentinfo),
    path('emp/', views.empinfo),
    path('regi/', views.showformdata),
    path('success/', views.thankyou),
]