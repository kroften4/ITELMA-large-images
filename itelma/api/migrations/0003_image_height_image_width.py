# Generated by Django 5.1.3 on 2024-11-23 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_last_called_image_last_opened'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='image',
            name='width',
            field=models.IntegerField(default=0),
        ),
    ]