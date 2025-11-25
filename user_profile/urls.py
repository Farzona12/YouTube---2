from django.urls import path
from .models import *
from .views import *

urlpatterns = [
    path('create/', profile_create_view, name = 'profile_create'),
    path('update/<int:pk>', profile_update_view, name = 'profile_update'),
    path('delete/<int:pk>', profile_delete_view, name = 'profile_delete'),
    path('profile_list', profile_list_view, name = 'profile_list'),
]