# Generated by Django 2.1.2 on 2019-11-07 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('susanowo', '0011_auto_20191107_0632'),
    ]

    operations = [
        migrations.AddField(
            model_name='ttodo',
            name='request_pertner',
            field=models.CharField(blank=True, help_text='自分で行わない場合、依頼した人を入力して下さい。', max_length=200, verbose_name='依頼した人'),
        ),
    ]