from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from ..forms import ProfileForm, EditAvaForm
from ..models import Friends, Profile


@login_required(login_url="index")
def profile(request):
    user = request.user
    initial_data = {
            "sex": user.profile.sex,
            "interested_in": user.profile.interested_in,
            "relationship_status": user.profile.relationship_status,
            "looking_for": user.profile.looking_for,
            "birthday": user.profile.birthday,
            "hometown": user.profile.hometown,
            "about_me": user.profile.about_me,
        }
    subscribers_subscriptions = Friends.objects.filter(
        Q(user1=request.user.id) | Q(user2=request.user.id)
    )
    subscribers, subscriptions = 0, 0
    for record in subscribers_subscriptions:
        if record.user1.id == user.id:
            subscriptions += 1
        else:
            subscribers += 1
    profile = user.profile.__dict__
    for elem in profile:
        if not profile[elem]:
            profile[elem] = '-'
    data = {
        'user': user,
        "profile": profile,
        "subscribers": subscribers,
        "subscriptions": subscriptions,
        "form": ProfileForm(initial=initial_data),
        "form_ava": EditAvaForm(),
    }
    return render(request, "profile/profile.html", context=data)
    

@login_required(login_url="index")
def update_profile(request):
    user = request.user
    form = ProfileForm(request.POST, instance=user.profile)
    if form.is_valid():
        form.save()
        return redirect("profile")
    

@login_required(login_url='index')
def update_ava(request):
    user = request.user
    form = EditAvaForm(request.POST, request.FILES, instance=user.profile)
    if form.is_valid():
        form.save()
        return redirect("profile")