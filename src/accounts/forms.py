from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User





class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'phone_number')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'phone_number')