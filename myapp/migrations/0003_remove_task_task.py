# Generated by Django 4.1.7 on 2023-04-04 02:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_task"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="task",
        ),
    ]
