# Generated by Django 4.0.4 on 2022-05-17 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_rename_uuid_courses_id_alter_courses_students'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='id',
            new_name='uuid',
        ),
    ]
