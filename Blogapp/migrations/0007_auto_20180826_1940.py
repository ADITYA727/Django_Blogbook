# Generated by Django 2.1 on 2018-08-26 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blogapp', '0006_auto_20180826_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userprofile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
