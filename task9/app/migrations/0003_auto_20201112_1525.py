# Generated by Django 3.1.3 on 2020-11-12 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='level',
            new_name='status',
        ),
    ]
