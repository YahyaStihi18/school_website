from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.hashers import make_password
from .models import Profile



class UserRegisterFrom(UserCreationForm):
    email = forms.EmailField(label='Email')
    class Meta:
        model = User
        fields = ['username','email']
    def validate_password(self, value: str) -> str:
        return make_password(value)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


