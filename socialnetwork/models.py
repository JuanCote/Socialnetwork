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


class Friends(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_content_type')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE)
