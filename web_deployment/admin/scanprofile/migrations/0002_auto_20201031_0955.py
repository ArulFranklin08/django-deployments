# Generated by Django 2.2.5 on 2020-10-31 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scanbooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('doctor_name', models.CharField(max_length=100, null=True)),
                ('consulation', models.CharField(max_length=100, null=True)),
                ('scan', models.CharField(max_length=100, null=True)),
                ('profile_for', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Transgender', 'Transgender')], max_length=10)),
                ('email', models.CharField(max_length=20, null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('payment', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scanpackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField(null=True)),
                ('scan_package_name', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.AddField(
            model_name='scanentry',
            name='company_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='scanentry',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='scanentry',
            name='image_alt_tag',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
