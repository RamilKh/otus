# Generated by Django 3.1.3 on 2020-11-13 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201112_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.SmallIntegerField(choices=[(1, 'User'), (5, 'Admin'), (9, 'Developer')], default=9),
        ),
    ]