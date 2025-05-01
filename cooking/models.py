from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    """Категория новостей"""
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('category_list', kwargs={'pk':self.pk})
    


class Post(models.Model):
    """Для новостных постов"""
    title = models.CharField(max_length=255)
    content = models.TextField(default='скоро тут будет статья')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    watched = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(User, default=None, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='пост')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    text = models.TextField(verbose_name='коментарий')
    created_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

