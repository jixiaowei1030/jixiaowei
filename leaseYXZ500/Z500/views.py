#encoding='utf-8'

import json
import time
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests
import jsonpath
import sys

# Create your views here.

url = 'http://sit-vrip.msfl.com.cn/'

req = requests.session()

def api(**kwargs):
    global headers_uat
    global url
    global req
    retries = Retry(total=2,
                    status_forcelist=[400, 500, 502, 503, 504])
    url_new = url +kwargs.get("url")
    kwargs.pop("url")
    req.mount('http://', HTTPAdapter(max_retries=retries))
    req.mount('https://', HTTPAdapter(max_retries=retries))
    res = req.request(url =url_new, verify=True, headers=headers_uat, **kwargs).json()
    print(url_new,res)
    return res

def login(custName):
    login = {"jxw":"d71166f649e82dd056e75bc793ce9c0a6cc1258930cf80a5111b49913ee84f80",
             "fht":"89ae7733c591b618bf21cf5f4a48e40dbf79c33495c94c91fbeccd843b141a81",
             "zll":"5d8fbee0cb6509d6252c977283b09c52f1fc17c6bfa1742c00f9f1177be256dc",
             "Huangzuning":"6a57bc9c2845a449f2873adc510ca4244c310c1f604d19946af6264003fafdbb",
             "xzw":"c3c9773841309436de74b77a52020ab815052e1b414d3765e81ba974f2b69970"}
    url1 = 'http://test-vrip.msfl.com.cn/uaa/login-psms-code'
    data = {"password":login[custName],"username":custName}
    res1 = requests.request('POST', url1, json=data,verify=True)
    print(res1)
    url2 = 'http://test-vrip.msfl.com.cn/auth/login-sms'
    data = {"code":"123456","rememberMe":True,"username":"%s"%custName}
    res2 = requests.request('POST', url2, json=data, verify=True).json()
    return res2

def pro_page():
    url = 'ifc/api/credit-auth/project/page'
    data = {
            "current": 1,
            "size": 20,
            "leaseName": "",
            "statusCode": "000000"
        }
    res = api(method ="POST", url=url,  json = data)
    return res

def preQuery(projectNo):
    '''预审初始化'''
    url = 'ifc/api/pre-approval/init?projectNo=%s'%projectNo
    res = api(method = "GET", url = url)
    return res

def add_pro(lesaseName):
    '''新建项目'''
    url = 'ifc/api/credit-auth/createProj?leaseName=%s' % lesaseName
    res = api(method="GET", url=url)
    return res

def getPro(projectNo):
    url = 'ifc/api/credit-auth/project/query/detail?projectNo=%s'%projectNo
    res = api(method ="GET", url=url)
    return res

def creditAuthSave(projectNo):
    '''创建征信授权'''
    url = 'ifc/callback/credit-auth/save'
    data_fht = {
        "businessName": "测试软创",
        "businessAddress": None,
        "businessCreditCode": "911101083398346103",
        "businessStartDate": None,
        "businessTermEndDate": None,
        "projectNo": projectNo,
        "preAprlCode": projectNo +"202308031008597437",
        "creditCustomerType": "ENT",
        "creditCustomerName": "范怀通",
        "creditCustomerTel": "13020117356",
        "creditCustomerNo": "412702199005284111",
        "creditCustomerIdType": None,
        "certificateValidStartDate": None,
        "certificateValidEndDate": None,
        "identityType": "法人",
        "accountManager": "fht",
        "creditCustomerSex": None,
        "creditCustomerAddress": "深圳市罗湖区深南东路5047号平安银行总行",
        "custCenterCode": None,
        "source": None
    }
    res = api(method='POST', url=url, json=data_fht)
    time.sleep(1)
    data_jxw = {
            "businessName": "测试Z500公司J2",
            "businessAddress": None,
            "businessCreditCode": "91310000NRNL32PU3J",
            "businessStartDate": None,
            "businessTermEndDate": None,
            "projectNo": projectNo,
            "preAprlCode": projectNo +"202308021551111545",
            "creditCustomerType": "ENT",
            "creditCustomerName": "季晓伟",
            "creditCustomerTel": "15705101126",
            "creditCustomerNo": "320683199410302714",
            "creditCustomerIdType": None,
            "certificateValidStartDate": None,
            "certificateValidEndDate": None,
            "identityType": "法人",
            "accountManager": "jxw",
            "creditCustomerSex": None,
            "creditCustomerAddress": "上海",
            "custCenterCode": None,
            "source": None
        }
    res = api(method='POST', url=url, json=data_jxw)

def creditAuthBack(projectNo):
    '''征信授权完成'''
    url = 'ifc/callback/credit-auth/signOffCallback'
    data_fht = {
        "preAprlCode": projectNo + "202308031008597437",
        "ssqContractId": "3374570986154108930",
        "businessLicenceFileId": "9015937627781681152",
        "faceFileId": "9121959342059274240",
        "backFileId": "9121869907951071232"
    }
    res = api(method='POST', url=url, json=data_fht)
    data_jxw =  {
        "backFileId": "9020716865953443840",
        "businessLicenceFileId": "6868482948483813376",
        "faceFileId": "9020792603410939904",
        "preAprlCode": projectNo + "202308021551111545",
        "ssqContractId": "3374018567829595143"
    }
    res = api(method='POST', url=url, json=data_jxw)

def taskCompleteInit(taskid):
    '''初始化流程'''
    url = 'ifc/api/flow/task-complete/init?taskId=%s'%taskid
    res = api(method='GET', url=url)

