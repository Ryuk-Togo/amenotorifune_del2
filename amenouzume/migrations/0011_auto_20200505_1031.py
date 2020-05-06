# Generated by Django 2.1.2 on 2020-05-05 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amenouzume', '0010_auto_20200502_0015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tstock',
            old_name='dwonload_date',
            new_name='download_date',
        ),
        migrations.AlterField(
            model_name='tstock',
            name='item_id',
            field=models.IntegerField(verbose_name='品目ID'),
        ),
        migrations.AlterField(
            model_name='tstock',
            name='place_id',
            field=models.IntegerField(verbose_name='場所'),
        ),
    ]
