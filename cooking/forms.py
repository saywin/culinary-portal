from django import forms
from .models import Post
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class PostAddForm(forms.ModelForm):
    """Форма для додавання статті від користувача"""

    class Meta:
        model = Post
        fields = ["title", "content", "photo", "category"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "photo": forms.FileInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }


class LoginForm(AuthenticationForm):
    """Форма для аутентифікації користувача"""

    username = forms.CharField(
        label="Ім'я користувача",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )


class RegistrationForm(UserCreationForm):
    """Форма для реєстрації користувача"""

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(
        max_length=150,
        label="Ім'я користувача",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ім'я користувача"}
        ),
    )
    email = forms.CharField(
        max_length=150,
        label="Email",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Введіть ваш email"}
        ),
    )
    password1 = forms.CharField(
        max_length=150,
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Пароль"}
        ),
    )
    password2 = forms.CharField(
        max_length=150,
        label="Підтвердження пароля",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Підтвердіть пароль",
            }
        ),
    )