def proSubmit(projectNo):
    '''预审提交'''
    url = 'ifc/api/pre-approval/submit'
    res_query = preQuery(projectNo)
    data={
        "projectNo": projectNo,
        "customerList": [
            {
                "id": jsonpath.jsonpath(res_query,'$..id')[0],
                "creditCustomerType": jsonpath.jsonpath(res_query,'$..creditCustomerType')[0],
                "creditCustomerTypeName": jsonpath.jsonpath(res_query,'$..creditCustomerTypeName')[0],
                "creditCustomerName": jsonpath.jsonpath(res_query,'$..creditCustomerName')[0],
                "creditCustomerNo": jsonpath.jsonpath(res_query,'$..creditCustomerNo')[0],
                "creditCustomerIdType": jsonpath.jsonpath(res_query,'$..creditCustomerIdType')[0],
                "creditCustomerIdTypeName": jsonpath.jsonpath(res_query,'$..creditCustomerIdTypeName')[0],
                "roleType": "6"
            },
            {
                "id": jsonpath.jsonpath(res_query,'$..id')[1],
                "creditCustomerType": jsonpath.jsonpath(res_query,'$..creditCustomerType')[1],
                "creditCustomerTypeName": jsonpath.jsonpath(res_query,'$..creditCustomerTypeName')[1],
                "creditCustomerName": jsonpath.jsonpath(res_query,'$..creditCustomerName')[1],
                "creditCustomerNo": jsonpath.jsonpath(res_query,'$..creditCustomerNo')[1],
                "creditCustomerIdType": jsonpath.jsonpath(res_query,'$..creditCustomerIdType')[1],
                "creditCustomerIdTypeName": jsonpath.jsonpath(res_query,'$..creditCustomerIdTypeName')[1],
                "roleType": "1"
            },
            {
                "id": jsonpath.jsonpath(res_query,'$..id')[2],
                "creditCustomerType": jsonpath.jsonpath(res_query,'$..creditCustomerType')[2],
                "creditCustomerTypeName": jsonpath.jsonpath(res_query,'$..creditCustomerTypeName')[2],
                "creditCustomerName": jsonpath.jsonpath(res_query,'$..creditCustomerName')[2],
                "creditCustomerNo": jsonpath.jsonpath(res_query,'$..creditCustomerNo')[2],
                "creditCustomerIdType": jsonpath.jsonpath(res_query,'$..creditCustomerIdType')[2],
                "creditCustomerIdTypeName": jsonpath.jsonpath(res_query,'$..creditCustomerIdTypeName')[2],
                "roleType": "2"
            },
            {
                "id": jsonpath.jsonpath(res_query,'$..id')[3],
                "creditCustomerType": jsonpath.jsonpath(res_query,'$..creditCustomerType')[3],
                "creditCustomerTypeName": jsonpath.jsonpath(res_query,'$..creditCustomerTypeName')[3],
                "creditCustomerName": jsonpath.jsonpath(res_query,'$..creditCustomerName')[3],
                "creditCustomerNo": jsonpath.jsonpath(res_query,'$..creditCustomerNo')[3],
                "creditCustomerIdType": jsonpath.jsonpath(res_query,'$..creditCustomerIdType')[3],
                "creditCustomerIdTypeName": jsonpath.jsonpath(res_query,'$..creditCustomerIdTypeName')[3],
                "roleType": "3"
            }
        ],
        "productType": "LS-DFL",
        "productNo": "LeaseYXZ300"
    }
    res = api(method ="POST", url=url,  json = data)
    return res_query

def opinionSumit(taskId):
    taskCompleteInit(taskId)
    '''提交审批意见'''
    url = 'ifc/api/flow/task-complete'
    data = {
            "remind": "测试同意222",
            "taskId": taskId
        }
    time.sleep(3)
    res = api(method = 'POST', url =url,json = data)

def custEnterpriseQuery(projectNo):
    '''客户信息-承租人-查询'''
    url = 'ifc/api/proj_cust_enterprise_info/queryByCondition'
    data = {
        "projectNo": projectNo
    }
    res = api(method = 'POST', url =url,json = data)
    return res

def custEnterpriseSave(projectNo):
    res_query = custEnterpriseQuery(projectNo)
    url = 'ifc/api/proj_cust_enterprise_info/save'
    data = {
            "id": jsonpath.jsonpath(res_query,'$..id')[0],
            "projectNo": projectNo,
            "sourceId": jsonpath.jsonpath(res_query,'$..sourceId')[0],
            "projectCustomerInfoId": jsonpath.jsonpath(res_query,'$..projectCustomerInfoId')[0],
            "roleType": jsonpath.jsonpath(res_query,'$..roleType')[0],
            "name": jsonpath.jsonpath(res_query,'$..name')[0],
            "idCardType": jsonpath.jsonpath(res_query,'$..idCardType')[0],
            "idCardTypeName":  jsonpath.jsonpath(res_query,'$..idCardTypeName')[0],
            "idCardNo": jsonpath.jsonpath(res_query,'$..idCardNo')[0],
            "phoneNumber": "15705101126",
            "country": "156",
            "countryName": "中国",
            "interIndustryClassifyOne": "A",
            "interIndustryClassifyTwo": "A01",
            "interIndustryClassifyThree": "A011",
            "interIndustryClassifyFour": "A0111",
            "interIndustryClassifyOneName": "农、林、牧、渔业",
            "interIndustryClassifyTwoName": "农业",
            "interIndustryClassifyThreeName": "谷物种植",
            "interIndustryClassifyFourName": "稻谷种植",
            "industryClassifyOne": "A",
            "industryClassifyTwo": "A01",
            "industryClassifyOneName": "机加",
            "industryClassifyTwoName": "机械加工",
            "registrationProvince": "110000",
            "registrationCity": "110100",
            "registrationRegion": "110101",
            "registrationProvinceName": "北京市",
            "registrationCityName": "市辖区",
            "registrationRegionName": "东城区",
            "registrationAddress": "上海",
            "officeProvince": "110000",
            "officeCity": "110100",
            "officeLocation": "110101",
            "officeProvinceName": "北京市",
            "officeCityName": "市辖区",
            "officeLocationName": "东城区",
            "officeAddress": "上海",
            "actualBusinessProvince": "110000",
            "actualBusinessCity": "110100",
            "actualBusinessLocation": "110101",
            "actualBusinessProvinceName": "北京市",
            "actualBusinessCityName": "市辖区",
            "actualBusinessLocationName": "东城区",
            "actualBusinessAddress": "上海",
            "rentStockholderRelated": None,
            "rentRelated": None,
            "ruralUrbanSignage": "N",
            "ruralUrbanSignageName": "否",
            "projectSource": "01",
            "projectSourceName": "银行推荐",
            "licProjectInvestmentOne": "A",
            "licProjectInvestmentTwo": "A01",
            "licProjectInvestmentThree": "A011",
            "licProjectInvestmentFour": "A0111",
            "licProjectInvestmentOneName": "农、林、牧、渔业",
            "licProjectInvestmentTwoName": "农业",
            "licProjectInvestmentThreeName": "谷物种植",
            "licProjectInvestmentFourName": "稻谷种植",
            "businessScope": "测试",
            "mainBusinessProducts": "测试",
            "enterpriseSize": "LARGE",
            "enterpriseSizeName": "大型",
            "enterpriseType": "10",
            "enterpriseTypeName": "法人企业",
            "institutionRegistCertNumber": None,
            "financialInstitutionCode": None,
            "holdingType": "A",
            "holdingTypeName": "公有控股经济",
            "zhongzhengCode": "122",
            "currency": "CNY",
            "currencyName": "人民币",
            "registeredCapital": "1000.00",
            "paidinCapital": "1000.00",
            "capitalization": "1000.00",
            "revenue": "1000.00",
            "establishmentTime": "2023-07-19 00:00:00",
            "businessLicenseExpirationDate": "2025-07-19 00:00:00",
            "businessStatus": "01",
            "businessStatusName": "正常运营",
            "employeeNumber": "1000",
            "legalRepresentative": "季晓伟",
            "legalRepresentativeMobile": "15705101126",
            "legalPersonPhone": "320683199410302714",
            "actualController": "季晓伟",
            "nationalEconomy": "A",
            "nationalEconomyName": "广义政府",
            "listedCompanyLogo": "A",
            "listedCompanyLogoName": "A股",
            "resolutionType": None,
            "resolutionTypeName": None,
            "email": "123@163.com",
            "registration": ["110000", "110100", "110101"],
            "industryType": ["A", "A01"],
            "office": ["110000", "110100", "110101"],
            "actualBusiness": ["110000", "110100", "110101"],
            "internationalIndustryType": ["A", "A01", "A011", "A0111"],
            "licProjectInvestment": ["A", "A01", "A011", "A0111"]
        }
    res = api(method = 'POST', url =url,json = data)

