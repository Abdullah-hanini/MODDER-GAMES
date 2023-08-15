from django import forms
from .models import new_user
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = new_user
        fields = ['first_name','last_name','user_name','email','phone_number','password1','password2']


