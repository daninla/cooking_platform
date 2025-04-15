from django import forms
from .models import Post
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class PostAddForm(forms.ModelForm):
    class Meta:
        """мета класс, указывает поведенческий характер, чертеж для класса"""
        model = Post
        fields = ['title','content','photo','category']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'photo':forms.FileInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'})
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Name",
        max_length=150,
        widget = forms.TextInput(attrs={'class':'form-control'}))

    password = forms.CharField(
        label="password",
        widget = forms.PasswordInput(attrs={'class':'form-control'}))
    