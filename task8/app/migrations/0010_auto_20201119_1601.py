# Generated by Django 3.1.3 on 2020-11-19 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='photo',
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(null=True, upload_to='photo'),
        ),
    ]
