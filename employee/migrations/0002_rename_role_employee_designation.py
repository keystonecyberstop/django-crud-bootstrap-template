# Generated by Django 4.2.5 on 2023-10-03 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='role',
            new_name='designation',
        ),
    ]
