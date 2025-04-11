from django.shortcuts import render
from .models import Category,Post
from django.db.models import F

def index(request):
    posts = Post.objects.all()
    context = {
        'title':'Главная страница',
        'posts':posts,
    }
    return render(request,'cooking/index.html',context)

def category_list(request,pk):
    posts = Post.objects.filter(category_id = pk)
    context = {
        'title':posts[0].category,
        'posts':posts,
    }
    return render(request,'cooking/index.html',context)


def post_detail(request, pk):
    """Страничка статьи"""
    article = Post.objects.get(pk=pk)
    Post.objects.filter(pk=pk).update(watched = F('watched')+1)
    context = {
        'title': article.title,
        'post': article,
    }
    return render(request,'cooking/article_detail.html',context)

