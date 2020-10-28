# Generated by Django 3.1.2 on 2020-10-27 08:29

import audiofield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('numconversion', '0005_auto_20201027_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='converted',
            name='audio',
            field=audiofield.fields.AudioField(blank=True, help_text='Allowed type - .mp3, .wav, .ogg', upload_to='your/upload/dir'),
        ),
    ]