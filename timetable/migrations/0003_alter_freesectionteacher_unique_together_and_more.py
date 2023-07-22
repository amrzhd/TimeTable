# Generated by Django 4.2.3 on 2023-07-22 07:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("timetable", "0002_alter_freesectionteacher_unique_together_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="freesectionteacher",
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name="sectionteacher",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="freesection",
            name="chinese_time",
            field=models.CharField(
                choices=[
                    ("9:00 - 9:45", "9:00 - 9:45"),
                    ("10:00 - 10:45", "10:00 - 10:45"),
                    ("11:00 - 11:45", "11:00 - 11:45"),
                    ("12:00 - 12:45", "12:00 - 12:45"),
                    ("13:00 - 13:45", "13:00 - 13:45"),
                    ("14:00 - 14:45", "14:00 - 14:45"),
                    ("15:00 - 15:45", "15:00 - 15:45"),
                    ("16:00 - 16:45", "16:00 - 16:45"),
                    ("17:00 - 17:45", "17:00 - 17:45"),
                    ("18:00 - 18:45", "18:00 - 18:45"),
                    ("19:00 - 19:45", "19:00 - 19:45"),
                    ("20:00 - 20:45", "20:00 - 20:45"),
                    ("21:00 - 21:45", "21:00 - 21:45"),
                ],
                default="4:30 - 5:15",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="freesectionteacher",
            name="student",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="section",
            name="chinese_time",
            field=models.CharField(
                choices=[
                    ("9:00 - 9:45", "9:00 - 9:45"),
                    ("10:00 - 10:45", "10:00 - 10:45"),
                    ("11:00 - 11:45", "11:00 - 11:45"),
                    ("12:00 - 12:45", "12:00 - 12:45"),
                    ("13:00 - 13:45", "13:00 - 13:45"),
                    ("14:00 - 14:45", "14:00 - 14:45"),
                    ("15:00 - 15:45", "15:00 - 15:45"),
                    ("16:00 - 16:45", "16:00 - 16:45"),
                    ("17:00 - 17:45", "17:00 - 17:45"),
                    ("18:00 - 18:45", "18:00 - 18:45"),
                    ("19:00 - 19:45", "19:00 - 19:45"),
                    ("20:00 - 20:45", "20:00 - 20:45"),
                    ("21:00 - 21:45", "21:00 - 21:45"),
                ],
                default="4:30 - 5:15",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="sectionteacher",
            name="student",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