def custEnterpriseRelatedQuery(projectNo):
    '''客户信息-关键人-查询'''
    url = 'ifc/api/proj_cust_enterprise_related_info/queryByCondition'
    data = {
        "projectNo": projectNo
    }
    res = api(method = 'POST', url =url,json = data)
    return res

def creditQuery(projectNo):
    url = 'ifc/api/credit-auth/queryList'
    data = {
            "searchParam": "",
            "projectNo": projectNo,
            "creditCustomerType": "IND"
        }
    res = api(method = 'POST', url =url,json = data)
    return res

def custEnterpriseRelateSave(projectNo):
    res_query = custEnterpriseRelatedQuery(projectNo)
    res_credit =creditQuery(projectNo)
    url = 'ifc/api/proj_cust_enterprise_related_info/edit'
    data = {
            "projectNo": projectNo,
            "actualController": {
                "id": jsonpath.jsonpath(res_query,'$..actualController.id')[0],
                "projectNo": projectNo,
                "sourceId": jsonpath.jsonpath(res_query,'$..actualController.sourceId')[0],
                "enterpriseInfoId": jsonpath.jsonpath(res_query,'$..actualController.enterpriseInfoId')[0],
                "roleType": "6",
                "resolutionType": None,
                "name": jsonpath.jsonpath(res_query,'$..actualController.name')[0],
                "idCardType": jsonpath.jsonpath(res_query,'$..actualController.idCardType')[0],
                "idCardTypeName": jsonpath.jsonpath(res_query,'$..actualController.idCardTypeName')[0],
                "idCardNo": jsonpath.jsonpath(res_query,'$..actualController.idCardNo')[0],
                "mobile": None,
                "shareholdingRatio": None,
                "renterRelationship": None,
                "residenceAddress": None,
                "creditReportTime": None,
                "authId": None
            },
            "legalRepresentative": {
                "id": jsonpath.jsonpath(res_query,'$..legalRepresentative.id')[0],
                "projectNo": projectNo,
                "sourceId": jsonpath.jsonpath(res_query,'$..legalRepresentative.sourceId')[0],
                "enterpriseInfoId": jsonpath.jsonpath(res_query,'$..legalRepresentative.enterpriseInfoId')[0],
                "roleType": "4",
                "resolutionType": None,
                "name": jsonpath.jsonpath(res_query,'$..legalRepresentative.name')[0],
                "idCardType": jsonpath.jsonpath(res_query,'$..legalRepresentative.idCardType')[0],
                "idCardTypeName": jsonpath.jsonpath(res_query,'$..legalRepresentative.idCardTypeName')[0],
                "idCardNo": jsonpath.jsonpath(res_query,'$..legalRepresentative.idCardNo')[0],
                "mobile": None,
                "shareholdingRatio": None,
                "renterRelationship": None,
                "residenceAddress": None,
                "creditReportTime": None,
                "authId": None
            },
            "beneficiary": {
                    "authId": jsonpath.jsonpath(res_credit,'$..id')[0],
                    "name": jsonpath.jsonpath(res_credit,'$..creditCustomerName')[0],
                    "idCardNo": jsonpath.jsonpath(res_credit,'$..creditCustomerNo')[0],
                    "idCardType": jsonpath.jsonpath(res_credit,'$..creditCustomerIdType')[0],
                    "idCardTypeName": jsonpath.jsonpath(res_credit,'$..creditCustomerIdTypeName')[0],
                    "residenceAddress": jsonpath.jsonpath(res_credit,'$..creditCustomerAddress')[0]
            },
            "personalIds": [],
            "custEnterpriseIds": [],
            "personalInfoModels":[
                {
                    "id":res_query["data"]["personalInfoModels"][0]["id"],
                    "projectNo": projectNo,
                    "projectCustomerInfoId": res_query["data"]["personalInfoModels"][0]["projectCustomerInfoId"],
                    "sourceId":res_query["data"]["personalInfoModels"][0]["sourceId"],
                    "roleType":"2",
                    "name":"范怀通",
                    "idCardType":"110",
                    "idCardTypeName":"身份证",
                    "idCardNo":"412702199005284111",
                    "mobile":"13020117356",
                    "country":"156",
                    "countryName":None,
                    "actualControllerRelationship":"director",
                    "actualControllerRelationshipName":None,
                    "maritalStatus":"MARRIED",
                    "maritalStatusName":None,
                    "gender":"1",
                    "genderName":None,
                    "birthDate":"2023-07-28",
                    "nation":"22",
                    "nationName":None,
                    "education":"1010",
                    "educationName":None,
                    "annualIncome":"1000.00",
                    "idProvince":"110000",
                    "idProvinceName":None,
                    "idCity":"110100",
                    "idCityName":None,
                    "idLocation":"110101",
                    "idLocationName":None,
                    "idAddress":"上海",
                    "creditReportTime":None,
                    "email":"666@163.com",
                    "authId":"1684739301136515074",
                    "idArray":[
                        "110000",
                        "110100",
                        "110101"
                    ]
                }
            ],
            "projCustEnterpriseVMList":[
                {
                    "id":res_query["data"]["projCustEnterpriseVMList"][0]["id"],
                    "projectNo": projectNo,
                    "sourceId":res_query["data"]["projCustEnterpriseVMList"][0]["sourceId"],
                    "projectCustomerInfoId":res_query["data"]["projCustEnterpriseVMList"][0]["projectCustomerInfoId"],
                    "roleType":"3",
                    "name":"测试软创",
                    "idCardType":"200",
                    "idCardTypeName":"统一社会信用代码证",
                    "idCardNo":"911101083398346103",
                    "mobile":None,
                    "country":"156",
                    "countryName":"中国",
                    "interIndustryClassifyOneName":"农、林、牧、渔业",
                    "interIndustryClassifyOne":"A",
                    "interIndustryClassifyTwoName":"农业",
                    "interIndustryClassifyTwo":"A01",
                    "interIndustryClassifyThreeName":"谷物种植",
                    "interIndustryClassifyThree":"A011",
                    "interIndustryClassifyFourName":"稻谷种植",
                    "interIndustryClassifyFour":"A0111",
                    "industryClassifyOneName":"机加",
                    "industryClassifyOne":"A",
                    "industryClassifyTwoName":"机械加工",
                    "industryClassifyTwo":"A01",
                    "registrationProvinceName":"北京市",
                    "registrationProvince":"110000",
                    "registrationCityName":"市辖区",
                    "registrationCity":"110100",
                    "registrationRegionName":"东城区",
                    "registrationRegion":"110101",
                    "registrationAddress":"上海",
                    "officeProvinceName":"北京市",
                    "officeProvince":"110000",
                    "officeCityName":"市辖区",
                    "officeCity":"110100",
                    "officeLocationName":"东城区",
                    "officeLocation":"110101",
                    "officeAddress":"上海",
                    "actualBusinessProvinceName":"北京市",
                    "actualBusinessProvince":"110000",
                    "actualBusinessCityName":"市辖区",
                    "actualBusinessCity":"110100",
                    "actualBusinessLocationName":"东城区",
                    "actualBusinessLocation":"110101",
                    "actualBusinessAddress":"上海",
                    "rentStockholderRelated":True,
                    "rentRelated":True,
                    "ruralUrbanSignageName":"否",
                    "ruralUrbanSignage":"N",
                    "projectSourceName":"银行推荐",
                    "projectSource":"01",
                    "licProjectInvestmentOneName":"农、林、牧、渔业",
                    "licProjectInvestmentOne":"A",
                    "licProjectInvestmentTwoName":"农业",
                    "licProjectInvestmentTwo":"A01",
                    "licProjectInvestmentThreeName":"谷物种植",
                    "licProjectInvestmentThree":"A011",
                    "licProjectInvestmentFourName":"稻谷种植",
                    "licProjectInvestmentFour":"A0111",
                    "businessScope":"测试",
                    "mainBusinessProducts":"测试",
                    "enterpriseSizeName":"大型",
                    "enterpriseSize":"LARGE",
                    "enterpriseType":"10",
                    "enterpriseTypeName":None,
                    "institutionRegistCertNumber":None,
                    "financialInstitutionCode":None,
                    "holdingType":"公有控股经济",
                    "holdingTypeName":None,
                    "zhongzhengCode":"122",
                    "currencyName":"人民币",
                    "currency":"CNY",
                    "registeredCapital":"1000.000000",
                    "paidinCapital":"1000.000000",
                    "capitalization":"1000.000000",
                    "revenue":"1000.000000",
                    "establishmentTime":"2023-07-19 00:00:00",
                    "businessLicenseExpirationDate":"2025-07-19 00:00:00",
                    "businessStatus":"01",
                    "businessStatusName":"正常运营",
                    "employeeNumber":"1000",
                    "legalRepresentative":"范怀通",
                    "legalRepresentativeMobile":"13020117356",
                    "legalPersonPhone":"412702199005284111",
                    "actualController":"范怀通",
                    "nationalEconomy":"A",
                    "nationalEconomyName":"广义政府",
                    "listedCompanyLogoName":"A股",
                    "listedCompanyLogo":"A",
                    "resolutionType":"01",
                    "resolutionTypeName":None,
                    "email":"123@163.com",
                    "authId":"1684739301191041026",
                    "shareholdingStructureList":[
                        {
                            "id":"1684745097828220930",
                            "name":"郑福仁",
                            "shareholdingRatio":"39.26",
                            "renterRelationship":"朋友"
                        },
                        {
                            "id":"1684745097798860802",
                            "name":"魏树敏",
                            "shareholdingRatio":"8.43",
                            "renterRelationship":"朋友"
                        },
                        {
                            "id":"1684745097815638018",
                            "name":"石银磊",
                            "shareholdingRatio":"4.68",
                            "renterRelationship":"朋友"
                        },
                        {
                            "id":"1684745097819832321",
                            "name":"杨枫",
                            "shareholdingRatio":"4.16",
                            "renterRelationship":"朋友"
                        },
                        {
                            "id":"1684745097861775361",
                            "name":"张婷婷",
                            "shareholdingRatio":"3.96",
                            "renterRelationship":"朋友"
                        }
                    ],
                    "internationalIndustryType":[
                        "A",
                        "A01",
                        "A011",
                        "A0111"
                    ],
                    "registration":[
                        "110000",
                        "110100",
                        "110101"
                    ]
                }
            ]
        }
    print(jsonpath.jsonpath(res_query,'$..shareholdingStructureList')[0])
    res = api(method = 'POST', url =url,json = data)

