# Generated by Django 2.2.5 on 2020-11-11 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctorprofile', '0009_auto_20201102_0938'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Doctorentry',
            new_name='Doctor_entry',
        ),
        migrations.RenameModel(
            old_name='Listofdoctor',
            new_name='List_of_doctor',
        ),
        migrations.RenameModel(
            old_name='Listofdoctorbooking',
            new_name='List_of_doctor_booking',
        ),
    ]
