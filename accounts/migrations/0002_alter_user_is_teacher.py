# Generated by Django 4.2.3 on 2023-07-17 14:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_teacher",
            field=models.BooleanField(default=False),
        ),
    ]