# Generated by Django 2.2.5 on 2020-11-09 07:22

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_auto_20201108_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherpage',
            name='Page_maintained_by',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trendingpage',
            name='Page_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='trendingpage',
            name='Page_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trendingpage',
            name='Page_url',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='trendingpage',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='otherpage',
            name='Description',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
