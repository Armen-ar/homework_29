# Generated by Django 4.1.1 on 2022-10-02 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_user_location_user_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='location',
            new_name='location_id',
        ),
    ]
