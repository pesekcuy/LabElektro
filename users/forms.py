import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from user_auth.models import User

#This will be used below
def current_year():
    return datetime.date.today().year
def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

#The form
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'year', 'password1', 'password2']
