"""Defines the URL pattern for users"""

from django.urls import path
from django.contrib.auth.views import LoginView  # Import LoginView instead of login
from . import views

app_name = 'users'

urlpatterns = [
    # Login page
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
]
