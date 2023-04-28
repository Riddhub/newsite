from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'not selected'

    class Meta:
        model = Women
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

# Personal validator function
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError(' long over 200 letters')
        return title


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
    'class': "form-control py-4", 'placeholder': "Введите имя пользователя"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
    'class': "form-control py-4", 'placeholder': "Введите пароль"}))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    # first_name = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    # last_name = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    # email = forms.CharField(widget=forms.EmailInput(attrs={
    #     'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']



