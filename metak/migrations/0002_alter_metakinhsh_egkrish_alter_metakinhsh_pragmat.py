# Generated by Django 4.0.3 on 2023-05-09 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metak', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metakinhsh',
            name='egkrish',
            field=models.BooleanField(null=True, verbose_name='Έγκριση'),
        ),
        migrations.AlterField(
            model_name='metakinhsh',
            name='pragmat',
            field=models.BooleanField(null=True, verbose_name='Πραγματοποιήθηκε'),
        ),
    ]
