# Generated by Django 2.1.2 on 2019-10-11 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('susanowo', '0008_auto_20191011_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='ttodo',
            name='deleted',
            field=models.BooleanField(blank=True, default=False, verbose_name='削除'),
        ),
    ]
