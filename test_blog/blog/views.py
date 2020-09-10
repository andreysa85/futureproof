from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.core.paginator import Paginator


# Create your views here.


def home(request):
    data = dict()
    if request.method == 'GET':
        if request.user.is_authenticated:
            posts = Post.objects.all().order_by('-time_creation')
            data['posts'] = posts
            paginator = Paginator(posts, 5)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            data['page_obj'] = page_obj
            return render(request, 'blog/home.html', context=data)
        else:
            posts = Post.objects.all().order_by('-time_creation')[:10]
            data['posts'] = posts
            paginator = Paginator(posts, 5)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            data['page_obj'] = page_obj
            return render(request, 'blog/home.html', context=data)


def login(request):
    return render(request, 'blog/login.html')


def entry(request):
    if request.method == 'GET':
        return render(request, 'blog/login.html')
    elif request.method == 'POST':
        data = dict()
        _login = request.POST.get('login')
        _pass = request.POST.get('pass')
        user = authenticate(request, username=_login, password=_pass)
        if user is not None:
            data['color'] = 'green'
            data['report'] = 'Вы успешно авторизированы !!! '
            auth_login(request, user)
            return redirect('/home')
        else:
            data['color'] = 'res'
            data['report'] = 'Ви ввели неверные данные.'
            return render(request, 'blog/login.html', context=data)


def exit(request):
    logout(request)
    return redirect('/home')


def details(request, iid: int):
    data = dict()
    post = Post.objects.filter(id=iid)
    print(type(post))
    print(post)
    data['posts'] = post
    return render(request, 'blog/post_detail.html', context=data)
