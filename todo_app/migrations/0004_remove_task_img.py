# Generated by Django 3.2.4 on 2021-06-13 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_task_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='img',
        ),
    ]
