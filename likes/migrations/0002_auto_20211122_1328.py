# Generated by Django 3.2.7 on 2021-11-22 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postlikes',
            name='users_like',
        ),
        migrations.AddField(
            model_name='postlikes',
            name='users_like',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users_like', to='accounts.user'),
            preserve_default=False,
        ),
    ]
