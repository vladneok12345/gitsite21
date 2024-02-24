from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name', 'email', 'body')
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={
        "id":"inputLogin",
        "class":"form-control",
        "placeholder":"Логин",
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        "type":"password",
        "id":"inputPassword",
        "class":"form-control",
        "placeholder":"Пароль",
    }))