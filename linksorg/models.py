# from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
# from django.utils import timezone

User = get_user_model()


class Link(models.Model):
    BOOL = (
        (True, 'Important'),
        (False, 'Average')
    )
    short_definition = models.CharField(max_length=200)
    url_link = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    important = models.BooleanField(choices=BOOL, verbose_name='Important or Average')
    date_time = models.DateTimeField('date added', auto_now_add=True)

    def __str__(self):
        return self.url_link
