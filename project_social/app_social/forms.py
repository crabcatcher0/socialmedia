from django import forms
from .models import *


class UserForm(forms.ModelForm):
    
    class Meta:
        model = UserRegister
        fields = ['first_name', 'last_name', 'username', 'address', 'phone_number', 'email', 'password', 'profile_pic']