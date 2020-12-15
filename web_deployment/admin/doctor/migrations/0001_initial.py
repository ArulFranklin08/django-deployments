# Generated by Django 2.2.5 on 2020-12-11 12:16

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('doctor_name', models.CharField(max_length=100, null=True)),
                ('mobile_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('email', models.CharField(max_length=20, null=True)),
                ('speciality', models.CharField(max_length=20, null=True)),
                ('doctor_image', models.ImageField(blank=True, upload_to='images/')),
                ('doctor_image_url', models.CharField(max_length=20, null=True)),
                ('doctor_alt_image', models.CharField(max_length=20, null=True)),
                ('discount', models.IntegerField(null=True)),
                ('street_name', models.CharField(max_length=100, null=True)),
                ('distance', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]