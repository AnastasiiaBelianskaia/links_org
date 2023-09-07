# Generated by Django 4.2.3 on 2023-09-06 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_definition', models.CharField(max_length=200)),
                ('url_link', models.CharField(max_length=250)),
                ('important', models.BooleanField(choices=[(True, 'Important'), (False, 'Average')], verbose_name='Important or Average')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='linksorg.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
