# Generated by Django 2.2.5 on 2020-10-27 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorprofile', '0003_auto_20201026_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorentry',
            name='sno',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='listofdoctor',
            name='sno',
            field=models.IntegerField(null=True),
        ),
    ]
