# Generated by Django 2.1.2 on 2019-05-17 05:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('susanowo', '0016_auto_20190517_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='ttodo',
            name='create_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='登録日時'),
        ),
    ]