# Generated by Django 4.2.3 on 2023-07-22 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("timetable", "0010_class_platform"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sectionteacher",
            name="section",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="timetable.section",
            ),
        ),
    ]
