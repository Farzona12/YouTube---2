from django.db import models
from accounts.models import CustomUser

class Channel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)



class Post(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    video = models.FileField(null=True, blank=True)
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
