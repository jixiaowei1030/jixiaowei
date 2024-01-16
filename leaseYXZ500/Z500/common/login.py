import requests



cust =  {"jxw": "69065d392b9ad3bc3c7034a4cffe416339bc7b8cbe4cc63a9d1d779c6da13bb1",
         "fht": "89ae7733c591b618bf21cf5f4a48e40dbf79c33495c94c91fbeccd843b141a81",
         "zll": "5d8fbee0cb6509d6252c977283b09c52f1fc17c6bfa1742c00f9f1177be256dc",
         "xzw":"c3c9773841309436de74b77a52020ab815052e1b414d3765e81ba974f2b69970",
         "cm":"e32d46dd141f4be8e619f36100a20e8667d9889b65f125fa3a1d18d34ae440ca",
         "huangzuning": "6a57bc9c2845a449f2873adc510ca4244c310c1f604d19946af6264003fafdbb",
         "huojunli":"6a57bc9c2845a449f2873adc510ca4244c310c1f604d19946af6264003fafdbb",
         "majie":"6a57bc9c2845a449f2873adc510ca4244c310c1f604d19946af6264003fafdbb",
         "hechaocheng":"dada1e7548e45f78a3949b8407b691369469744833524ce96beb2583c0671ed7",
         "fengyong":"ff469da47cbba9706105ab6f6309576cb43dc7b57a390177178787971ea7577f",
         "zonghao":"03f1f17ea039cd1f8f1da0670cf54b9d462ea584977f19632a80065244b89c3b",
         "moziluo":"7d0a409bb44ab3ae3539a8a9fda397c6ed56cdc43c77fd6147d3e1c59b54d069",
         "jiaohailong":"6a57bc9c2845a449f2873adc510ca4244c310c1f604d19946af6264003fafdbb",    #1111
         "zhongyunyin":"6516878ecba849e9e840a7672f0cae0227a3ede65475b8034602ece05f19547a",
         "uat":"7c60396d8ca138b4cf28dd39626102ebb95d28308cc9c7834e2cc8770f8b0c84",       #8888
         "caijieru":"6516878ecba849e9e840a7672f0cae0227a3ede65475b8034602ece05f19547a",
         "ph_sd":"f55cfeed93688c157fa77f993619beb74768f4ba818dd70e035dda6e812efa29",
         "wangfangfang":"63af81259e04bcc046b4c07e484bebf58c441b90a2257d60dc6321f4fd87195b",
         "liaoruochen":"6516878ecba849e9e840a7672f0cae0227a3ede65475b8034602ece05f19547a",
         "zhuwang":"fcac531c1a7359d233ed74f27343210ef673a5be9ad596c31d68f8ef86254b21",
         "caiguodong":"d71166f649e82dd056e75bc793ce9c0a6cc1258930cf80a5111b49913ee84f80",
         "ph_guhanjie":"2f0a382c8f8c6b81f634821a9a909772850e44f08d5c848b0d1cbe86a242e435",
         "fanhanyu":"b1de6cd7b1acdd9e2adccd1280e6360a03d3d04c4f6901e9d91edf220891bda6"}


def login(custName,env):
    if env == 'sit':
        url = 'http://sit-vrip.msfl.com.cn/'
    else:
        url = 'http://test-vrip.msfl.com.cn/'
    url_code = url + 'uaa/login-psms-code'
    url_sms = url + 'auth/login-sms'
    # else:
    #     url_code = 'http://test-vrip.msfl.com.cn/uaa/login-psms-code'
    #     url_sms = 'http://test-vrip.msfl.com.cn/auth/login-sms'
    if custName == "guhanjie":
        custName = "ph_guhanjie"
    data = {"password": cust[custName], "username": custName}
    res_code = requests.request('POST', url_code, json=data, verify=True)
    print(res_code.text)
    data = {"code": "123456", "rememberMe": True, "username": "%s" % custName}
    res_sms = requests.request('POST', url_sms, json=data, verify=True).json()
    return res_sms
