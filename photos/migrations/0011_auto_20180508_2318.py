# Generated by Django 2.0.4 on 2018-05-08 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0010_auto_20180508_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='capture_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
