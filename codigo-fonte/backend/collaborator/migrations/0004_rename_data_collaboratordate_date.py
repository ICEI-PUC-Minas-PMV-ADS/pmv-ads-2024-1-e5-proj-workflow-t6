# Generated by Django 3.2.25 on 2024-06-03 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collaborator', '0003_collaboratordate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collaboratordate',
            old_name='data',
            new_name='date',
        ),
    ]
