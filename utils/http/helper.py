# -*- coding: utf-8 -*-
import functools
import re
from datetime import datetime, date
from functools import wraps
from inspect import _empty, signature
from common.getlogintoken import LoginGetToken as loginone
from common.getopstoken import LoginGetToken as logintwo
from common.gethqgtoken import LoginGetToken as loginthree
from utils.http import BaseClient
from common.const import Env,UserToken,LoginToken

try:
    import simplejson as json
except ImportError:
    import json


class CJsonEncoder(json.JSONEncoder):
    # 修复json.dumps(datetime,date)无法序列化的错误
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def _set_or_update_node(parent: dict, key: str, d: dict):
    if isinstance(parent.get(key, None), dict):
        parent[key].update(d)
    else:
        parent[key] = d


def hook_params(client: BaseClient, method: str, request: dict, has_token: bool):
    """
    自动填充必传的字段
    :param client:
    :param method:
    :param request:
    :param has_token: 特殊接口必须使用该字段
    :return:
    """
    required = {
        # 'actionKey': 'appkey',
        # 'appkey': services.appkey,
        # 'access_key': client.login_info['data']['token'] if client.login_info else '',
        # 'csrf_token': client.login_info['data']['token'] if client.login_info else '',
        # 'csrf': client.login_info['data']['csrf'] if client.login_info else '',
        # 'ts': int(time.time())
    }
    if has_token:
        required["token"] = client.login_info['data']['token'] if client.login_info else ''
    if method.upper() == "GET":
        if request.get("params"):
            request['params'].update(required)
        else:
            request['params'] = required
        request['params'] = {k: v for k, v in request['params'].items() if v not in (None, "")}
        restore_key(request['params'])
    elif request.get("json"):
        request['json'].update(required)
        request['json'] = {k: v for k, v in request['json'].items() if v not in (None, "")}
        restore_key(request['json'])
    elif isinstance(request.get("data"), dict):  # data有可能不是dict
        request['data'].update(required)
        request['data'] = {k: v for k, v in request['data'].items() if v not in (None, "")}
        restore_key(request['data'])


suitable_env = [i for i in Env.__dict__.keys() if not i.startswith("__")]


def restore_key(Dict):
    '''恢复key名'''
    for x in Dict:
        if x.startswith('int_'):
            Dict[x[4:]] = Dict[x]
            del Dict[x]
        if x.endswith('__'):
            Dict[x[:-2]] = Dict[x]
            del Dict[x]


def hook_all_headers(client: BaseClient, request: dict, xmkp, moblie, password):
    '''处理http请求的headers'''
    # 设置env环境
    env = Env.ENV

    headersdata = {}  # 变量使用之前建议先定义出来
    is_ops = 0
    if xmkp == 'daka':
        Host = "daka.test.ximalaya.com"
    elif xmkp == 'm' or xmkp == 'math':
        Host = "m.test.ximalaya.com"
    elif xmkp == 'xxm':
        Host = 'xxm.test.ximalaya.com'
    else:
        Host = "ops.test.ximalaya.com"
        is_ops = 1

    if is_ops == 0 and xmkp != 'math':
        if LoginToken.XMLYTOKEN == {}:
            login = loginone(moblie, password, env)
            LoginToken.XMLYTOKEN = login.LoginGetToken()
        else:pass
        token = "4&_token=" + LoginToken.XMLYTOKEN
        headersdata = {
            "Host": Host,
            "Cookie": token
        }
        print(token)
    elif is_ops == 1:
        if LoginToken.OPSTOKEN == {}:
            loginops = logintwo(moblie, password, env)
            LoginToken.OPSTOKEN = loginops.LoginGetToken()
        else:pass
        token = LoginToken.OPSTOKEN
        headersdata = {
            "Host": Host,
            "Accept": "application/json, text/plain, */*",
            "Cookie": "_const_cas_ticket = " + token
        }
    elif is_ops == 0 and xmkp == 'math':
        if LoginToken.XMLYTOKEN == {}:
            login = loginone(moblie, password, env)
            LoginToken.XMLYTOKEN = login.LoginGetToken()
        else:pass
        token = "4&_token=" + LoginToken.XMLYTOKEN

        if LoginToken.HQGTOKEN == {}:
            logintoken = loginthree(moblie, env)
            LoginToken.HQGTOKEN = logintoken.LoginGetToken()
        else:pass
        authorization = LoginToken.HQGTOKEN
        headersdata = {
            "Host": Host,
            "authorization": authorization,
            "Cookie": token
        }
    else:pass

    UserToken.USERTOKEN = headersdata
    request['headers'] = headersdata
    request['headers'].update(client.extra_headers)


# 新增公司内部rpc接口的调用header @author:joe.shi@ximalaya.com
def hook_rpc_headers(request):
    Host = "192.168.3.54:8901"
    headersdata = {
        "Host": Host,
        "xmly-login-user": "joe.shi"
    }
    request['headers'] = headersdata


# def hook_qqx_headers(client: BaseClient, request: dict):
#     """
#     处理奇奇学请求headers
#     @param client:
#     @param request:
#     @return: None
#     """
#     '''处理新概念请求的headers'''
#     request['headers'] = services.qqx_token
#     request['headers'].update(client.extra_headers)

