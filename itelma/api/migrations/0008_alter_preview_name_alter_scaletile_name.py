# Generated by Django 5.1.3 on 2024-11-23 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_preview_name_scaletile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preview',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scaletile',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
