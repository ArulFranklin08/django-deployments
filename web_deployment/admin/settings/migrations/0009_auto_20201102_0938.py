# Generated by Django 2.2.5 on 2020-11-02 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0008_auto_20201031_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='image_alt_tag',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='drugcartsservice',
            name='image_alt_tag',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pickopportunity',
            name='image_alt_tag',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='specialcare',
            name='image_alt_tag',
            field=models.CharField(max_length=100, null=True),
        ),
    ]