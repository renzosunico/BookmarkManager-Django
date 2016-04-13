from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):

    confirm_password = forms.CharField(
        max_length=32,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control input-md', 'minlength': 6,
                   'placeholder': 'Retype Password',
                   'required': 'required'
                   })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')
        widgets = {
            'username': forms.TextInput(
                attrs={'required': 'required', 'class': 'form-control input-md', 'placeholder': 'Username'}),
            'email': forms.EmailInput(
                attrs={'required': 'required', 'class': 'form-control', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control input-md',
                'placeholder': 'Password',
                'minlength': 8,
            })
        }

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'Your password did not matched.'
            )

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user
