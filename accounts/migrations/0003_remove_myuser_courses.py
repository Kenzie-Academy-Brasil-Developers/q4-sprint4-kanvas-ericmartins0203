# Generated by Django 4.0.4 on 2022-05-15 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_myuser_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='courses',
        ),
    ]