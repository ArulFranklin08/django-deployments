# Generated by Django 2.2.5 on 2020-10-28 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorprofile', '0006_listofdoctorbooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorentry',
            name='clinic_image_url',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='doctorentry',
            name='doctor_image_url',
            field=models.CharField(max_length=20, null=True),
        ),
    ]