from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

# from django.utils import timezone

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Link(models.Model):
    BOOL = (
        (True, 'Important'),
        (False, 'Average')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    short_definition = models.CharField(max_length=200)
    url_link = models.CharField(max_length=250, verbose_name='link')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='links')
    important = models.BooleanField(choices=BOOL, verbose_name='Important or Average')
    date_time = models.DateTimeField('date added', auto_now_add=True)

    def __str__(self):
        return self.url_link
