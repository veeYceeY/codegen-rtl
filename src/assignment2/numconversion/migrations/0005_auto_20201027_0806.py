# Generated by Django 3.1.2 on 2020-10-27 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('numconversion', '0004_converted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='converted',
            name='audio',
            field=models.FileField(max_length=10000, upload_to=None),
        ),
    ]