'''交易结构-增加'''
def projTradeAdd(projectNo):
    trade = []
    url = 'ifc/api/credit-apply/trades/addProjTrades'
    data = {
        "projectNo": projectNo
    }
    for i in range(8):
        res = api(method='POST', url=url, json=data)
        trade.append(res)
    return trade

'''供应商保存'''
def supplierSave(projectNo,id_1,id_2,id_3,id_4,id_5,id_6,id_7,id_8):
    url = 'ifc/api/credit-apply/trades/saveSupplier'
    list = []
    data_1 = {
        "id": None,
        "projectNo": projectNo,
        "projTradesId": id_1,
        "supplierId": "9821",
        "supplierName": "广州新力供应商公司",
        "certType": "200",
        "certId": "91420117758156711C",
        "artificialPerson": "夏紫文",
        "registerFullAddress": "天津市市辖区和平区，1231321",
        "contacts": None,
        "phone": None,
        "openingBank": None,
        "openingBankNum": None,
        "account": None,
        "accountNo": None,
        "invoiceTitle": None,
        "taxQualification": None,
        "taxId": None,
        "taxTel": None,
        "taxAddress": None,
        "contractType": None,
        "tradeMode": "02",
        "tradeModeName": "货到付款",
        "settleMode": "BankAcceptanceBill",
        "settleModeName": "银行承兑汇票",
        "braceletInstallNode": "BeforePayment",
        "braceletInstallNodeName": "付款前安装",
        "productNodeType": "LS-DFL-I",
        "productNodeTypeName": "直接租赁",
        "isInstallBracelet": 1,
        "isInstallBraceletName": "是",
        "notePeriod": "01",
        "notePeriodName": "60天"
    }
    data_2 = {
        "id": None,
        "projectNo": projectNo,
        "projTradesId": id_2,
        "supplierId": "9822",
        "supplierName": "测试Z500广州伊之密供应商公司",
        "certType": "200",
        "certId": "91320509339101863J",
        "artificialPerson": "夏紫文",
        "registerFullAddress": "北京市市辖区东城区，12313",
        "contacts": None,
        "phone": None,
        "openingBank": None,
        "openingBankNum": None,
        "account": None,
        "accountNo": None,
        "invoiceTitle": None,
        "taxQualification": None,
        "taxId": None,
        "taxTel": None,
        "taxAddress": None,
        "contractType": None,
        "tradeMode": "02",
        "tradeModeName": "货到付款",
        "settleMode": "LetterCredit",
        "settleModeName": "信用证",
        "braceletInstallNode": "BeforePayment",
        "braceletInstallNodeName": "付款前安装",
        "productNodeType": "LS-DFL-I",
        "productNodeTypeName": "直接租赁",
        "isInstallBracelet": 1,
        "isInstallBraceletName": "是",
        "notePeriod": "01",
        "notePeriodName": "60天"
    }
    data_3 = {
        "id": None,
        "projectNo": projectNo,
        "projTradesId": id_3,
        "supplierId": "9820",
        "supplierName": "测试Z500供应商合同公司1",
        "certType": "200",
        "certId": "91320509339101863J",
        "artificialPerson": "夏紫文",
        "registerFullAddress": "北京市市辖区房山区，123123",
        "contacts": None,
        "phone": None,
        "openingBank": None,
        "openingBankNum": None,
        "account": None,
        "accountNo": None,
        "invoiceTitle": None,
        "taxQualification": None,
        "taxId": None,
        "taxTel": None,
        "taxAddress": None,
        "contractType": None,
        "tradeMode": "02",
        "tradeModeName": "货到付款",
        "settleMode": "LetterCredit",
        "settleModeName": "信用证",
        "braceletInstallNode": "BeforePayment",
        "braceletInstallNodeName": "付款前安装",
        "productNodeType": "LS-DFL-I",
        "productNodeTypeName": "直接租赁",
        "isInstallBracelet": 1,
        "isInstallBraceletName": "是",
        "notePeriod": "01",
        "notePeriodName": "60天"
    }
    data_4 = {
        "id": None,
        "projectNo": projectNo,
        "projTradesId": id_4,
        "supplierId": "9820",
        "supplierName": "测试Z500供应商合同公司1",
        "certType": "200",
        "certId": "91320509339101863J",
        "artificialPerson": "夏紫文",
        "registerFullAddress": "北京市市辖区房山区，123123",
        "contacts": None,
        "phone": None,
        "openingBank": None,
        "openingBankNum": None,
        "account": None,
        "accountNo": None,
        "invoiceTitle": None,
        "taxQualification": None,
        "taxId": None,
        "taxTel": None,
        "taxAddress": None,
        "contractType": None,
        "tradeMode": "02",
        "tradeModeName": "货到付款",
        "settleMode": "BankAcceptanceBill",
        "settleModeName": "银行承兑汇票",
        "braceletInstallNode": "BeforePayment",
        "braceletInstallNodeName": "付款前安装",
        "productNodeType": "LS-DFL-I",
        "productNodeTypeName": "直接租赁",
        "isInstallBracelet": 1,
        "isInstallBraceletName": "是",
        "notePeriod": "01",
        "notePeriodName": "60天"
    }
    data_5 = {
        "id": None,
        "projectNo": projectNo,
        "projTradesId": id_5,
        "supplierId": "9820",
        "supplierName": "测试Z500供应商合同公司1",
        "certType": "200",
        "certId": "91320509339101863J",
        "artificialPerson": "夏紫文",
        "registerFullAddress": "北京市市辖区房山区，123123",
        "contacts": None,
        "phone": None,
        "openingBank": None,
        "openingBankNum": None,
        "account": None,
        "accountNo": None,
        "invoiceTitle": None,
        "taxQualification": None,
        "taxId": None,
        "taxTel": None,
        "taxAddress": None,
        "contractType": None,
        "tradeMode": "02",
        "tradeModeName": "货到付款",
        "settleMode": "LetterCredit",
        "settleModeName": "信用证",
        "braceletInstallNode": "BeforePayment",
        "braceletInstallNodeName": "付款前安装",
        "productNodeType": "LS-DFL-I",
        "productNodeTypeName": "直接租赁",
        "isInstallBracelet": 1,
        "isInstallBraceletName": "是",
        "notePeriod": "01",
        "notePeriodName": "60天"
    }
    data_6 = {
        "id": None,
        "projectNo": projectNo,
        "projTradesId": id_6,
        "supplierId": "9836",
        "supplierName": "测试Z500供应商合同公司J1",
        "certType": "200",
        "certId": "91110000FB0RBU0R7P",
        "artificialPerson": "季晓伟",
        "registerFullAddress": "北京市市辖区东城区",
        "contacts": None,
        "phone": None,
        "openingBank": None,
        "openingBankNum": None,
        "account": None,
        "accountNo": None,
        "invoiceTitle": None,
        "taxQualification": None,
        "taxId": None,
        "taxTel": None,
        "taxAddress": None,
        "contractType": None,
        "tradeMode": "02",
        "tradeModeName": "货到付款",
        "settleMode": "BankAcceptanceBill",
        "settleModeName": "银行承兑汇票",
        "braceletInstallNode": "BeforePayment",
        "braceletInstallNodeName": "付款前安装",
        "productNodeType": "LS-DFL-I",
        "productNodeTypeName": "直接租赁",
        "isInstallBracelet": 1,
        "isInstallBraceletName": "是",
        "notePeriod": "01",
        "notePeriodName": "60天"
    }
    data_7 = {
        "id": None,
        "projectNo": projectNo,
        "projTradesId": id_7,
        "supplierId": "9836",
        "supplierName": "测试Z500供应商合同公司J1",
        "certType": "200",
        "certId": "91110000FB0RBU0R7P",
        "artificialPerson": "季晓伟",
        "registerFullAddress": "北京市市辖区东城区",
        "contacts": None,
        "phone": None,
        "openingBank": None,
        "openingBankNum": None,
        "account": None,
        "accountNo": None,
        "invoiceTitle": None,
        "taxQualification": None,
        "taxId": None,
        "taxTel": None,
        "taxAddress": None,
        "contractType": None,
        "tradeMode": "02",
        "tradeModeName": "货到付款",
        "settleMode": "LetterCredit",
        "settleModeName": "信用证",
        "braceletInstallNode": "BeforePayment",
        "braceletInstallNodeName": "付款前安装",
        "productNodeType": "LS-DFL-I",
        "productNodeTypeName": "直接租赁",
        "isInstallBracelet": 1,
        "isInstallBraceletName": "是",
        "notePeriod": "01",
        "notePeriodName": "60天"
    }
    data_8 = {
        "id": None,
        "projectNo": projectNo,
        "projTradesId": id_8,
        "supplierId": "9836",
        "supplierName": "测试Z500供应商合同公司J1",
        "certType": "200",
        "certId": "91110000FB0RBU0R7P",
        "artificialPerson": "季晓伟",
        "registerFullAddress": "北京市市辖区东城区",
        "contacts": None,
        "phone": None,
        "openingBank": None,
        "openingBankNum": None,
        "account": None,
        "accountNo": None,
        "invoiceTitle": None,
        "taxQualification": None,
        "taxId": None,
        "taxTel": None,
        "taxAddress": None,
        "contractType": None,
        "tradeMode": "02",
        "tradeModeName": "货到付款",
        "settleMode": "LetterCredit",
        "settleModeName": "信用证",
        "braceletInstallNode": "BeforePayment",
        "braceletInstallNodeName": "付款前安装",
        "productNodeType": "LS-DFL-I",
        "productNodeTypeName": "直接租赁",
        "isInstallBracelet": 1,
        "isInstallBraceletName": "是",
        "notePeriod": "01",
        "notePeriodName": "60天"
    }
    list.append(data_1)
    list.append(data_2)
    list.append(data_3)
    list.append(data_4)
    list.append(data_5)
    list.append(data_6)
    list.append(data_7)
    list.append(data_8)
    for i in list:
        res = api(method='POST', url=url, json=i)

    # res_1 = api(method='POST', url=url, json=data_1)
    # res_2 = api(method='POST', url=url, json=data_2)
    # res_3 = api(method='POST', url=url, json=data_3)
    # res_4 = api(method='POST', url=url, json=data_4)
    # res_5 = api(method='POST', url=url, json=data_5)
    # res_6 = api(method='POST', url=url, json=data_6)
    # res_7 = api(method='POST', url=url, json=data_7)
    # return res_1,res_2,res_3,res_4,res_5,res_6,res_7

