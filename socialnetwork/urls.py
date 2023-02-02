from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import index, home_page, logout, friends

urlpatterns = [
    path('', index, name='index'),
    path('homepage', home_page, name='home_page'),
    path('logout', logout, name='logout'),
    path('friends', friends, name='friends')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
