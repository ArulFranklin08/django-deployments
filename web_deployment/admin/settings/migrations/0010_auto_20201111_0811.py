# Generated by Django 2.2.5 on 2020-11-11 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0009_auto_20201102_0938'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Asidebanner',
            new_name='A_side_banner',
        ),
        migrations.RenameModel(
            old_name='Drugcartsservice',
            new_name='Drug_carts_service',
        ),
        migrations.RenameModel(
            old_name='Mainslider',
            new_name='Main_slider',
        ),
        migrations.RenameModel(
            old_name='Pickopportunity',
            new_name='Pick_opportunity',
        ),
        migrations.RenameModel(
            old_name='PostImage',
            new_name='Post_Image',
        ),
        migrations.RenameModel(
            old_name='Specialcare',
            new_name='Special_care',
        ),
    ]
