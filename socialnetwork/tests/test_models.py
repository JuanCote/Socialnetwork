from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Profile, Post, Friends
from datetime import date


class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user2 = User.objects.create_user(username='testuser2', password='testpassword')
        self.user.profile.sex = 'Male'
        self.user.profile.birthday = date(1990, 1, 1)
        self.user.profile.save()
        

    def test_profile_model(self):
        user = User.objects.get(username='testuser')
        self.assertEqual(user.profile.sex, 'Male')
        self.assertEqual(user.profile.birthday, date(1990, 1, 1))


    def test_post_model(self):
        post = Post.objects.create(content='Test content', user=self.user)
        self.assertEqual(post.content, 'Test content')
        self.assertEqual(post.user, self.user)


    def test_post_with_image(self):
        post_with_image = Post.objects.create(content='Test content', user=self.user, image = 'images/test_image.jpg')
        self.assertEqual(post_with_image.image, 'images/test_image.jpg')


    def test_friends_model(self):
        friends = Friends.objects.create(user1=self.user, user2=self.user2)
        self.assertEqual(friends.user1, self.user)
        self.assertEqual(friends.user2, self.user2)


    def test_profile_default_avatar(self):
        default_avatar = self.user.profile.avatar
        self.assertEqual(default_avatar, 'images/circleuser.png')

