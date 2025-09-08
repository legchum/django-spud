from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('newnote/', views.newnote, name="newnote"),
    path('cool_picture/', views.cool_picture, name="cool_picture"),
    path('delete/<int:note_id>/', views.delete_note, name="delete_note"),
]
