# Generated by Django 5.0.7 on 2024-07-30 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Account',
        ),
    ]
