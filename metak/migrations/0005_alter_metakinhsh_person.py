# Generated by Django 4.2.3 on 2023-07-11 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('metak', '0004_metakinhsh_handler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metakinhsh',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Χρήστης'),
        ),
    ]
