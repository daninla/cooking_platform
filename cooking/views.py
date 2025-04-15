from django.shortcuts import render,redirect
from .models import Category,Post
from django.db.models import F
from .forms import PostAddForm

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
    ext_post = Post.objects.all().order_by('-watched')[:4]
    context = {
        'title': article.title,
        'post': article,
        'ext_posts':ext_post,
    }
    return render(request,'cooking/article_detail.html',context)


def add_post(request):
    if request.method == "POST":
        pass
    else:
        form = PostAddForm()

    context = {
        'form': form,
        'title': 'Добавить статью'
    }
    return render(request, 'cooking/article_add_form.html', context)