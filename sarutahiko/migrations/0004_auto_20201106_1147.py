# Generated by Django 2.1.2 on 2020-11-06 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarutahiko', '0003_auto_20201105_1025'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TKondateRecipe',
        ),
        migrations.RemoveField(
            model_name='tkondate',
            name='is_main',
        ),
        migrations.AddField(
            model_name='tkondate',
            name='is_sub',
            field=models.CharField(default='', max_length=100, verbose_name='主菜／副菜'),
            preserve_default=False,
        ),
    ]
