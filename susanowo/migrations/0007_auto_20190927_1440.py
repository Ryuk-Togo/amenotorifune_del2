# Generated by Django 2.1.2 on 2019-09-27 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('susanowo', '0006_auto_20190927_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='ttodo',
            name='category',
            field=models.CharField(blank=True, max_length=2, verbose_name='カテゴリー'),
        ),
        migrations.AlterField(
            model_name='ttodo',
            name='can_do_tow_minite',
            field=models.BooleanField(blank=True, verbose_name='２分以上かかりそう？'),
        ),
    ]