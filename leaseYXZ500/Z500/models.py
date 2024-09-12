from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class Test(models.Model):
#     name = models.CharField(max_length=20)
#
#     class Meat:
#         app_label = "test"
#         manage = True

class Sys_param_config(models.Model):
    config_type = models.CharField(max_length=20)
    config_value = models.CharField(max_length=20)
    class Meta:
        managed = False
        # app_label = "ifc_uat"
        db_table = "sys_param_config"

class Auth_group(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        managed = False
        # app_label = "ifc_uat"
        db_table = "auth_group"

class Biz_flow_info(models.Model):
    task_id = models.CharField(max_length=20)
    business_key = models.CharField(max_length=20)
    assignee = models.CharField(max_length=20)
    task_name = models.CharField(max_length=20)
    class Meta:
        managed = False
        # app_label = "ifc_uat"
        db_table = "biz_flow_info"

class Auth_user_sync_record(models.Model):
    AUTH_USER_SYNC_ID = models.IntegerField(primary_key=True)
    USER_ID = models.CharField(max_length=20)
    UC_SYNC_ID = models.CharField(max_length=20)
    class Meta:
        managed = False
        # app_label = "xiaowei_uat"
        db_table = "auth_user_sync_record"


class Z500_test(models.Model):
    name = models.CharField(max_length=20)
    # count = models.IntegerField(max_length=20)
    projectNo = models.CharField(max_length=20)
    node = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    create_time = models.DateTimeField(max_length=6)
    env = models.CharField(max_length=20)

    class Meta:
        managed = False
        # app_label = "xiaowei_uat"
        db_table = "z500_test"



class Pay_main_info(models.Model):

    pay_info_no = models.CharField(max_length=20)
    pay_main_no = models.CharField(max_length=20)
    project_no = models.CharField(max_length=20)
    proj_trades_id = models.IntegerField(max_length=100)

    class Meta:
        managed = False
        db_table = "pay_main_info"


class Proj_main_info(models.Model):

    project_no = models.CharField(max_length=20)
    creator_id = models.CharField(max_length=20)


    class Meta:
        managed = False
        db_table = "proj_main_info"


class Proj_trades_supplier(models.Model):
    project_no = models.CharField(max_length=20)
    proj_trades_id = models.IntegerField(max_length=100)
    settle_mode = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "proj_trades_supplier"

class Credit_auth(models.Model):
    '''征信授权表'''
    credit_customer_no = models.CharField(max_length=20)
    credit_customer_type = models.CharField(max_length=20)
    project_no = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "Credit_auth"

class Proj_cust_enterprise_info(models.Model):
    '''项目-企业信息表'''
    id_card_no = models.CharField(max_length=20)
    project_no = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "proj_cust_enterprise_info"

class Proj_cust_enterprise_related_info(models.Model):
    '''项目-企业关键人信息表'''
    id_card_no = models.CharField(max_length=20)
    project_no = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "Proj_cust_enterprise_related_info"


class Proj_cust_personal_info(models.Model):
    '''项目-个人信息表'''
    id_card_no = models.CharField(max_length=20)
    project_no = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "Proj_cust_personal_info"

class Project_manage(models.Model):
    '''项目管理'''
    PROJECT_MANAGE_ID = models.CharField(max_length=20,primary_key=True)
    PROJECT_NO = models.CharField(max_length=20)
    PROJECT_GROUP_ID = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "Project_manage"


class Project_manage_group(models.Model):
    '''项目管理组(多交易结构)'''
    PROJECT_GROUP_ID = models.CharField(max_length=20,primary_key=True)
    SOURCE_SYS_RELA_NO = models.CharField(max_length=20)
    EFFECT_STATUS = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "Project_manage_group"

class Uaa_user(models.Model):
    '''用户表'''
    id = models.CharField(max_length=20,primary_key=True)
    login = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "Uaa_user"



#
# class Teacher(models.Model):
#     name = models.CharField(max_length=30)
#     age = models.IntegerField(blank=True, null=True)
#     tel = models.CharField(max_length=30)
#
#     class Meta:
#         managed = False
#         # app_label = "xiaowei_uat"
#         db_table = "Teacher"

class MeetingRoom(models.Model):
    name = models.CharField(max_length=100, unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.room} - {self.date} {self.start_time}-{self.end_time}"

