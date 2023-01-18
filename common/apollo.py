# -*- coding: utf-8 -*-
import json

import requests
from utils.decorators import SingletonIfSameParameters
import inspect

def get_function_name():
    '''获取正在运行函数(或方法)名称'''
    return inspect.stack()[1][3]


class ApolloClient(metaclass=SingletonIfSameParameters):

    def __init__(self,
                 config_server_url=Apollo.CONFIG_SERVER,
                 app_id=Apollo.APP_ID,
                 cluster=Apollo.CLUSTER,
                 namespace=Apollo.NAMESPACE):
        self.config_server_url = config_server_url
        self.app_id = app_id
        self.cluster = cluster
        self.url = '{host}/{configs}/{app_id}/{cluster}/{namespace}'.format(
            host=self.config_server_url,
            configs=Apollo.CONFIGS,
            app_id=self.app_id,
            cluster=self.cluster,
            namespace=namespace)
        s = json.loads(requests.get(self.url).json()['configurations']['mysql'])
        self.config = requests.get(self.url).json()['configurations']


class _Services:
    apollo = ApolloClient()

    @property
    def configs(self):
        return self.apollo.config

    @property
    def mysql(self):
        return json.loads(self.configs['{}'.format(get_function_name())])

    @property
    def daka_token(self):

        return json.loads(self.configs['{}'.format(get_function_name())])

    @property
    def m_token(self):
        return json.loads(self.configs['{}'.format(get_function_name())])


    @property
    def ops_token(self):
        return json.loads(self.configs['{}'.format(get_function_name())])

    @property
    def growth_token(self):
        return json.loads(self.configs['{}'.format(get_function_name())])

    @property
    def math_token(self):
        return json.loads(self.configs['{}'.format(get_function_name())])

    @property
    def redis(self):
        return json.loads(self.configs['{}'.format(get_function_name())])

    @property
    def mpay_token(self):
        return json.loads(self.configs['{}'.format(get_function_name())])

    @property
    def m_xgn_token(self):
        return json.loads(self.configs['{}'.format(get_function_name())])

    @property
    def ops_growth_token(self):
        return json.loads(self.configs['{}'.format(get_function_name())])

    @property
    def qqx_token(self):
        return json.loads(self.configs['{}'.format(get_function_name())])


services = _Services()

if __name__ == '__main__':
    # print(services.configs)
    print(services.memcached)
    print(services.mysql)
    print(services.m_token)
    print(services.daka_token)
    print(services.redis)
    print(services.ops_token)
    print(services.growth_token)
    print(services.mpay_token)
    print(services.ops_growth_token)
    print(services.m_xgn_token)
    print(services.qqx_token)