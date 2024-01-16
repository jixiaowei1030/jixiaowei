from django.db import models

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

