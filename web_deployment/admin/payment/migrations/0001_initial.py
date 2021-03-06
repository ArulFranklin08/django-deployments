# Generated by Django 2.2.5 on 2020-10-31 04:25

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('cus_no', models.IntegerField(null=True)),
                ('cus_id', models.IntegerField(null=True)),
                ('trans_id', models.IntegerField(null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('email', models.CharField(max_length=100)),
                ('total_amount', models.IntegerField(null=True)),
            ],
        ),
    ]
