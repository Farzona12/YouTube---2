from django.db import models
from accounts.models import CustomUser

class Channel(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='channels')
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    subscribers = models.ManyToManyField(CustomUser, related_name='subscriptions',blank=True)


class Post(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    views_count = models.IntegerField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)


class Video(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField( null=True, blank=True)
    video_file = models.FileField()
    created_at = models.DateField(auto_now=True)
    views_count = models.IntegerField(null=True, blank=True)
    is_public = models.BooleanField()



class Comments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateField(auto_now=True)



class Likes_Dislikes(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,null=True, blank=True )
    TYPES = (
        ('like', 'like'),
        ('dislike', 'dislike')
    )
    type =  models.CharField(max_length=8, choices=TYPES)
