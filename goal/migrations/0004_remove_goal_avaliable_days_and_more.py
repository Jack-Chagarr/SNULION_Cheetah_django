# Generated by Django 4.2.3 on 2023-07-18 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goal', '0003_goal_prev_cumulative_time_goal_prev_progress_rate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='avaliable_days',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='exception_list',
        ),
    ]
