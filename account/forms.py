from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegForm(UserCreationForm):
    pass

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名 ', max_length=30)
    password = forms.CharField(label='密码 ',widget=forms.PasswordInput())

