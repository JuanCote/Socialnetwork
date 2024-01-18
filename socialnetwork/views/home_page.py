from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ..forms import PostForm, Post
from ..models import Post


@login_required(login_url="index")
def home_page(request):
    user = request.user
    form = PostForm()
    posts = Post.objects.order_by("-created_at")
    data = {"form": form, "posts": posts, "user": user}
    return render(request, "homepage/news.html", context=data)


@login_required(login_url='index')
def create_post(request):
    user = request.user
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        post = Post(
            content=form.cleaned_data["content"],
            image=form.cleaned_data["image"],
            user=user,
        )
        post.save()
        return redirect("home_page")
    posts = Post.objects.order_by("-created_at")
    data = {"form": form, "posts": posts, "user": user}
    return render(request, "homepage/news.html", context=data)


@login_required(login_url="index")
def logout(request):
    django_logout(request)
    return redirect("index")