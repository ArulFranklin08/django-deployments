# Generated by Django 2.2.5 on 2020-11-11 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0006_addclinic_clinic_url'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Addclinic',
            new_name='Add_clinic',
        ),
        migrations.RenameModel(
            old_name='Clinicbooking',
            new_name='Clinic_booking',
        ),
    ]