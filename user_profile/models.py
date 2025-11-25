from django.db import models
from accounts.models import CustomUser


class User_profile(models.Model):
    image = models.ImageField()    
    bio = models.TextField(null=True, blank=True)
    age = models.IntegerField()
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    '''
    I will enter the subscribers field manually myself.
    This field will not be visible in the HTML.
    We will handle it during the save or update process in the backend.

    After clicking “+ subscriber”, we will manually add the subscriber both to the Subscribers table and to the Channel.
    '''
    subscribers= models.IntegerField(null=True, blank=True)
    video = models.IntegerField(null=True, blank=True)