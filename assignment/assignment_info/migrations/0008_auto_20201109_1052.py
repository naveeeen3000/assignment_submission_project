# Generated by Django 3.1.2 on 2020-11-09 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment_info', '0007_auto_20201109_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissions',
            name='answer',
            field=models.FileField(upload_to='assignments/<django.db.models.fields.related.ForeignKey>'),
        ),
    ]
