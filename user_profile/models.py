from django.db import models
from accounts.models import CustomUser


class User_profile(models.Model):
    image = models.ImageField()    
    bio = models.TextField()
    age = models.IntegerField()
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)



