# Generated by Django 2.1.2 on 2020-02-10 02:15

from django.db import migrations, models
import omoikane.models


class Migration(migrations.Migration):

    dependencies = [
        ('omoikane', '0004_auto_20200207_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mmenu',
            name='icon',
            field=models.ImageField(blank=True, height_field='url_height', null=True, upload_to=omoikane.models.get_upload_dir, verbose_name='アイコン', width_field='url_width'),
        ),
    ]