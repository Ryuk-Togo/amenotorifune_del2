# Generated by Django 2.1.2 on 2020-04-28 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenouzume', '0003_tstockhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mplace',
            name='place_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='場所名'),
        ),
    ]
