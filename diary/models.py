from django.db import models
from django.utils import timezone
from django.utils.html import format_html


class Note(models.Model):
    datetime = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=1024, default='')
    text = models.TextField(default='', blank=True)

    def __str__(self):
        return 'Note {} {}'.format(self.datetime.strftime('%Y-%m-%d'), self.title)
