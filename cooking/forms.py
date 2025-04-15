from django import forms
from .models import Post

class PostAddForm(forms.ModelForm):
    class Meta:
        """мета класс, указывает поведенческий характер, чертеж для класса"""
        model = Post
        fields = ['title','content','photo','category']
