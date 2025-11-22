from django.contrib import admin
from .models import *



admin.site.register(Channel)
admin.site.register(Post)
admin.site.register(Video)
admin.site.register(Comments)
admin.site.register(Likes_Dislikes)