# Generated by Django 2.2.5 on 2020-10-31 12:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitaldetails', '0010_hospitalbooking_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalentry',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hospitaltype',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
