# Generated by Django 2.2.5 on 2020-11-11 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0009_auto_20201109_1854'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Errorpage',
            new_name='Error_page',
        ),
        migrations.RenameModel(
            old_name='Otherpage',
            new_name='Other_page',
        ),
        migrations.RenameModel(
            old_name='Totalpage',
            new_name='Total_page',
        ),
        migrations.RenameModel(
            old_name='Trendingpage',
            new_name='Trending_page',
        ),
    ]
