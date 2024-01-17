from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import index, sign_in, sign_up, home_page, logout, friends_all, subscribe, friends_subscriptions, friends_subscribers, profile

urlpatterns = [
    path('', index, name='index'),
    path('sign_in', sign_in, name='sign_in'),
    path('sign_up', sign_up, name='sign_up'),
    path('homepage', home_page, name='home_page'),
    path('logout', logout, name='logout'),
    path('friends_all', friends_all, name='friends_all'),
    path('friends_subscriptions', friends_subscriptions, name='friends_subscriptions'),
    path('friends_subscribers', friends_subscribers, name='friends_subscribers'),
    path('subscribe', subscribe, name='subscribe'),
    path('profile', profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
