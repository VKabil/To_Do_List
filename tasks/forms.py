# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistrationForm(UserCreationForm):
    age = forms.IntegerField()

    class Meta:
        # model = User
        fields = ['username', 'email', 'password1', 'password2', 'age']

class LoginForm(AuthenticationForm):
    pass
