from django.db import models

class Note(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=1024, default='')
    text = models.TextField(default='', blank=True)
