# Generated by Django 4.0.4 on 2022-05-17 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '__first__'),
        ('accounts', '0004_rename_uuid_myuser_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='address.address'),
        ),
    ]
