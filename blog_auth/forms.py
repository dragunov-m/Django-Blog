# Core Django
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

User = get_user_model()


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Email",
                "type": "email",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "type": "password",
                "placeholder": "Password",
            }
        ),
    )


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileUpdateForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               label='New Password', required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'avatar',)
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
