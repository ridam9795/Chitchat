# Generated by Django 4.0 on 2023-10-21 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sketchboard', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
    ]
