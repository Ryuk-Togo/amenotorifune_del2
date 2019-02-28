from django.db import models

# Create your models here.
class T_Todo(models.Model):
    # todo_id = AutoField(primary_key=True)  # 自動的に追加されるので定義不要
    title = models.CharField(max_length=30)
    discription = models.CharField(max_length=200)
    should_action = models.IntegerField()
    where_dont_action = models.IntegerField()
    single_action = models.IntegerField()
    can_do_tow_minite = models.IntegerField()
    should_myself = models.IntegerField()
    should_do_than_2min = models.IntegerField()
    user_id = models.CharField(max_length=6)
    category = models.CharField(max_length=6)
    create_date = models.TimeField()
    create_pg_id = models.CharField(max_length=30)
    create_user_id = models.CharField(max_length=6)
    update_date = models.TimeField()
    update_pg_id = models.CharField(max_length=30)
    update_user_id = models.CharField(max_length=6)
    
class M_User(models.Model):
    user_id = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    create_date = models.TimeField()
    create_pg_id = models.CharField(max_length=30)
    create_user_id = models.CharField(max_length=6)
    update_date = models.TimeField()
    update_pg_id = models.CharField(max_length=30)
    update_user_id = models.CharField(max_length=6)
    
class T_Task(models.Model):
    # task_id = models.CharField(max_length=30)
    user_id = models.CharField(max_length=30)
    todo_id = models.CharField(max_length=30)
    task_date_time = models.DateTimeField()
    task_discription = models.TextField()
    create_date = models.TimeField()
    create_pg_id = models.CharField(max_length=30)
    create_user_id = models.CharField(max_length=6)
    update_date = models.TimeField()
    update_pg_id = models.CharField(max_length=30)
    update_user_id = models.CharField(max_length=6)

class T_Remaind(models.Model):
    # task_id = models.CharField(max_length=30)
    user_id = models.CharField(max_length=30)
    task_id = models.CharField(max_length=30)
    task_date_time = models.DateTimeField()
    message = models.TextField()
    create_date = models.TimeField()
    create_pg_id = models.CharField(max_length=30)
    create_user_id = models.CharField(max_length=6)
    update_date = models.TimeField()
    update_pg_id = models.CharField(max_length=30)
    update_user_id = models.CharField(max_length=6)
