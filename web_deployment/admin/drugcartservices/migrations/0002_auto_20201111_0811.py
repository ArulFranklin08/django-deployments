# Generated by Django 2.2.5 on 2020-11-11 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drugcartservices', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cuppingtherapy',
            new_name='Cupping_therapy',
        ),
        migrations.RenameModel(
            old_name='Spasaloon',
            new_name='Fitness_centre',
        ),
        migrations.RenameModel(
            old_name='Fitnesscentre',
            new_name='Physio_therapy',
        ),
        migrations.RenameModel(
            old_name='Stemcelltheraphy',
            new_name='Spa_saloon',
        ),
        migrations.RenameModel(
            old_name='Physiotherapy',
            new_name='Stem_cell_theraphy',
        ),
    ]
