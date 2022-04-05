from django.core import validators
from django import forms

class StudentRegestration(forms.Form):
    # name = forms.CharField(empty_value='hk',error_messages={'required':'name required'})
    name = forms.CharField(validators=[validators.MaxLengthValidator(10)],error_messages={'required':'Enter name'})
    email = forms.EmailField(error_messages={'required':'email required'})

    def clean(self):
        cleaned_data = super().clean()
        valname= self.cleaned_data['name']
        valemail = self.cleaned_data['email']
        
        # if len(valname) < 4 :
        #     print(len(valname))
        #     raise forms.ValidationError('name should be more then 4 char')

        # if len(valemail) < 10:
        #     raise forms.ValidationError('email should be more then 10 char')

        
    # password = forms.CharField(widget=forms.PasswordInput)
    # mobile = forms.IntegerField(min_value=5,max_value=10)
    # agree = forms.BooleanField()
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) <4:
    #         raise forms.ValidationError('Enter more than 4 char')
    #     return valname