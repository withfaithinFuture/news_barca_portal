from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history, name='history'),
    path('squad/', views.squad, name='squad'),
    path('profile/', views.profile, name='profile'),
    path('auth/', views.auth_view, name='auth'),
    path('register/', views.register_view, name='register'),
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),

]
