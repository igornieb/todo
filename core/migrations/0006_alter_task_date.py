# Generated by Django 4.1.2 on 2023-01-12 09:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_account_profile_picture_alter_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 12, 10, 49, 21, 904607)),
        ),
    ]
