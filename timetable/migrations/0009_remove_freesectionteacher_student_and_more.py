# Generated by Django 4.2.3 on 2023-07-22 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("timetable", "0008_class"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="freesectionteacher",
            name="student",
        ),
        migrations.AddField(
            model_name="freesectionteacher",
            name="free_section_class",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="timetable.class",
            ),
        ),
    ]
