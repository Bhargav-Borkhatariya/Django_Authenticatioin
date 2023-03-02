from user_auth import views
from django.urls import path

urlpatterns = [
    path("", views.home, name='login'),
    path("signup", views.signup, name='signup'),
    path("dashboard", views.dashboard, name='dashboard'),
]
