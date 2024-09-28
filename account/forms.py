from django.forms import Form, PasswordInput, TextInput, CharField, EmailInput
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Login(Form):

    username = CharField(widget=TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = CharField(widget=PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))


class Signup(Form):
    username = CharField(widget=TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password1 = CharField(widget=PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password1'}))
    password2 = CharField(widget=PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password2'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken.")
        return username

    def clean_password2(self):
        
        password1 = self.cleaned_data.get("password1")
        password2 =self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            return ValidationError('password not match')
        return password2

    def save(self):

        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1']
        )
        return user