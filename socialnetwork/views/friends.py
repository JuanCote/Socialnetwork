import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q

from ..models import Friends



@login_required(login_url="index")
def friends_all(request):
    users = User.objects.exclude(username=request.user)
    subscriptions = Friends.objects.filter(user1=request.user)
    print(subscriptions[0].user1.first_name)
    subscriptions = [x.user2 for x in subscriptions]
    data = {
        "users": users,
        "current_user": request.user,
        "subscriptions": subscriptions,
        "page": 0,
    }
    return render(request, "profile/friends/friends_all.html", context=data)


@login_required(login_url="index")
def friends_subscriptions(request):
    subscriptions = Friends.objects.filter(user1=request.user)
    subscriptions = [x.user2 for x in subscriptions]
    data = {"subscriptions": subscriptions, "current_user": request.user, "page": 2}
    return render(request, "profile/friends/friends_subscriptions.html", context=data)


@login_required(login_url="index")
def friends_subscribers(request):
    subscribers_subscriptions = Friends.objects.filter(
        Q(user1=request.user.id) | Q(user2=request.user.id)
    )
    subscriptions, subscribers = [], []
    subscribers = [x.user1 for x in subscribers_subscriptions if x.user2 == request.user]
    subscriptions = [x.user2 for x in subscribers_subscriptions if x.user1 == request.user]
    data = {
        "subscribers": subscribers,
        "subscriptions": subscriptions,
        "current_user": request.user,
        "page": 1,
    }
    return render(request, "profile/friends/friends_subscribers.html", context=data)


@login_required(login_url="index")
def subscribe(request):
    data = json.loads(request.body)
    users = User.objects.filter(username__in=(data["user1"], data["user2"]))
    if int(users[0].username) == data["user1"]:
        user1, user2 = users[0], users[1]
    else:
        user1, user2 = users[1], users[0]
    subscribe = Friends.objects.filter(user1=user1, user2=user2)
    if subscribe.exists():
        subscribe.delete()
    else:
        subscribe = Friends.objects.create(user1=user1, user2=user2)
        subscribe.save()