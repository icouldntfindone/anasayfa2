# Generated by Django 3.2.9 on 2024-04-11 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_forum_thread'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default='2024-04-11 12:43'),
            preserve_default=False,
        ),
    ]
