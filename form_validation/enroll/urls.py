from sqlite3 import converters
from django.urls import path, register_converter
from enroll import views, converters

register_converter(converters.FourDigitYearConverter,'yyyy')

urlpatterns = [
    path('regi/',views.showformdata),
    path('success/', views.thankyou),
    path('session/<yyyy:year>/',views.show_details,name ='detail'),
]