# Generated by Django 3.1.3 on 2023-08-09 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='chocies',
            new_name='choices',
        ),
        migrations.RemoveField(
            model_name='question',
            name='course',
        ),
    ]