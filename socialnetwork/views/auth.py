from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.shortcuts import render, redirect
from django.dispatch import receiver



from ..forms import Login, Register
from ..models import Profile


def index(request):
    if request.user.is_authenticated:
        return redirect("home_page")

    data = {
        "form_login": Login(), 
        "form_register": Register()
        }

    return render(request, "auth/index.html", context=data)


def sign_in(request):
    form_login = Login(request.POST)
    if form_login.is_valid():
        try:
            user_from_db = User.objects.get(email=form_login.cleaned_data["email"])
        except User.DoesNotExist:
            user_from_db = None
        if user_from_db:
            username = user_from_db.username
            user = authenticate(
                username=username, password=form_login.cleaned_data["password"]
            )
            if user:
                login(request, user)
                return redirect("home_page")
            else:
                form_login.add_error(None, "Invalid password")
        else:
            form_login.add_error(None, "Invalid email")
    data = {"form_login": form_login, "form_register": Register()}
    return render(request, "auth/index.html", context=data)


def sign_up(request):
    form_register = Register(request.POST)
    data = {'form_login': Login()}
    if form_register.is_valid():
        form_register.save()
        messages.success(request, "Success registration")
        data['messages'] = messages.get_messages(request)
    else:
        data['visible_popup'] = True
    data['form_register'] = form_register
    return render(request, "auth/index.html", context=data)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)