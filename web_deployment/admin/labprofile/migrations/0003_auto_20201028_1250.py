# Generated by Django 2.2.5 on 2020-10-28 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labprofile', '0002_auto_20201027_1348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listofdoctor',
            old_name='image',
            new_name='doc_image',
        ),
        migrations.AddField(
            model_name='labentry',
            name='lab_alt_image',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='labentry',
            name='lab_alt_tag',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='labentry',
            name='video_alt_tag',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='labentry',
            name='video_url',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='listofdoctor',
            name='image_alt_tag',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='listofdoctor',
            name='video_alt_tag',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='listofdoctor',
            name='video_url',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='listofpackage',
            name='image_alt_tag',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='listofpackage',
            name='image_url',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='listofpackage',
            name='video_alt_tag',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='listofpackage',
            name='video_url',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
