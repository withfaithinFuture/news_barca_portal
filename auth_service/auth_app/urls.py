from django.urls import path
from .views import register_view
from .views import auth_view
from django.contrib import admin
from .views import logout_view

urlpatterns = [
    path('auth/', auth_view, name='auth'),
    path('register/', register_view, name='register'),
    path('admin/', admin.site.urls),
    path('logout/', logout_view, name='logout'),
]