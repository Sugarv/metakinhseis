# Generated by Django 4.2.3 on 2023-07-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metak', '0006_alter_metakinhsh_handler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metakinhsh',
            name='date_to',
            field=models.DateField(null=True, verbose_name='Ημ/νία Έως'),
        ),
    ]
