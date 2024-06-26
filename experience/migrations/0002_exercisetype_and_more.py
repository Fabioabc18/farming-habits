# Generated by Django 5.0.3 on 2024-03-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_type', models.CharField(max_length=100)),
                ('exercise_difficulty', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.RenameField(
            model_name='dailygoals',
            old_name='exercise_goal',
            new_name='exercise_time_goal',
        ),
    ]
