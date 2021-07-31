# Generated by Django 3.2.5 on 2021-07-31 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('textsnippets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textsnippet',
            name='CreatedBy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Textsnippet', to='authentication.user', verbose_name='User'),
            preserve_default=False,
        ),
    ]
