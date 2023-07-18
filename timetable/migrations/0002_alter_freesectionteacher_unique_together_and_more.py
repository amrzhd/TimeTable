# Generated by Django 4.2.3 on 2023-07-18 12:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("timetable", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="freesectionteacher",
            unique_together={("teacher", "free_section")},
        ),
        migrations.AlterUniqueTogether(
            name="sectionteacher",
            unique_together={("teacher", "section")},
        ),
    ]
