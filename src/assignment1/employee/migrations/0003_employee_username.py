# Generated by Django 3.1.2 on 2020-10-25 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20201025_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
    ]
