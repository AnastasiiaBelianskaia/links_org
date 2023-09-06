import django_filters
from .models import Link


class LinkFilter(django_filters.FilterSet):
    class Meta:
        model = Link
        fields = ['category', 'important']
