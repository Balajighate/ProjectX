from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import Employee

from django import forms

from captcha.fields import CaptchaField 

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput,TextInput


# register / create user

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','password1','password2']


class LoginForm(AuthenticationForm):
    class Meta:
        username = forms.CharField(widget=TextInput)
        password = forms.CharField(widget=PasswordInput)
    captcha = CaptchaField() 


class CreateRecordForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['first_name','last_name','email','mobileno','address','city','state','country']


class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['first_name','last_name','email','mobileno','address','city','state','country']

