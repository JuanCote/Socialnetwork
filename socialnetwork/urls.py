from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views.auth import index, sign_in, sign_up
from .views.home_page import home_page, create_post, logout
from .views.profile import profile, update_profile, update_ava
from .views.friends import friends_all, subscribe, friends_subscriptions, friends_subscribers

urlpatterns = [
    path('', index, name='index'),
    path('sign_in', sign_in, name='sign_in'),
    path('sign_up', sign_up, name='sign_up'),
    path('homepage', home_page, name='home_page'),
    path('create_post', create_post, name='create_post'),
    path('logout', logout, name='logout'),
    path('friends_all', friends_all, name='friends_all'),
    path('friends_subscriptions', friends_subscriptions, name='friends_subscriptions'),
    path('friends_subscribers', friends_subscribers, name='friends_subscribers'),
    path('subscribe', subscribe, name='subscribe'),
    path('profile', profile, name='profile'),
    path('update_profile', update_profile, name='update_profile'),
    path('update_ava', update_ava, name='update_ava')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
