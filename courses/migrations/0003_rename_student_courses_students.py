# Generated by Django 4.0.4 on 2022-05-15 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_courses_instructor_courses_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='student',
            new_name='students',
        ),
    ]
