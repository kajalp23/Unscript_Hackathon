# Generated by Django 3.1.1 on 2020-11-21 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mercuri', '0003_delete_hospitaladmin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospitaldata',
            old_name='avilableOxygenCylinders',
            new_name='availableOxygenCylinders',
        ),
    ]