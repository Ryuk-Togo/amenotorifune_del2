# Generated by Django 2.1.2 on 2019-11-07 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('susanowo', '0010_auto_20191106_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ttodo',
            name='discription',
            field=models.TextField(help_text='タスクの詳細な内容を入力して下さい', verbose_name='タスクの詳細'),
        ),
    ]
