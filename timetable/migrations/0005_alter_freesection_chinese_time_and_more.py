# Generated by Django 4.2.3 on 2023-07-22 09:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("timetable", "0004_alter_section_chinese_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="freesection",
            name="chinese_time",
            field=models.CharField(
                choices=[
                    ("4:30 - 5:15", "4:30 - 5:15"),
                    ("5:30 - 6:15", "5:30 - 6:15"),
                    ("6:30 - 7:15", "6:30 - 7:15"),
                    ("7:30 - 8:15", "7:30 - 8:15"),
                    ("8:30 - 9:15", "8:30 - 9:15"),
                    ("9:30 - 10:15", "9:30 - 10:15"),
                    ("10:30 - 11:15", "10:30 - 11:15"),
                    ("11:30 - 12:15", "11:30 - 12:15"),
                    ("12:30 - 13:15", "12:30 - 13:15"),
                    ("13:30 - 14:15", "13:30 - 14:15"),
                    ("14:30 - 15:15", "14:30 - 15:15"),
                    ("15:30 - 16:15", "15:30 - 16:15"),
                    ("16:30 - 17:15", "16:30 - 17:15"),
                ],
                default="4:30 - 5:15",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="section",
            name="chinese_time",
            field=models.CharField(
                choices=[
                    ("4:30 - 5:15", "4:30 - 5:15"),
                    ("5:30 - 6:15", "5:30 - 6:15"),
                    ("6:30 - 7:15", "6:30 - 7:15"),
                    ("7:30 - 8:15", "7:30 - 8:15"),
                    ("8:30 - 9:15", "8:30 - 9:15"),
                    ("9:30 - 10:15", "9:30 - 10:15"),
                    ("10:30 - 11:15", "10:30 - 11:15"),
                    ("11:30 - 12:15", "11:30 - 12:15"),
                    ("12:30 - 13:15", "12:30 - 13:15"),
                    ("13:30 - 14:15", "13:30 - 14:15"),
                    ("14:30 - 15:15", "14:30 - 15:15"),
                    ("15:30 - 16:15", "15:30 - 16:15"),
                    ("16:30 - 17:15", "16:30 - 17:15"),
                ],
                default="4:30 - 5:15",
                max_length=50,
            ),
        ),
    ]