'''查询品牌'''
def pageSerach():
    url = 'ifc/api/proj/pageSearchBrands'
    data = {
        "searchParam": "",
        "current": 1,
        "size": 20
    }
    res = api(method='POST', url=url, json=data)
    return res

'''添加租赁物'''
def leaseSave(projectNo,id):
    res = pageSerach()
    url = 'ifc/api/credit-apply/trades/saveLeasehold'
    data = {
        "projectNo": projectNo,
        "projTradesId": id,
        "tradesLeaseholdList": [{
            "projectNo": "",
            "projTradesId": None,
            "leaseholdName": "测试租赁物1",
            "brandId": jsonpath.jsonpath(res,"$..idArtlBrand")[2],
            "brandFullName": jsonpath.jsonpath(res,"$..brandFullName")[2],
            "spec": "123",
            "leaseholdType": "625304010101",
            "industryClassify": ["A", "A01", "A011"],
            "industryClassifyName": "",
            "industryClassifyOne": "A",
            "industryClassifyOneName": "",
            "industryClassifyTwo": "A01",
            "industryClassifyTwoName": "",
            "price": "1000.00",
            "amount": "1",
            "financeAmt": 100,
            "financeScale": "10.00",
            "bookAmt": "1000.00",
            "isInstallBracelet": 1,
            "isLesseeRegisterAddress": 1,
            "isLesseeTheOwner": 0,
            "ownerType": "",
            "ownerName": "",
            "place": ["110000", "110100", "110101"],
            "placeProvince": "110000",
            "placeProvinceName": "",
            "placeCity": "110100",
            "placeCityName": "",
            "placeDistrict": "110101",
            "placeDistrictName": "",
            "placeDetailAddress": "",
            "directReversalUniqueIdentifier": "",
            "leaseholdTypeList": ["625001000000", "625101010000", "625201010100", "625304010101"],
            "leaseholdTypeOne": "625001000000",
            "leaseholdTypeTwo": "625101010000",
            "leaseholdTypeThree": "625201010100",
            "industryClassifyThree": "A011",
            "brandLevel": "0040",
            "facilityName": "叠纸机"
        }]
    }
    res = api(method='POST', url=url, json=data)

