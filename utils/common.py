import pymysql
import types

# from common.apollo import services
from utils.conn import MySQLConnectionMgr, MemcachedConnectionMgr, RedisConnectionMgr
# from utils.shell_proxy.client import ShellClient
from utils.util import attr_dict
from common.const import RedisConfig,MysqlConfig


def get_mysql(mysql_login_info=None):
    if not mysql_login_info:
        # 默认拿service中设置的环境
        # mysql_login_info = services.mysql
        mysql_login_info = MysqlConfig.MYSQL

    mysql = MySQLConnectionMgr(autocommit=True, charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor,
                               **mysql_login_info).connection.cursor()

    # monkey patch
    def query(self, sql, fetch_all=False):
        try:
            self.execute(sql)
        except Exception as e:
            raise e
        else:
            if fetch_all:
                result = [attr_dict(r) if r else attr_dict({}) for r in self.fetchall()]
            else:
                r = self.fetchone()
                result = attr_dict(r) if r else attr_dict({})

        return result

    mysql.query = types.MethodType(query, mysql)
    return mysql


def get_redis(**kwargs):
    if not kwargs:
        # login_info = services.redis
        login_info = RedisConfig.REDIS
    else:
        # temp = services.redis
        temp = RedisConfig.REDIS
        temp.update(kwargs)
        login_info = temp

    redis = RedisConnectionMgr(**login_info).client

    def fuzzy_delete(self, exp_key):
        try:
            keys = self.keys(exp_key)
            for key in keys:
                self.delete(key)
        except Exception as e:
            raise e
        return "OK"

    redis.fuzzy_delete = types.MethodType(fuzzy_delete, redis)
    return redis


# def get_memcached():
#     return MemcachedConnectionMgr(**services.memcached).client


# def get_shell():
#     return ShellClient(services.ip)

if __name__ == '__main__':
    # a = get_redis()
    b = get_mysql()