# Generated by Django 4.2.7 on 2024-02-26 18:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todos", "0002_alter_todo_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