'''查询融资信息'''
def financeQuery(projectNo,projTradesId):
    url = 'ifc/api/credit-apply/trades/queryFinanceInfo'
    data = {
        "projectNo": projectNo,
        "projTradesId": projTradesId
    }
    res = api(method='POST', url=url, json=data)

    return res

'''租金测算'''
def rentCalc(projectNo,projTradesId,id):
    url = 'ifc/api/credit-apply/trades/rentCalc'
    data = {
        "projectNo": projectNo,
        "projTradesId": projTradesId,
        "id": id,
        "rateAppearMode": "Implication",
        "rateAppearModeName": "隐含利率",
        "lprBaseRate": None,
        "rentRate": None,
        "bpFloatValue": None,
        "preditRentDate": "2023-07-19",
        "financeTerm": 12,
        "yearPaymentTimes": "12",
        "totalPaymentTimes": "12",
        "financeTotalAmt": 100,
        "totalBookAmt": "1000.00",
        "financingPaymentDirection": "Supplier",
        "financingPaymentDirectionName": "供应商",
        "isExistDownPayment": 1,
        "isExistDownPaymentName": "是",
        "downPaymentCalcMode": "FIX_AMOUNT",
        "downPaymentCalcModeName": "固定金额",
        "downPaymentRatio": 0.9,
        "downPaymentAmt": 900,
        "downPaymentPayDirection": "OurCompany",
        "downPaymentPayDirectionName": None,
        "isExistMargin": 0,
        "isExistMarginName": None,
        "marginCalcMode": None,
        "marginCalcModeName": None,
        "marginRatio": None,
        "marginAmt": None,
        "marginDeductMode": None,
        "marginDeductModeName": None,
        "retentionPriceAmt": "100.00",
        "discountAmt": None,
        "firstTermAmt": None,
        "rentalMode": "Postpay",
        "rentalModeName": None,
        "rentCalcMode": "EquivalentRent",
        "rentCalcModeName": None,
        "rentAmt": "10",
        "quickPaymentAmt": None,
        "rentTotalAmt": None,
        "interestTotalAmt": None,
        "recoveryPrincipalTotalAmt": None,
        "incomeTotalAmt": None,
        "xirrRate": None,
        "xirrPureRate": None,
        "irrRate": None,
        "irrPureRate": None,
        "financeSegmentList": [],
        "repayScheduleList": []
    }
    res = api(method='POST', url=url, json=data)
    return res

'''融资信息'''
def rentSave(projectNo,projTradesId):
    res = financeQuery(projectNo,projTradesId)
    id = jsonpath.jsonpath(res,'$..id')[0]
    rentCalc(projectNo,projTradesId,id)
    url = 'ifc/api/credit-apply/trades/rentSave'
    data = {
        "projectNo": projectNo,
        "projTradesId": projTradesId,
        "id": id,
        "rateAppearMode": "Implication",
        "rateAppearModeName": "隐含利率",
        "lprBaseRate": "3.65",
        "rentRate": 0.34390000000000004,
        "bpFloatValue": 0,
        "preditRentDate": "2023-08-19",
        "financeTerm": 12,
        "yearPaymentTimes": "12",
        "totalPaymentTimes": "12",
        "financeTotalAmt": 100,
        "totalBookAmt": "1000.00",
        "financingPaymentDirection": "Supplier",
        "financingPaymentDirectionName": "供应商",
        "isExistDownPayment": 1,
        "isExistDownPaymentName": "是",
        "downPaymentCalcMode": "FIX_AMOUNT",
        "downPaymentCalcModeName": "固定金额",
        "downPaymentRatio": 0.9,
        "downPaymentAmt": 900,
        "downPaymentPayDirection": "OurCompany",
        "downPaymentPayDirectionName": None,
        "isExistMargin": 0,
        "isExistMarginName": None,
        "marginCalcMode": None,
        "marginCalcModeName": None,
        "marginRatio": None,
        "marginAmt": None,
        "marginDeductMode": None,
        "marginDeductModeName": None,
        "retentionPriceAmt": "100.00",
        "discountAmt": None,
        "firstTermAmt": None,
        "rentalMode": "Postpay",
        "rentalModeName": None,
        "rentCalcMode": "EquivalentRent",
        "rentCalcModeName": None,
        "rentAmt": "10.00",
        "quickPaymentAmt": None,
        "rentTotalAmt": None,
        "interestTotalAmt": None,
        "recoveryPrincipalTotalAmt": None,
        "incomeTotalAmt": None,
        "xirrRate": None,
        "xirrPureRate": None,
        "irrRate": None,
        "irrPureRate": None,
        "financeSegmentList": [],
        "repayScheduleList": []
    }
    res = api(method='POST', url=url, json=data)

