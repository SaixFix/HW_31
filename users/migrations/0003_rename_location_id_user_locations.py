# Generated by Django 4.1.5 on 2023-02-06 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='location_id',
            new_name='locations',
        ),
    ]