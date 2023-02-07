from datetime import date

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    content = models.CharField(max_length=188)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to='images/')
    sex = models.CharField(max_length=10, blank=True)
    interested_in = models.CharField(max_length=30, blank=True)
    relationship_status = models.CharField(max_length=50, blank=True)
    looking_for = models.CharField(max_length=50, blank=True)
    birthday = models.DateField(default=date.today())
    hometown = models.CharField(max_length=50, blank=True)
    about_me = models.CharField(max_length=50, blank=True)


class Friends(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_content_type')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE)
