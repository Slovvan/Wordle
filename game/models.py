from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=6, unique=True)
    is_daily = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
