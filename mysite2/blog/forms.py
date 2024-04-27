from .models import Comment, User
from django import forms
from .models import Post
from .models import PostPoint

class SearchForm(forms.Form):
    query=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control mr-sm-2',
        'type':'search',
        'placeholder':'Search',
        'aria-label':'Search'
    }))
class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ('first_name', 'last_name', 'username',
                  'email')
class UserCreateForm(forms.ModelForm):
    password=forms.CharField(max_length=40,widget=forms.PasswordInput())
    class Meta:
        model=User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password')
class PostPointForm(forms.ModelForm):
    class Meta:
        model = PostPoint
        fields = ('post_header', 'post_point_text', 'post_images')
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','short_description','image','tags')

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