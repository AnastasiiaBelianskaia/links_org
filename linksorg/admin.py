from django.contrib import admin

from .models import Link


class LinkAdmin(admin.ModelAdmin):
    list_display = ['important', 'url_link', 'category']


admin.site.register(Link, LinkAdmin)
