# Generated by Django 2.2.5 on 2020-11-11 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scanprofile', '0004_auto_20201031_1808'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Scanbooking',
            new_name='Scan_booking',
        ),
        migrations.RenameModel(
            old_name='Scanentry',
            new_name='Scan_entry',
        ),
        migrations.RenameModel(
            old_name='Scanpackage',
            new_name='Scan_package',
        ),
    ]