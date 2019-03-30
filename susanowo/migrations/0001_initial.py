# Generated by Django 2.1.2 on 2019-03-19 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('create_date', models.TimeField()),
                ('create_pg_id', models.CharField(max_length=30)),
                ('create_user_id', models.CharField(max_length=6)),
                ('update_date', models.TimeField()),
                ('update_pg_id', models.CharField(max_length=30)),
                ('update_user_id', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='TRemaind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('task_id', models.CharField(max_length=30)),
                ('task_date_time', models.DateTimeField()),
                ('message', models.TextField()),
                ('create_date', models.TimeField()),
                ('create_pg_id', models.CharField(max_length=30)),
                ('create_user_id', models.CharField(max_length=6)),
                ('update_date', models.TimeField()),
                ('update_pg_id', models.CharField(max_length=30)),
                ('update_user_id', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='TTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('todo_id', models.CharField(max_length=30)),
                ('task_date_time', models.DateTimeField()),
                ('task_discription', models.TextField()),
                ('create_date', models.TimeField()),
                ('create_pg_id', models.CharField(max_length=30)),
                ('create_user_id', models.CharField(max_length=6)),
                ('update_date', models.TimeField()),
                ('update_pg_id', models.CharField(max_length=30)),
                ('update_user_id', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='TTodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('discription', models.CharField(max_length=200)),
                ('should_action', models.IntegerField()),
                ('where_dont_action', models.IntegerField()),
                ('single_action', models.IntegerField()),
                ('can_do_tow_minite', models.IntegerField()),
                ('should_myself', models.IntegerField()),
                ('should_do_than_2min', models.IntegerField()),
                ('user_id', models.CharField(max_length=6)),
                ('category', models.CharField(max_length=6)),
                ('create_date', models.TimeField()),
                ('create_pg_id', models.CharField(max_length=30)),
                ('create_user_id', models.CharField(max_length=6)),
                ('update_date', models.TimeField()),
                ('update_pg_id', models.CharField(max_length=30)),
                ('update_user_id', models.CharField(max_length=6)),
            ],
        ),
    ]
