# Generated by Django 4.2.3 on 2023-07-07 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('metak', '0002_alter_metakinhsh_egkrish_alter_metakinhsh_pragmat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='metakinhsh',
            options={'verbose_name': 'Μετακίνηση', 'verbose_name_plural': 'Μετακινήσεις'},
        ),
        migrations.AlterField(
            model_name='metakinhsh',
            name='egkrish',
            field=models.BooleanField(default=False, verbose_name='Έγκριση'),
        ),
        migrations.AlterField(
            model_name='metakinhsh',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Χρήστης'),
        ),
        migrations.AlterField(
            model_name='metakinhsh',
            name='pragmat',
            field=models.BooleanField(default=False, verbose_name='Πραγματοποιήθηκε'),
        ),
    ]
