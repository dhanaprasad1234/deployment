from .models import store
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import store

class StoreForm(forms.ModelForm):
    class Meta:
        model = store
        fields = ['Name','Description','Price']

class User(UserCreationForm):
    class Meta:
        model = User
        fields =  ['username','password1', 'password2','email','first_name','last_name',]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)