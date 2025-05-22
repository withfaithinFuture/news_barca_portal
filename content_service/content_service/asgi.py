"""
ASGI config for content_service project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# Установить переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'content_service.settings')
django.setup()

# Импорт роутинга WebSocket
from likes.routing import websocket_urlpatterns  # если likes — это поддиректория с routing.py

# Финальное ASGI-приложение
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})
