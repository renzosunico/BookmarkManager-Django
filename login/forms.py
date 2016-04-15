from django import forms
from django.contrib.auth.forms import AuthenticationForm, forms
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={'required': 'required', 'class': 'form-control input-md', 'placeholder': 'Username'}
        )
    )

    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control input-md',
                'placeholder': 'Password',
                'minlength': 8,
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'password')