# -*- coding: utf-8 -*-
import logging
import time
import timeit

import allure
import requests

# from common.apollo import services
from utils.conn import RedisConnectionMgr
from utils.log import LOGGER
from utils.util import Counter, Dict, merge_dicts, attr_dict

try:
    import simplejson as json
except (ImportError, SyntaxError):
    import json
C = Counter()

INTERFACE_ERROR_L = ["code,url,resp"]


def _join_urls(root, *args):
    '''
    拼接url
    :param root: 根路径
    :param args:
    :return:
    '''
    urls = []
    if root.endswith(r"\/"):
        root = root[:-2]
    elif root.endswith("/"):
        root = root[:-1]
    urls.append(root)

    for path in args:
        if path is None or path.strip() == "":
            continue

        if path.startswith(r"\/"):
            path = path[2:]
        elif path.startswith("/"):
            path = path[1:]
        urls.append(path)
    return "/".join(urls)


class BaseClient(object):

    def __init__(self, session=None, extra_headers=None, **kwargs):
        if session and not isinstance(session, requests.Session):
            raise TypeError('need the instance of requests.Session class')
        self.session = session
        self.response_handlers = []  # 移除默认的status_coder_checker ,不对3xx抛异常处理
        self.json_handlers = []
        self.interceptor = None
        self.logger = LOGGER
        self.special_ip = kwargs.pop("special_ip", None)  # 特殊地区ip
        self.req_kwargs = dict(timeout=90)
        self.req_kwargs.update(kwargs)
        self.extra_headers = extra_headers or {}

    @staticmethod
    def login(mid):
        if mid is not None:
            r = requests.post('http://hassan.ximalaya.co/ep/admin/hassan/v2/uat/account/cookie/query',
                              json={"mid": mid})
            return r.json()
        return None

    def _call_api(self,
                  endpoint,
                  method="post",
                  req_kwargs=None,
                  *,
                  is_json_resp=True,
                  interceptor=None,
                  disable_log=False,
                  **kwargs):
        '''
        http调用函数
        :param endpoint: 接口地址,用ip拼接成完整的请求地址
        :param method: http请求方式
        :param req_kwargs: 透传给requests.request的请求参数（不包含url, method）
        :param is_json_resp: 是否json响应
        :param interceptor: 该参数赋值后,会改变输出值
        :param disable_log: 部分接口不打印日志,如文件上传接口
        :return: response : 属性字典包装的response
        '''
        # print(req_kwargs['headers'])
        LOGGER.debug(req_kwargs)
        if str(req_kwargs['headers']['Host']).startswith('m.test'):
            server_ip = 'm.test.ximalaya.com'
        elif str(req_kwargs['headers']['Host']).startswith('daka.test'):
            server_ip = 'daka.test.ximalaya.com'
        elif str(req_kwargs['headers']['Host']).startswith('ops.test'):
            server_ip = 'ops.test.ximalaya.com'
        elif str(req_kwargs['headers']['Host']).startswith('xxm.test'):
            server_ip = 'xxm.test.ximalaya.com'
        #  新增公司内部rpc接口的调用的host  @author:joe.shi@ximalaya.com
        elif str(req_kwargs['headers']['Host']).startswith('192.168.3.54'):
            server_ip = '192.168.3.54:8901'
        else:
            server_ip = 'ops.test.ximalaya.com'
        # print(req_kwargs)
        LOGGER.debug(req_kwargs)
        url = _join_urls('http://' + server_ip, endpoint)
        print('\n'+'**********' + url +'**********')
        LOGGER.debug(url)
        req_id = C.counter
        kwargs = self.req_kwargs.copy()
        merge_dicts(kwargs, req_kwargs)

        with allure.step('req url: {}'.format(url)):
            if not disable_log:
                self.logger.debug("start request",
                                  extra=dict(method=method,
                                             parameters=kwargs,
                                             url=url,
                                             request_id=req_id))
            allure.attach(method, "request method")
            allure.attach(url, "request url", allure.attachment_type.URI_LIST)
            allure.attach(json.dumps(kwargs['headers'], ensure_ascii=False, indent=4),
                          "request headers", allure.attachment_type.JSON)
            if kwargs.get('json'):
                allure.attach(json.dumps(kwargs['json'], ensure_ascii=False, indent=4),
                              "request json", allure.attachment_type.JSON)
            elif kwargs.get('params'):
                allure.attach(json.dumps(kwargs['params'], ensure_ascii=False, indent=4),
                              "request params", allure.attachment_type.JSON)
            elif kwargs.get('data'):
                allure.attach(json.dumps(kwargs['data'], ensure_ascii=False, indent=4),
                              "request data", allure.attachment_type.TEXT)
            if not self.session:
                self.session = requests.session()
            start = timeit.default_timer()
            # print(kwargs)
            response = self.session.request(method, url, **kwargs)
            # response.raise_for_status()  # requests 自带对status code检查的方法,对>=400的status code 抛出异常
            #counter_for_exception(response)  # 对环境不稳定就行检测统计
            # print(response)
            if not disable_log:
                latency = int((timeit.default_timer() - start) * 1000)
                if '<html' in response.text or not response.text:
                    self.logger.debug("got response",
                                      extra=dict(response=response.text,
                                                 request_id=req_id,
                                                 is_json_format=is_json_resp,
                                                 url=response.url,
                                                 status_code=response.status_code,
                                                 latency=latency))
                elif isinstance(response.text, str):
                    self.logger.debug("got response",
                                      extra=dict(response=response.text,
                                                 request_id=req_id,
                                                 is_json_format=is_json_resp,
                                                 url=response.url,
                                                 status_code=response.status_code,
                                                 latency=latency))
                else:
                    self.logger.debug(
                        "got response",
                        extra=dict(response=response.json() if is_json_resp else response.text,
                                   request_id=req_id,
                                   is_json_format=is_json_resp,
                                   url=response.url,
                                   status_code=response.status_code,
                                   latency=latency))
            allure.attach(str(response.status_code), "response status")
            allure.attach(str(latency), "response latency")
            allure.attach(json.dumps(dict(response.headers), ensure_ascii=False, indent=4),
                          "response headers", allure.attachment_type.JSON)
            if '<html' in response.text or not response.text:
                allure.attach(response.text, "response body", allure.attachment_type.HTML)
            elif isinstance(response.text, str):
                allure.attach(response.text, "response body", allure.attachment_type.TEXT)
            else:
                allure.attach(json.dumps(response.json(), ensure_ascii=False, indent=4),
                              "response body", allure.attachment_type.JSON)
            for handler in self.response_handlers:
                handler(response)

            if is_json_resp:
                try:
                    resp_to_json = response.json()  # 如果返回的是数字类型的字符串，resp.json()会变成数字
                    if isinstance(resp_to_json, (int, float)):
                        return resp_to_json
                except ValueError:
                    if not disable_log:
                        self.logger.error('convert response to json fail',
                                          extra=dict(request_id=req_id))
                        return response.text
                    raise
                else:
                    for handler in self.json_handlers:
                        handler(resp_to_json)
            intercept_func = interceptor or self.interceptor
            final_response = response if intercept_func is None else intercept_func(
                response,
                locals().get('resp_to_json', None))
            if isinstance(final_response.json(),list):
                return final_response.json()

            try:
                if Dict(final_response).code != -400:
                    red = RedisConnectionMgr(host='172.22.33.198')
                    if self.mid:
                        red.client.sadd('http_proxy_mid', self.mid)
                    red.client.sadd('http_proxy_path_' + method, endpoint)
                    if method == 'get':
                        data = req_kwargs['params']
                    elif method == 'post':
                        data = req_kwargs['data']
                    elif method == 'put':
                        data = req_kwargs['data']
                    elif method == 'delete':
                        data = req_kwargs['data']
                    elif method == 'patch':
                        data = req_kwargs['data']
                    elif method == 'options':
                        data = req_kwargs['data']
                    else:
                        data = req_kwargs['json']
                    for x in [
                        'actionKey', 'appkey', 'access_key', 'csrf_token', 'csrf', 'ts', 'sign'
                    ]:
                        if x in data:
                            data.pop(x)
                    red.client.zadd(
                        'http_proxy_data:' + endpoint,
                        {json.dumps(data, sort_keys=True, ensure_ascii=False): int(time.time())})
            except Exception as e:
                ...

            try:
                return attr_dict(final_response)
            except ValueError:
                return attr_dict(final_response.json())


def counter_for_exception(resp):
    r_dict = resp.json()
    code = str(r_dict.get("code"))

    if "504" == code or "-504" == code:
        INTERFACE_ERROR_L.append(",".join([code, resp.url, resp.text.replace(",", "，")]))
