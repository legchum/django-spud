from django.db import models

# Create your models here.
class Note(models.Model):
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
