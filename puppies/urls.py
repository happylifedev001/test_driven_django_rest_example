from django.conf.urls import url
from .views import get_delete_update_puppy, get_post_puppy

urlpatterns = [
    url(r'^api/v1/puppies/(?P<pk>[0-9]+)$', get_delete_update_puppy, name='get_delete_update_puppy'),
    url(r'^api/v1/puppies/$', get_post_puppy, name='get_post_puppy'),
]
