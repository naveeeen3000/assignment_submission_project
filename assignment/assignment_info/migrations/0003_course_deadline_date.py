# Generated by Django 3.1.2 on 2020-11-09 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_info', '0002_remove_course_deadline_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='deadline_date',
            field=models.DateField(null=True),
        ),
    ]
