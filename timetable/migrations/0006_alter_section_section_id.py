# Generated by Django 3.2.18 on 2023-06-21 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0005_auto_20230618_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='section_id',
            field=models.CharField(max_length=25, primary_key=True, serialize=False, unique=True),
        ),
    ]