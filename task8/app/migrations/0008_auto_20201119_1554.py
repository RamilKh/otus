# Generated by Django 3.1.3 on 2020-11-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20201118_0633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'User'), (5, 'Admin'), (9, 'Developer')], default=1),
        ),
    ]
