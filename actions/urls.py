from django.urls import path
from .models import *
from .views import  *
urlpatterns = [
    path('channel_create/',channel_create_view,name ='channel_create'),
    path('channel_list/',channel_list_view,name ='channel_list'),
    path('channel_update/<int:pk>',channel_update_view,name ='channel_update'),
    path('channel_delete/<int:pk>',channel_delete_view,name ='channel_delete'),
    path('channel_detail/<int:pk>',channel_detail_view,name ='channel_detail'),
    path('post_create/<int:pk>',post_create_view,name ='post_create'),
    path('video_create/<int:pk>',video_create_view,name ='video_create'),
]



