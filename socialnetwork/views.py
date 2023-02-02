from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import Login, Register, PostForm, Post
from .models import Post


def index(request):
    if request.user.is_authenticated:
        return redirect('home_page')

    hidden = True
    form_login = Login()
    form_register = Register()

    if request.method == 'POST' and 'Login' in request.POST:
        form_login = Login(request.POST)
        if form_login.is_valid():
            username = form_login.cleaned_data['email'].split('@',1)[0]
            user = authenticate(username=username, password=form_login.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home_page')
            else:
                form_login.add_error(None, 'Invalid email or password')
    elif request.method == 'POST' and 'Register' in request.POST:
        form_register = Register(request.POST)
        if form_register.is_valid():
            form_register.save()
            messages.success(request, 'Success registration')
            data = {'form_login': Login(), 'form_register': form_register, 'hidden': True, messages: messages}
            return render(request, 'index.html', context=data)
        else:
            hidden = False
    data = {'form_login': form_login, 'form_register': form_register, 'hidden': hidden}
    return render(request, 'index.html', context=data)


@login_required(login_url='index')
def home_page(request):
    user = request.user
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post(content=form.cleaned_data['content'], image=form.cleaned_data['image'], user=user)
            post.save()
            return redirect('home_page')
        else:
            print('not valid')
    else:
        posts = Post.objects.order_by('-created_at')
        data = {'form': form, 'posts': posts, 'user': user}
        return render(request, 'news.html', context=data)


@login_required(login_url='index')
def logout(request):
    django_logout(request)
    return redirect('index')


@login_required(login_url='index')
def friends(request):
    users = User.objects.select_related('profile')
    data = {'users': users}
    return render(request, 'friends.html', context=data)
