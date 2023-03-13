from django.urls import re_path
from .views import get_delete_update_puppy, get_post_puppy

urlpatterns = [
    re_path(r'^api/v1/puppies/(?P<pk>[0-9]+)$', get_delete_update_puppy, name='get_delete_update_puppy'),
    re_path(r'^api/v1/puppies/$', get_post_puppy, name='get_post_puppy'),
]
