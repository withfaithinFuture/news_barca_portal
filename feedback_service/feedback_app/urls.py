from django.urls import path
from .views import feedback_view

urlpatterns = [
    path('feedback/', feedback_view, name='feedback'),
]
