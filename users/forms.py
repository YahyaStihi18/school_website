from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.hashers import make_password



class UserRegisterFrom(UserCreationForm):
    email = forms.EmailField(label='Email')
    class Meta:
        model = User
        fields = ['username','email']
    def validate_password(self, value: str) -> str:
        return make_password(value)
