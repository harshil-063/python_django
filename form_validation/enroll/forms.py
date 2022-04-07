from dataclasses import field, fields
from pyexpat import model
from tkinter import Widget
from unicodedata import name
from django.core import validators
from django import forms

from .models import User

# this function is for custom validation
def start_with_s(self):
    if(self[0] != 's'):
        raise forms.ValidationError('name should start with s')

class StudentRegestration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        
        # labels = {'name':'enter name','email':'enter email','password':'enter password'}
        # help_texts = {'name':'enter your full name','email':'enter your email'}
        error_messages = {'name':{'required':'name required'},'email':{'required':'email required'}}
        widgets = {
            # 'password':forms.PasswordInput(),
            'name': forms.TextInput(attrs={'class':'myclass','placeholder':'enter your name'}),
            'email':forms.TextInput(attrs={'class':'myclass','placeholder':'enter your email'}),
            'password':forms.PasswordInput(attrs={'class':'myclass','placeholder':'enter your password'})
            }

# class StudentRegestration(forms.Form):
#     # name = forms.CharField(min_length=5,max_length=10,error_messages={'required':'name is required'},strip=False)
#     # name = forms.CharField(validators=[validators.MaxLengthValidator(10)]) #this is example of builtin validators
#     # name = forms.CharField(validators=[start_with_s]) #this is example of custom validation
#     name = forms.CharField(error_messages={'required':'name is required'})
#     email = forms.EmailField(error_messages={'required':'email is required'})
#     password = forms.CharField(error_messages={'required':'password is required'})
#     # cpassword = forms.CharField(error_messages={'required':'cpassword is required'})
#     # roll = forms.IntegerField(min_value=5)
#     # price = forms.DecimalField(min_value=5,max_value=50,max_digits=4,decimal_places=1)
#     # rate = forms.FloatField(min_value=5,max_value=15)
#     # agree = forms.BooleanField()

#     # this function is for mach password and cpassword
#     # def clean(self):
#     #     cleaned_data = super().clean()
#     #     valpwd = cleaned_data['password']
#     #     valcpwd = cleaned_data['cpassword']
#     #     if valpwd != valcpwd:
#     #         raise forms.forms.ValidationError('Password does not match')



#     # clean method use to validate perticular field
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 4:
#     #         raise forms.ValidationError('enter more then 4 char')
#     #     return valname

#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if len(valemail) < 10:
#     #         raise forms.ValidationError('enter more then 10 char email')
#     #     return valemail