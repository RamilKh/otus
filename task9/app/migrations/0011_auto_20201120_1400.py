# Generated by Django 3.1.3 on 2020-11-20 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20201119_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.profile'),
        ),
    ]