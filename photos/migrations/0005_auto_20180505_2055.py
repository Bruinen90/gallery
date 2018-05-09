# Generated by Django 2.0.4 on 2018-05-05 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20180505_2050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='image_height',
            new_name='height',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='image_width',
            new_name='width',
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(height_field='height', upload_to='', width_field='width'),
        ),
    ]
