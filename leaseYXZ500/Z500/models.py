from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=20)

    class Meat:
        manage = True

class Sys_param_config(models.Model):
    config_type = models.CharField(max_length=20)
    config_value = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = "sys_param_config"

class Auth_group(models.Model):
    name = models.CharField(max_length=20)
    class Meta:
        managed = False
        db_table = "auth_group"







