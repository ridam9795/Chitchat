# Generated by Django 4.0 on 2023-10-31 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sketchboard', '0012_remove_contact_name_contact_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
