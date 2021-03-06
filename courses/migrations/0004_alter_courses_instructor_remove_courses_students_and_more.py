# Generated by Django 4.0.4 on 2022-05-16 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_rename_student_courses_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='instructor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='courses',
            name='students',
        ),
        migrations.AddField(
            model_name='courses',
            name='students',
            field=models.ManyToManyField(null=True, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
    ]