'''评估主体类型'''
def evaluationSubjectQuery(projectNo):
    url = 'ifc/api/risk-info/queryEvaluationSubjectBase'
    data = {
        "projectNo": projectNo,
        "roleType": "1"
    }
    res = api(method='POST', url=url, json=data)
    return res

'''评估主体保存'''
def evaluationSubjectSave(projectNo):
    res = evaluationSubjectQuery(projectNo)
    url = 'ifc/api/risk-info/saveEvaluationSubject'
    data = {
        "id": None,
        "projectNo": projectNo,
        "evaluationSubjectId": jsonpath.jsonpath(res,'$..evaluationSubjectId')[0],
        "evaluationSubjectType": "1",
        "evaluationSubjectTypeName": jsonpath.jsonpath(res,'$..evaluationSubjectName')[0],
        "evaluationSubjectName": None,
        "generalScore": None,
        "scheme": None,
        "riskScoreItemMap": {
            "depositGt5timesRent6Mon": 0,
            "houseProperty": 0,
            "loansAndConsume6mGe3": 0,
            "businessTeam60AndOverdueRateOver2Percent": 0,
            "personDishonestExecutee": 0
        },
        "scoreConfigList": [{
            "id": None,
            "projectNo": projectNo,
            "scoreItemCode": "houseProperty",
            "scoreItemName": "房产（单价超1万，且净值覆盖敞口）",
            "elementValue": "是",
            "ratingScore": 1
        }, {
            "id": None,
            "projectNo": projectNo,
            "scoreItemCode": "houseProperty",
            "scoreItemName": "房产（单价超1万，且净值覆盖敞口）",
            "elementValue": "否",
            "ratingScore": 0
        }, {
            "id": None,
            "projectNo": projectNo,
            "scoreItemCode": "depositGt5timesRent6Mon",
            "scoreItemName": "近6个月内日均存款余额大于最高租金5倍",
            "elementValue": "是",
            "ratingScore": 1
        }, {
            "id": None,
            "projectNo": projectNo,
            "scoreItemCode": "depositGt5timesRent6Mon",
            "scoreItemName": "近6个月内日均存款余额大于最高租金5倍",
            "elementValue": "否",
            "ratingScore": 0
        }, {
            "id": None,
            "projectNo": projectNo,
            "scoreItemCode": "personDishonestExecutee",
            "scoreItemName": "当前未决诉讼达20万或2年内曾失信限高等",
            "elementValue": "是",
            "ratingScore": -1
        }, {
            "id": None,
            "projectNo": projectNo,
            "scoreItemCode": "personDishonestExecutee",
            "scoreItemName": "当前未决诉讼达20万或2年内曾失信限高等",
            "elementValue": "否",
            "ratingScore": 0
        }, {
            "id": None,
            "projectNo": projectNo,
            "scoreItemCode": "loansAndConsume6mGe3",
            "scoreItemName": "近六个月小贷、消费类金融查询超3次（含）",
            "elementValue": "是",
            "ratingScore": -1
        }, {
            "id": None,
            "projectNo": projectNo,
            "scoreItemCode": "loansAndConsume6mGe3",
            "scoreItemName": "近六个月小贷、消费类金融查询超3次（含）",
            "elementValue": "否",
            "ratingScore": 0
        }, {
            "id": None,
            "projectNo": projectNo,
            "scoreItemCode": "businessTeam60AndOverdueRateOver2Percent",
            "scoreItemName": "业务团队60+逾期率超2%",
            "elementValue": "是",
            "ratingScore": -2
        }, {
            "id": None,
            "projectNo": projectNo,
            "scoreItemCode": "businessTeam60AndOverdueRateOver2Percent",
            "scoreItemName": "业务团队60+逾期率超2%",
            "elementValue": "否",
            "ratingScore": 0
        }],
        "scoreItemVMList": [{
            "elementValue": "50万（含）以下",
            "ratingScore": 5,
            "scoreItemCode": "applyQuota",
            "scoreItemName": "申请额度"
        }, {
            "elementValue": "C及以下，70%",
            "ratingScore": 1,
            "scoreItemCode": "brandLevel",
            "scoreItemName": "设置品牌等级"
        }]
    }
    res = api(method='POST', url=url, json=data)

'''授信要素查询'''
def creditElementQuery(projectNo):
        url = 'ifc/api/risk-info/queryCreditElement'
        data = {
            "projectNo": projectNo
        }
        res = api(method='POST', url=url, json=data)
        return res

'''授信要素'''
def creditElementSave(projectNo):
    res = custEnterpriseQuery(projectNo)
    url = 'ifc/api/risk-info/saveCreditElement'
    data ={
        "projectNo": projectNo,
        "custRelatedList": [],
        "shareholderStructureList": [],
        "projCustEnterpriseIncomeVerification": {
            "id": None,
            "confirmableIncome": "100",
            "currentYearIncome": "100.00",
            "previousYearIncome": "100.00",
            "projectNo": None
        },
        "bankStatementList": [],
        "electricChargeList": [{
            "billDate": "2023-07",
            "billAmount": "10.00"
        }, {
            "billDate": "2023-06",
            "billAmount": "10.00"
        }, {
            "billDate": "2023-05",
            "billAmount": "10.00"
        }, {
            "billDate": "2023-04",
            "billAmount": "10.00"
        }, {
            "billDate": "2023-03",
            "billAmount": "10.00"
        }, {
            "billDate": "2023-02",
            "billAmount": "10.00"
        }],
        "rigidLiabilityList": [{
            "customerType": "1",
            "liabilityType": "BankLoan",
            "belongingCompanyId": jsonpath.jsonpath(res,"$..id")[0],
            "rigidLiabilityAmount": "10.00",
            "mortgageLiabilityAmount": "10.00"
        }],
        "totalAmount": 10,
        "recentElecDate": "2023-07"
    }
    res = api(method='POST', url=url, json=data)

'''准入要求'''
def accessRquirementSave(projectNo):
    url = 'ifc/api/risk-info/saveAccessRequirement'
    data = {
            "projectNo": projectNo,
            "list": [{
                "accessItemCode": "",
                "arSubTypeName": "其他",
                "arDesc": "其他",
                "comment": "其他",
                "projectNo": projectNo,
                "arCode": "ar6",
                "arSubCode": "arSub16"
            }]
        }
    res = api(method='POST', url=url, json=data)

'''影像信息'''
def attachmentSave(projectNo,fileId,fileName,subCategoryCode):
    url = 'ifc/api/attachment/saveFileRelation'
    data = {
        "fileId": fileId,
        "fileName": fileName,
        "subCategoryCode": subCategoryCode,
        "isUpdate": True,
        "code": "projectCreditApproval",
        "businessKey": projectNo,
        "businessType": "PROJECT"
    }
    res = api(method='POST', url=url, json=data)

