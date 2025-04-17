from django.shortcuts import render,redirect
from .models import Category,Post
from django.db.models import F
from .forms import PostAddForm,LoginForm, RegistrationForm
from django.contrib.auth import login, logout

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
        form = PostAddForm(request.POST,request.FILES)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            post.save()
            return redirect('post_detail', post.pk)
    else: 
        form = PostAddForm()

    context = {
        'form': form,
        'title': 'Добавить статью'
    }
    return render(request, 'cooking/article_add_form.html', context)


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('index')
    else:
        form = LoginForm()
        
    context = {
        'title':'Авторизация пользователя',
        'form':form
    }
    return render(request,'cooking/login_form.html', context)


def user_logout(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = RegistrationForm()

    context = {
        'title':'Регистрация пользователя',
        'form':form,
    }
    return render(request,'cooking/register.html',context)