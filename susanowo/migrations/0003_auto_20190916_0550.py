# Generated by Django 2.1.2 on 2019-09-16 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('susanowo', '0002_ttodo_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ttodo',
            name='delivery_date',
            field=models.DateField(blank=True, verbose_name='期限'),
        ),
    ]
