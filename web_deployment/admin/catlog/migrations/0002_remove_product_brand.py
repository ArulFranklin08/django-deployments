# Generated by Django 2.2.5 on 2020-10-31 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
    ]