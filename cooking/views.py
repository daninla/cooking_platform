from django.shortcuts import render,redirect
from .models import Category,Post,Comment
from django.db.models import F,Q
from .forms import PostAddForm,LoginForm, RegistrationForm,CommentForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from .serializers import PostSerializer,CategorySerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

class Index(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'cooking/index.html'
    extra_context = {'title':'Главная страница'}


class PostDetail(DetailView):
    model = Post
    template_name = 'cooking/article_detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(pk=self.kwargs['pk'])
        Post.objects.filter(pk=self.object.pk).update(watched=F('watched')+ 1)

        context['ext_posts'] = Post.objects.all().exclude(pk=self.object.pk).order_by('-watched')[:5]
        context['title'] = self.object.title
        context['comments'] = Comment.objects.filter(post=post)

        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm

        return context


class AddPost(CreateView):
    form_class = PostAddForm
    template_name = 'cooking/article_add_form.html'
    extra_context = { 'title': 'Добавить статью'}

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(UpdateView):
    model = Post
    form_class = PostAddForm
    template_name = 'cooking/article_add_form.html'


class PostDelete(DeleteView):
        model = Post
        success_url = reverse_lazy('index')
        template_name = 'cooking/post_delete.html'
        context_object_name = 'post'


class SearchResalt(Index):
    def get_queryset(self):
        word = self.request.GET.get('q')
        posts = Post.objects.filter(
            Q(title__icontains=word) | Q(content__icontains=word)
        )
        return posts


def add_comment(request,post_id):
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = Post.objects.get(pk=post_id)
        comment.save()
        messages.success(request,'Коментарий добавлен')
    return redirect('post_detail',post_id)



def category_list(request,pk):
    posts = Post.objects.filter(category_id = pk)
    context = {
        'title':posts[0].category,
        'posts':posts,
    }
    return render(request,'cooking/index.html',context)


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,'Вы успешно вошли в аккаунт')
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


def profile(request,user_id):
    user = User.objects.get(pk=user_id)
    posts = Post.objects.filter(author=user)
    context = {
        'user':user,
        'posts':posts
    }
    return render(request,'cooking/profile.html',context)


class UserChangePassword(PasswordChangeView):
    success_url = reverse_lazy('index')


class CookingAPI(ListAPIView):
    queryset = Post.objects.filter(is_published = True)
    serializer_class = PostSerializer


class CookingAPIDetail(RetrieveAPIView):
    queryset = Post.objects.filter(is_published = True)
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

class CookingCategoryAPI(ListAPIView):
    queryset = Category.objects.filter(is_published = True)
    serializer_class = CategorySerializer


class CookingCategoryAPIDetail(RetrieveAPIView):
    queryset = Category.objects.filter(is_published = True)
    serializer_class = CategorySerializer

