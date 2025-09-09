from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('register', views.register, name='register'),
    path("login", views.login, name="login"),
    path("logout", views.user_logout, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("create_record", views.create_record, name="create_record"),
    path("update_record/<int:pk>", views.update_record, name="update_record")
]
