# Generated by Django 3.1.2 on 2020-10-24 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(upload_to='empimages')),
                ('Email', models.CharField(default='', max_length=100)),
                ('Password', models.CharField(default='', max_length=100)),
                ('Phone', models.CharField(default='', max_length=100)),
                ('Address', models.CharField(default='', max_length=100)),
                ('dob', models.CharField(default='', max_length=100)),
                ('doj', models.CharField(default='', max_length=100)),
                ('designation', models.CharField(default='', max_length=100)),
                ('salary', models.CharField(default='', max_length=100)),
            ],
        ),
    ]