#
# def sign(Dict):
#     '''移动端请求签名算法'''
#     m = hashlib.md5()
#     urlencoded = urllib.parse.urlencode(Dict)
#     m.update(bytes(urlencoded + services.app_secret, 'utf8'))
#     s = m.hexdigest()
#     Dict.update({'sign': s})
#
#
# def hook_sign(method: str, request: dict):
#     '''为三种格式数据排序和添加移动端签名'''
#     if method.upper() == "GET":
#         request['params'] = {k: request['params'][k] for k in sorted(request['params'].keys())}
#         sign(request['params'])
#     elif request.get("json"):
#         request['json'] = {k: request['json'][k] for k in sorted(request['json'].keys())}
#         sign(request['json'])
#     elif isinstance(request.get("data"), dict):  # data有可能不是dict
#         request['data'] = {k: request['data'][k] for k in sorted(request['data'].keys())}
#         sign(request['data'])


def smart_payload(func):
    '''自动组装payload'''

    @wraps(func)
    def _wrapper(*args, **kwargs):
        func(*args, **kwargs)  # to raise TypeError
        parameters = signature(func).parameters
        arguments = list(parameters.keys())
        payload = {
            parameter.name: parameter.default
            for _, parameter in parameters.items()
            if parameter.default is not _empty and parameter.name != "self"
        }
        if arguments[0] == "self":
            arguments.pop(0)
            args = args[1:]
        if args:
            for index, val in enumerate(args):
                arg_name = arguments[index]
                payload[arg_name] = val
        payload.update(kwargs)
        return payload

    return _wrapper


def api(rule,
        method="post",
        is_json_req=False,
        arg_handler=None,
        xmkp="ops",
        has_token=False,
        **kwargs):
    """
    :param rule: 接口地址,如果是restful接口,则: /query/<id>/
    :param method: 请求方式 get/post/option ...
    :param is_json_req: 是否是json请求,如果传True，传给requests.request为 json=payload
    :param arg_handler: 定义后,可以更改参数名称,如将驼峰参数名修改为其lower_case
    :param mlive: 是否是管理后台请求
    :param kwargs: 具体参考BaseClient._call_api的请求参数
    :param has_token: 业务上 token 值。
    :return:
    """

    def wrapper(func):
        @wraps(func)
        def _wrapper(self, *fargs, **fkwargs):
            patter = re.compile(r"[{][{](.*?)[}][}]", re.S)
            endpoint = rule
            for key in patter.findall(rule):
                endpoint = patter.sub(fkwargs.pop(key, ""), endpoint, count=1)
            # endpoint = rule + fkwargs.pop("extra_url", "")
            if "req_json" in fkwargs:
                payload = fkwargs["req_json"]
                moblie = fkwargs['mobile']
                password = fkwargs['password']
            elif "req_data" in fkwargs:
                payload = fkwargs["req_data"]
                moblie = fkwargs['mobile']
                password = fkwargs['password']
            # 公司内部rpc接口的调用特殊逻辑 @author:joe.shi@ximalaya.com
            elif "rpc_req" in kwargs:
                payload = fargs[0]
            else:
                payload = smart_payload(func)(self, *fargs, **fkwargs)
                moblie = payload['mobile']
                password = payload['password']
                del payload['mobile']
                del payload['password']
            print("-----",payload)
            special_ip = payload.get("special_ip")
            print(special_ip)
            c = re.compile(r'<\S*?>')
            paths = c.findall(endpoint)
            for path in paths:
                tp = path[1:-1]
                if tp not in payload:
                    raise ValueError("invalid restful api rule")
                else:
                    endpoint = endpoint.replace(path,
                                                str(payload.pop(tp)))  # url path must be string
            if arg_handler:
                payload = {arg_handler(k): v for k, v in payload.items()}
            req_kwargs = kwargs.pop("req_kwargs", {})
            if method.upper() == "GET":
                _set_or_update_node(req_kwargs, 'params', payload)
            elif is_json_req:
                _set_or_update_node(req_kwargs, 'json', payload)
            else:
                _set_or_update_node(req_kwargs, 'data', payload)
            hook_params(self, method, req_kwargs, has_token)

            # 公司内部rpc接口的调用特殊逻辑 @author:joe.shi@ximalaya.com
            if "rpc_req" in kwargs:
                hook_rpc_headers(req_kwargs)
                req_kwargs['data']['params'] = json.dumps(req_kwargs['data']['params'], cls=CJsonEncoder)

            else:
                hook_all_headers(self, req_kwargs, xmkp, moblie, password)

            return self._call_api(endpoint=endpoint,
                                  method=method,
                                  req_kwargs=req_kwargs,
                                  special_ip=special_ip,
                                  **kwargs)

        return _wrapper

    return wrapper


get_xxm = functools.partial(api, method='get', xmkp='xxm')
post_xxm = functools.partial(api, method='post', xmkp='xxm')

get_m = functools.partial(api, method='get', xmkp='m')
post_m = functools.partial(api, method='post', xmkp='m')
patch_m = functools.partial(api, method='patch', xmkp='m')

get_ops = functools.partial(api, method='get', xmkp='ops')
post_ops = functools.partial(api, method='post', xmkp='ops')
put_ops = functools.partial(api, method='put', xmkp='ops')
delete_ops = functools.partial(api, method='delete', xmkp='ops')
patch_ops = functools.partial(api, method='patch', xmkp='ops')

get_daka = functools.partial(api, method='get', xmkp='daka')
post_daka = functools.partial(api, method='post', xmkp='daka')

get_math = functools.partial(api, method='get', xmkp='math')
post_math = functools.partial(api, method='post', xmkp='math')

post_rpc = functools.partial(api, method='post', xmkp='rpc', rpc_req=1)  # 公司内部rpc接口的调用特殊逻辑 @author:joe.shi@ximalaya.com
