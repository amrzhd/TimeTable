# Generated by Django 4.2.3 on 2023-07-18 12:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_user_is_teacher"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="teacher_id",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]