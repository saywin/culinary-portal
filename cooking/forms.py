from django import forms
from .models import Post
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


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
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
