from django.urls import re_path
from .consumers import LikeConsumer

websocket_urlpatterns = [
    re_path(r'ws/likes/(?P<content_type>\w+)/(?P<content_id>\d+)/$', LikeConsumer.as_asgi()),
]
