# Generated by Django 5.0.3 on 2024-03-25 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0002_waterconsumption_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waterconsumption',
            name='points',
        ),
    ]