'''影像信息下一步校验'''
def attachmentNextStep(projectNo):
    url = 'ifc/api/attachment/nextStep'
    data = {
        "businessKey": projectNo,
        "templateCode": "projectCreditApproval"
    }
    res = api(method='POST', url=url, json=data)

'''补充资料'''
def reqTextSave(projectNo):
    url = 'ifc/api/risk-info/saveReqTextItem'
    data = {
        "partnerInfoList": [],
        "workshopType": "1",
        "isExistEstate": 0,
        "estateInfoCommand": {
            "estateNum": "",
            "isExistMortgage": 1,
            "marketValueApprox": "",
            "netValue": "",
            "estateBelonger": ""
        },
        "workshopInfoVm": {
            "landArea": "100",
            "floorArea": "100",
            "marketValueApprox": "100",
            "leaseTerm": "",
            "yearlyRental": ""
        },
        "entIncomeScaleApprox": "100",
        "entIncomeScaleApproxLy": "100",
        "fluctuationCause": "说明原因",
        "equipmentName": "设备名称",
        "equipmentTotal": "10",
        "stageEquipmentTotal": "10",
        "projAdvantage": "项目优势",
        "projDisadvantage": "项目劣势",
        "abnormalSlowReleaseCondition": "缓释条件",
        "supplementaryContent": "其他补充",
        "projectNo": projectNo
    }
    res = api(method='POST', url=url, json=data)

def detectorExec(itemCode,taskid):
    url = 'ifc/api/common/detector/exec'
    data = {
        "detectorCode": "project_credit:auditApply",
        "itemCode": itemCode,
        "taskId": taskid
        }
    res = api(method='POST', url=url, json=data)

def index(request):
    return HttpResponse("Hello world !  django ~~")

def demo(request):
    return render(request, 'demo.html')

# 测试QQ号访问页面
def test_qq(request):
    return render(request, 'get_demo.html')

# 提交后返回页面
def result_qq(request):
    global url
    headers = {"Cookie": "access_token=5ebac3c5-61d3-4b0e-9fa1-b2a9eebd730a"}
    projectNo = request.GET["id"]
    url = url + 'ifc/api/credit-auth/project/query/detail?projectNo=%s'%projectNo
    print(url)
    res = requests.request("GET", url, verify=True, headers=headers).json()
    result = {
        "code": 20000,
        "status": True,
        "message": "success",
        "data": res["data"]
    }
    return JsonResponse(result)



'''新建Z500'''
def add_pr(request):
    start_time = time.time()
    global headers_uat
    custName = request.GET["custName"]
    res = login(custName)
    headers_uat = {"AccessToken": res["access_token"]}
    lesaseName = request.GET["lesaseName"]

    # projectNo = 'PJ202308030008'
    # #
    res = add_pro(lesaseName)
    projectNo = res["data"]["projectNo"]
    '''征信授权'''
    creditAuthSave(projectNo)
    creditAuthBack(projectNo)
    '''预审提交'''
    res = proSubmit(projectNo)
    taskId = jsonpath.jsonpath(res,'$..taskId')[0]
    opinionSumit(taskId)
    print("风控预审中")
    time.sleep(60)
    while True:
        count = 0
        res = pro_page()
        for i in res["data"]["records"]:
            if i["projectNo"] == projectNo:
                if i["statusName"] == "待授信申请":
                    count = 1
                    break;
        if count == 1:
            break;
    '''授信-客户信息'''
    custEnterpriseSave(projectNo)
    custEnterpriseRelateSave(projectNo)

    # '''交易结构'''
    projTrades = []
    for i in projTradeAdd(projectNo):
        # res_trade = projTradeAdd(projectNo)
        projTradesId = jsonpath.jsonpath(i, '$..id')[0]
        projTrades.append(projTradesId)
    '''供应商'''
    supplierSave(projectNo, projTrades[0],projTrades[1],projTrades[2],projTrades[3],projTrades[4],projTrades[5],projTrades[6],projTrades[7])
    for i in projTrades:
        '''租赁物'''
        leaseSave(projectNo, i)
        '''融资信息'''
        rentSave(projectNo, i)
    '''风险信息'''
    '''评估主体'''
    evaluationSubjectSave(projectNo)
    '''授信要素'''
    creditElementSave(projectNo)
    '''准入要求'''
    accessRquirementSave(projectNo)
    '''影像信息'''
    file = [{
        "fileId": "603584879892357120",  # 地图厂房证或厂房租赁合同
        "fileName": "mmexport1689754224318.jpg",
        "subCategoryCode": "contractOfEstateOrLease"
    },
        {
            "fileId": "603585308428591104",  # 电费缴费凭证
            "fileName": "mmexport1689754227145.jpg",
            "subCategoryCode": "billsOfElectric"
        },
        {
            "fileId": "603585498497671168",  # 尽调照片
            "fileName": "mmexport1689754230008.jpg",
            "subCategoryCode": "dueDiligencePhotos"
        },
        {
            "fileId": "603585669293924352",  # 公司章程
            "fileName": "mmexport1689754235448.jpg",
            "subCategoryCode": "articlesOfAssociationLessee"
        },
        {
            "fileId": "605424487122853888",  # 新力租赁设备采购合同
            "fileName": "mmexport1690616408068.jpg",
            "subCategoryCode": "rentalEquipProcurementContract_9821"
        },
        {
            "fileId": "605425274645372928",  # 伊之密租赁设备采购合同
            "fileName": "mmexport1690616619857.jpg",
            "subCategoryCode": "rentalEquipProcurementContract_9822"
        },
        {
            "fileId": "605425386654261248",  # 合同公司1租赁设备采购合同
            "fileName": "mmexport1690616406693.jpg",
            "subCategoryCode": "rentalEquipProcurementContract_9820"
        }
        ,
        {
            "fileId": "606207196724191232",  # 合同公司J1租赁设备采购合同
            "fileName": "mmexport1690803025832.jpg",
            "subCategoryCode": "rentalEquipProcurementContract_9836"
        }
    ]
    for i in file:
        attachmentSave(projectNo,i["fileId"],i["fileName"],i["subCategoryCode"])
    attachmentNextStep(projectNo)
    reqTextSave(projectNo)

    # '''风险探测'''
    # res_taskid = getPro(projectNo)
    # taskid = jsonpath.jsonpath(res_taskid, '$..taskId')[0]
    # exec = ["authLetterValidDate", "supplierQuota", "antiTerrorism", "relatedPartyQueries", "financingAmount",
    #         "projectAmtEvaluateSubject", "totalRecoveryPrincipal", "leaseQuota"]
    # for i in exec:
    #     detectorExec(i, taskid)
    # '''提交审核'''
    # opinionSumit(taskid)

    end_time = time.time()
    run_time = round(end_time - start_time,2)

    result = {
        "code": 200,
        "status": True,
        "message": 'success,耗时%ss,打开app项目列表查看新建项目！！！'% run_time,
        "data": "项目编号：%s" %projectNo
    }

    # return HttpResponse("提交成功,打开app项目列表查看新建项目！！！")
    return JsonResponse(result,json_dumps_params={'ensure_ascii':False})


