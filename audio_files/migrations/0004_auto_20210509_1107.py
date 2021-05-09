# Generated by Django 3.2.2 on 2021-05-09 05:37

import audio_files.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_files', '0003_auto_20210509_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='name',
            field=models.CharField(max_length=100, validators=[audio_files.models.name_validation]),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='name',
            field=models.CharField(max_length=100, validators=[audio_files.models.name_validation]),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='participants',
            field=models.CharField(max_length=1000, validators=[audio_files.models.participant_validation]),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=100, validators=[audio_files.models.name_validation]),
        ),
    ]
