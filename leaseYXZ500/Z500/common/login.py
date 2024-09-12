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
         "zonghao_uat":"64c09c8e292f6946aca59f166e6bb332f23f8615f23b0e443e6eb7602e1ae026",
         "zonghao_sit":"0dad862ecff035925690f92366213f72c7ff364d029ba72700805a71e181d746",
         "moziluo":"7d0a409bb44ab3ae3539a8a9fda397c6ed56cdc43c77fd6147d3e1c59b54d069",
         "jiaohailong":"6a57bc9c2845a449f2873adc510ca4244c310c1f604d19946af6264003fafdbb",    #1111
         "zhongyunyin":"7b2994e0510bdff433bccb8551a7f168974227169c3851ea61546e532dde715c",
         "uat":"7c60396d8ca138b4cf28dd39626102ebb95d28308cc9c7834e2cc8770f8b0c84",       #8888
         "caijieru":"fe979fca15bbaf65574aa2179070414a979d20df24970222fffaf589286dccf3",   #4444
         "ph_sd":"f55cfeed93688c157fa77f993619beb74768f4ba818dd70e035dda6e812efa29",
         "wangfangfang":"63af81259e04bcc046b4c07e484bebf58c441b90a2257d60dc6321f4fd87195b",
         "liaoruochen":"6516878ecba849e9e840a7672f0cae0227a3ede65475b8034602ece05f19547a",
         "zhuwang":"fcac531c1a7359d233ed74f27343210ef673a5be9ad596c31d68f8ef86254b21",
         "caiguodong":"d71166f649e82dd056e75bc793ce9c0a6cc1258930cf80a5111b49913ee84f80",
         "ph_guhanjie":"5d9fdd524fe7339b3d36b51ccad52886b84c3877ce5a8eab6a268b991415f4ac",
         "fanhanyu":"5cf6676bf1b47224147372f03dd95c348babb5203cc091c7bca34c6e0f5bae42",  # uat
         "limeng":"c547c4d55375917bfc49e9cf19d0896435dc63c6b0c1668d9f5894786bff7f4d",
         "ph_sunruxin":"7f3aaeb5882cb38884e7b282d44c4f2379b991477d952469568fce9916bfc6ef",
         "txzw":"ccc20c989d8c79c10c18cc3a4de68b3de39c9dcb239ad2815a6b7eb4ebe2d73b",   #9717  sit
         "hefei":"",
         "cm2":"28bea76c47758b57db0c9e4b9133915c3fe8628e2e4f1f10c40b1ff9b3e9e8e7",
         "spadmin":"d71166f649e82dd056e75bc793ce9c0a6cc1258930cf80a5111b49913ee84f80", #0255 uat
         "jhw":"d71166f649e82dd056e75bc793ce9c0a6cc1258930cf80a5111b49913ee84f80",
         "lisiyu":"d71166f649e82dd056e75bc793ce9c0a6cc1258930cf80a5111b49913ee84f80", #uat
         "liting":"29666aaed9d4a9498e235b4bf2dbd5f4101f5a984e641e18825452aec56a21a7",
         "zhengyuheng":"0ae774a051f9e5f40230329e98da33329e3e5f0ca6f59e3352c03bf9a608923c",   #3059
         "ljy":"cc165af296f4a693627a0fbc75edf10aaf298eba8dc3621d0eaea453342bbccc",
         "cs1":"d71166f649e82dd056e75bc793ce9c0a6cc1258930cf80a5111b49913ee84f80",
         "liudezhi":"d71166f649e82dd056e75bc793ce9c0a6cc1258930cf80a5111b49913ee84f80",
         "gaoyongxia":"d71166f649e82dd056e75bc793ce9c0a6cc1258930cf80a5111b49913ee84f80",
         "ph_zhongyunyin":"d71166f649e82dd056e75bc793ce9c0a6cc1258930cf80a5111b49913ee84f80",  #uat Msfl#0000
         "jitao":"01b5850d619532fd5f68a4553fa63c593dd7d644502e7bdd6a2ae156c53b50e0",  #uat #8988
         "msfl":"7adf0f9bc83eb29972c02ecbd4415b435f2afed2228fe0eef4355cdc87985cf4",
         "ywzg":"8c2340d2f7e921ffb1ff9dfb099fecc07ab1ae326fe579e8cdf3cbdd0f0fc13f", #Msfl@123
         "ph_jiangyakun":"64462cf41d806fd1b445f5821b1d68f0626fb4ae94f63d233fd5651dc9ab4ad5",
         "ph_lijunyan":"690786e363d6ec84a6cbce93bfde3feafdadfce528ca6e3bb3e7cc9edcb62f15",
         "ph_caijieru":"b4c51f0ec02308e6f5f4ad7efa14174bc295a49c9161229be3a7a3b369986005",
         "liuzihao":"d71166f649e82dd056e75bc793ce9c0a6cc1258930cf80a5111b49913ee84f80",
         "ljy":"cc165af296f4a693627a0fbc75edf10aaf298eba8dc3621d0eaea453342bbccc"}   #3790


def login(custName,env):
    if env == 'sit':
        url = 'http://sit-vrip.msfl.com.cn/'
    elif env == 'test':
        url = 'http://test-vrip.msfl.com.cn/'
    elif env == 'uat':
        url = 'http://uat-vrip.msfl.com.cn/'
    url_code = url + 'uaa/login-psms-code'
    url_sms = url + 'auth/login-sms'
    # else:
    #     url_code = 'http://test-vrip.msfl.com.cn/uaa/login-psms-code'
    #     url_sms = 'http://test-vrip.msfl.com.cn/auth/login-sms'
    if custName == "guhanjie":
        custName = "ph_guhanjie"
    if custName == "sunruxin":
        custName = "ph_sunruxin"
    if custName == "zonghao":
        if env == 'sit':
            custNamePas = "zonghao_sit"
        else:
            custNamePas = "zonghao_uat"
        data = {"password": cust[custNamePas], "username": custName}
    else:
        data = {"password": cust[custName], "username": custName}
    res_code = requests.request('POST', url_code, json=data, verify=True)
    print(res_code.text)
    data = {"code": "123456", "rememberMe": True, "username": "%s" % custName}
    res_sms = requests.request('POST', url_sms, json=data, verify=True).json()
    return res_sms
