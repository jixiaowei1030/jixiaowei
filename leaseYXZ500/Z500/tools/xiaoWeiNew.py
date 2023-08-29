from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from Z500.tools import test_data
from Z500.common.login import login
from Z500.models import Test
from Z500.models import Sys_param_config
from Z500.models import Auth_group
from Z500.tools.dingtalk import send_notify



import time
import requests
import jsonpath
import datetime


class xiaoWeiNew():

    def __init__(self, headers):
        self.headers = headers
        self.url = 'https://test-vrip.msfl.com.cn/'
        self.req = requests.session()

    def api(self,**kwargs):

        retries = Retry(total=2,
                        status_forcelist=[400, 500, 502, 503, 504])
        url = self.url +kwargs.get("url")
        kwargs.pop("url")
        self.req.mount('http://', HTTPAdapter(max_retries=retries))
        self.req.mount('https://', HTTPAdapter(max_retries=retries))

        try:
            res = self.req.request(url =url, verify=False, headers=self.headers, **kwargs).json()
            print(url,res)
            return res
        except Exception as e:
            print("发生异常：", str(e))
            time.sleep(30)
            res = self.req.request(url=url, verify=False, headers=self.headers, **kwargs).json()
            print(url, res)
            return res

    def updateHeader(self,custName):
        res = login(custName)
        headers = {"AccessToken": res["access_token"]}
        self.headers = headers

    def add_pro(self,lesaseName):
        '''新建项目'''
        url = 'ifc/api/credit-auth/createProj?leaseName=%s' % lesaseName
        res = self.api(method="GET", url=url)
        return res

    def pro_page(self):
        url = 'ifc/api/credit-auth/project/page'
        data = {
                "current": 1,
                "size": 20,
                "leaseName": "",
                "statusCode": "000000"
            }
        res = self.api(method ="POST", url=url,  json = data)
        return res

    def preQuery(self,projectNo):
        '''预审初始化'''
        url = 'ifc/api/pre-approval/init?projectNo=%s'%projectNo
        res = self.api(method = "GET", url = url)
        return res

    def getPro(self,projectNo):
        url = 'ifc/api/credit-auth/project/query/detail?projectNo=%s'%projectNo
        res = self.api(method ="GET", url=url)
        return res

    def creditAuthSave(self,projectNo,custName,guarantor):
        '''创建征信授权'''
        url = 'https://test-asp.msfl.com.cn/asp/ifc/notice/credit-auth/save'

        retries = Retry(total=2,
                        status_forcelist=[400, 500, 502, 503, 504])
        req =requests.session()
        req.mount('http://', HTTPAdapter(max_retries=retries))
        req.mount('https://', HTTPAdapter(max_retries=retries))

        data = test_data.getAuthData(projectNo,custName,guarantor)
        for i in data:
            try:
                res = req.request(method='POST', url=url, json=i,verify=False, headers=self.headers)
                time.sleep(1)
            except:
                time.sleep(30)
                res = req.request(method='POST', url=url, json=i, verify=False, headers=self.headers)
                time.sleep(1)

    def creditAuthBack(self,projectNo,custName,guarantor):
        '''征信授权完成'''
        url = 'https://test-asp.msfl.com.cn/asp/ifc/notice/credit-auth/signOffCallback'
        retries = Retry(total=2,
                        status_forcelist=[400, 500, 502, 503, 504])
        req = requests.session()
        req.mount('http://', HTTPAdapter(max_retries=retries))
        req.mount('https://', HTTPAdapter(max_retries=retries))

        data = test_data.getBackData(projectNo,custName,guarantor)
        for i in data:
            try:
                res = req.request(method='POST', url=url, json=i,verify=False, headers=self.headers)
            except:
                time.sleep(30)
                res = req.request(method='POST', url=url, json=i,verify=False, headers=self.headers)


    def taskCompleteInit(self,taskid):
        '''初始化流程'''
        url = 'ifc/api/flow/task-complete/init?taskId=%s'%taskid
        res = self.api(method='GET', url=url)
        return res

    def proSubmit(self,projectNo,guarantor):
        '''预审提交'''
        url = 'ifc/api/pre-approval/submit'
        res_query = self.preQuery(projectNo)
        if guarantor == '1':
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
        else:
            data = {
                "projectNo": projectNo,
                "customerList": [
                    {
                        "id": jsonpath.jsonpath(res_query, '$..id')[0],
                        "creditCustomerType": jsonpath.jsonpath(res_query, '$..creditCustomerType')[0],
                        "creditCustomerTypeName": jsonpath.jsonpath(res_query, '$..creditCustomerTypeName')[0],
                        "creditCustomerName": jsonpath.jsonpath(res_query, '$..creditCustomerName')[0],
                        "creditCustomerNo": jsonpath.jsonpath(res_query, '$..creditCustomerNo')[0],
                        "creditCustomerIdType": jsonpath.jsonpath(res_query, '$..creditCustomerIdType')[0],
                        "creditCustomerIdTypeName": jsonpath.jsonpath(res_query, '$..creditCustomerIdTypeName')[0],
                        "roleType": "6"
                    },
                    {
                        "id": jsonpath.jsonpath(res_query, '$..id')[1],
                        "creditCustomerType": jsonpath.jsonpath(res_query, '$..creditCustomerType')[1],
                        "creditCustomerTypeName": jsonpath.jsonpath(res_query, '$..creditCustomerTypeName')[1],
                        "creditCustomerName": jsonpath.jsonpath(res_query, '$..creditCustomerName')[1],
                        "creditCustomerNo": jsonpath.jsonpath(res_query, '$..creditCustomerNo')[1],
                        "creditCustomerIdType": jsonpath.jsonpath(res_query, '$..creditCustomerIdType')[1],
                        "creditCustomerIdTypeName": jsonpath.jsonpath(res_query, '$..creditCustomerIdTypeName')[1],
                        "roleType": "1"
                    }
                ],
                "productType": "LS-DFL",
                "productNo": "LeaseYXZ300"
            }

        res = self.api(method ="POST", url=url,  json = data)
        return res_query

    def opinionSumit(self,taskId):
        res = self.taskCompleteInit(taskId)
        if not res["data"]["remind"]:
            remind = '测试同意'
        else:
            remind = res["data"]["remind"]
        '''提交审批意见'''
        url = 'ifc/api/flow/task-complete'
        data = {
                "remind": remind,
                "taskId": taskId
            }
        time.sleep(3)
        res = self.api(method = 'POST', url =url,json = data)

    def custEnterpriseQuery(self,projectNo):
        '''客户信息-承租人-查询'''
        url = 'ifc/api/proj_cust_enterprise_info/queryByCondition'
        data = {
            "projectNo": projectNo
        }
        res = self.api(method = 'POST', url =url,json = data)
        return res

    def custEnterpriseSave(self,projectNo):
        '''客户信息-承租人-保存'''
        res_query = self.custEnterpriseQuery(projectNo)
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
                "phoneNumber": jsonpath.jsonpath(res_query,'$..phoneNumber')[0],
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
                "rentStockholderRelated": False,
                "rentRelated": False,
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
                "legalRepresentative": jsonpath.jsonpath(res_query,'$..legalRepresentative')[0],
                "legalRepresentativeMobile": jsonpath.jsonpath(res_query,'$..legalRepresentativeMobile')[0],
                "legalPersonPhone": jsonpath.jsonpath(res_query,'$..legalPersonPhone')[0],
                "actualController": jsonpath.jsonpath(res_query,'$..actualController')[0],
                "nationalEconomy": "A",
                "nationalEconomyName": "广义政府",
                "listedCompanyLogo": "A",
                "listedCompanyLogoName": "A股",
                "resolutionType": jsonpath.jsonpath(res_query,'$..resolutionType')[0],
                "resolutionTypeName": jsonpath.jsonpath(res_query,'$..resolutionTypeName')[0],
                "email": "123@163.com",
                "registration": ["110000", "110100", "110101"],
                "industryType": ["A", "A01"],
                "office": ["110000", "110100", "110101"],
                "actualBusiness": ["110000", "110100", "110101"],
                "internationalIndustryType": ["A", "A01", "A011", "A0111"],
                "licProjectInvestment": ["A", "A01", "A011", "A0111"],
                "shareholdingStructureList": []
            }
        res = self.api(method = 'POST', url =url,json = data)

    def custEnterpriseRelatedQuery(self,projectNo):
        '''客户信息-关键人-查询'''
        url = 'ifc/api/proj_cust_enterprise_related_info/queryByCondition'
        data = {
            "projectNo": projectNo
        }
        res = self.api(method = 'POST', url =url,json = data)
        return res

    def creditQuery(self,projectNo):
        '''客户信息-受益人-查询'''
        url = 'ifc/api/credit-auth/queryList'
        data = {
                "customerName": "",
                "projectNo": projectNo,
                "isUse": 1,
                "creditAuthStatus": 1,
                "creditCustomerType": "IND"
            }
        res = self.api(method = 'POST', url =url,json = data)
        return res

    def custEnterpriseRelateSave(self,projectNo,guarantor):
        '''客户信息-关键人-保存'''
        res_query = self.custEnterpriseRelatedQuery(projectNo)
        res_credit =self.creditQuery(projectNo)
        url = 'ifc/api/proj_cust_enterprise_related_info/edit'
        if guarantor == '2':
            data = {
                "projectNo": projectNo,
                "actualController": {
                    "id": jsonpath.jsonpath(res_query,'$..actualController.id')[0],
                    "projectNo": projectNo,
                    "sourceId": jsonpath.jsonpath(res_query,'$..actualController.sourceId')[0],
                    "enterpriseInfoId": jsonpath.jsonpath(res_query,'$..actualController.enterpriseInfoId')[0],
                    "roleType": "6",
                    "resolutionType": None,
                    "resolutionTypeName":None,
                    "name": jsonpath.jsonpath(res_query,'$..actualController.name')[0],
                    "idCardType": jsonpath.jsonpath(res_query,'$..actualController.idCardType')[0],
                    "idCardTypeName": jsonpath.jsonpath(res_query,'$..actualController.idCardTypeName')[0],
                    "idCardNo": jsonpath.jsonpath(res_query,'$..actualController.idCardNo')[0],
                    "mobile": jsonpath.jsonpath(res_query,'$..actualController.mobile')[0],
                    "shareholdingRatio": None,
                    "renterRelationship": None,
                    "residenceAddress": None,
                    "creditReportTime": None,
                    "authId": jsonpath.jsonpath(res_query,'$..actualController.authId')[0],
                    "idProvince": "110000",
                    "idProvinceName": None,
                    "idCity": "110100",
                    "idCityName": None,
                    "idLocation": "110101",
                    "idLocationName": None,
                    "idAddress": "上海",
                    "idArray": ["110000", "110100", "110101"]
                },
                "legalRepresentative": {
                    "id": jsonpath.jsonpath(res_query,'$..legalRepresentative.id')[0],
                    "projectNo": projectNo,
                    "sourceId": jsonpath.jsonpath(res_query,'$..legalRepresentative.sourceId')[0],
                    "enterpriseInfoId": jsonpath.jsonpath(res_query,'$..legalRepresentative.enterpriseInfoId')[0],
                    "roleType": "4",
                    "resolutionType": None,
                    "resolutionTypeName": None,
                    "name": jsonpath.jsonpath(res_query,'$..legalRepresentative.name')[0],
                    "idCardType": jsonpath.jsonpath(res_query,'$..legalRepresentative.idCardType')[0],
                    "idCardTypeName": jsonpath.jsonpath(res_query,'$..legalRepresentative.idCardTypeName')[0],
                    "idCardNo": jsonpath.jsonpath(res_query,'$..legalRepresentative.idCardNo')[0],
                    "mobile": jsonpath.jsonpath(res_query,'$..legalRepresentative.mobile')[0],
                    "shareholdingRatio": None,
                    "renterRelationship": None,
                    "residenceAddress": None,
                    "creditReportTime": None,
                    "authId": jsonpath.jsonpath(res_query,'$..legalRepresentative.authId')[0],
                    "idProvince": "110000",
                    "idProvinceName": None,
                    "idCity": "110100",
                    "idCityName": None,
                    "idLocation": "110101",
                    "idLocationName": None,
                    "idAddress": "上海",
                    "idArray": ["110000", "110100", "110101"]
                },
                "beneficiary": {
                    "authId": jsonpath.jsonpath(res_credit,'$..id')[0],
                    "name": jsonpath.jsonpath(res_credit,'$..creditCustomerName')[0],
                    "idCardNo": jsonpath.jsonpath(res_credit,'$..creditCustomerNo')[0],
                    "idCardType": jsonpath.jsonpath(res_credit,'$..creditCustomerIdType')[0],
                    "idCardTypeName": jsonpath.jsonpath(res_credit,'$..creditCustomerIdTypeName')[0],
                    "residenceAddress": jsonpath.jsonpath(res_credit,'$..creditCustomerAddress')[0],
                    "idArray": ["110000", "110100", "110101"],
                    "idProvince": "110000",
                    "idCity": "110100",
                    "idLocation": "110101"
                },
                "personalIds": [],
                "custEnterpriseIds": [],
                "personalInfoModels":[],
                "projCustEnterpriseVMList":[]
            }
        elif guarantor == '1':
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
                    "mobile": jsonpath.jsonpath(res_query,'$..actualController.mobile')[0],
                    "shareholdingRatio": None,
                    "renterRelationship": None,
                    "residenceAddress": None,
                    "creditReportTime": None,
                    "authId": jsonpath.jsonpath(res_query,'$..actualController.authId')[0],
                    "idProvince": "110000",
                    "idProvinceName": "北京市",
                    "idCity": "110100",
                    "idCityName": "市辖区",
                    "idLocation": "110101",
                    "idLocationName": "东城区",
                    "idAddress": "上海",
                    "idArray": ["110000", "110100", "110101"]
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
                    "mobile": jsonpath.jsonpath(res_query,'$..legalRepresentative.mobile')[0],
                    "shareholdingRatio": None,
                    "renterRelationship": None,
                    "residenceAddress": None,
                    "creditReportTime": None,
                    "authId": jsonpath.jsonpath(res_query,'$..legalRepresentative.authId')[0],
                    "idProvince": "110000",
                    "idProvinceName": "北京市",
                    "idCity": "110100",
                    "idCityName": "市辖区",
                    "idLocation": "110101",
                    "idLocationName": "东城区",
                    "idAddress": "上海",
                    "idArray": ["110000", "110100", "110101"]
                },
                "beneficiary": {
                        "authId": jsonpath.jsonpath(res_credit,'$..id')[0],
                        "name": jsonpath.jsonpath(res_credit,'$..creditCustomerName')[0],
                        "idCardNo": jsonpath.jsonpath(res_credit,'$..creditCustomerNo')[0],
                        "idCardType": jsonpath.jsonpath(res_credit,'$..creditCustomerIdType')[0],
                        "idCardTypeName": jsonpath.jsonpath(res_credit,'$..creditCustomerIdTypeName')[0],
                        "residenceAddress": jsonpath.jsonpath(res_credit,'$..creditCustomerAddress')[0],
                        "idArray": ["110000", "110100", "110101"],
                        "idProvince": "110000",
                        "idCity": "110100",
                        "idLocation": "110101"
                },
                "personalIds": [],
                "custEnterpriseIds": [],
                "personalInfoModels":[
                    {
                        "id":res_query["data"]["personalInfoModels"][0]["id"],
                        "projectNo": projectNo,
                        "projectCustomerInfoId": res_query["data"]["personalInfoModels"][0]["projectCustomerInfoId"],
                        "sourceId":res_query["data"]["personalInfoModels"][0]["sourceId"],
                        "roleType":res_query["data"]["personalInfoModels"][0]["roleType"],
                        "name":res_query["data"]["personalInfoModels"][0]["name"],
                        "idCardType":res_query["data"]["personalInfoModels"][0]["idCardType"],
                        "idCardTypeName":res_query["data"]["personalInfoModels"][0]["idCardTypeName"],
                        "idCardNo":res_query["data"]["personalInfoModels"][0]["idCardNo"],
                        "mobile":res_query["data"]["personalInfoModels"][0]["mobile"],
                        "country":"156",
                        "countryName":None,
                        "actualControllerRelationship":"director",
                        "actualControllerRelationshipName":None,
                        "maritalStatus":"MARRIED",
                        "maritalStatusName":None,
                        "gender":"1",
                        "genderName":None,
                        "birthDate":"1980-07-28",
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
                        "idAddress":res_query["data"]["personalInfoModels"][0]["idAddress"],
                        "creditReportTime":None,
                        "email":"666@163.com",
                        "authId":res_query["data"]["personalInfoModels"][0]["authId"],
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
                        "roleType":res_query["data"]["projCustEnterpriseVMList"][0]["roleType"],
                        "name":res_query["data"]["projCustEnterpriseVMList"][0]["name"],
                        "idCardType":res_query["data"]["projCustEnterpriseVMList"][0]["idCardType"],
                        "idCardTypeName":res_query["data"]["projCustEnterpriseVMList"][0]["idCardTypeName"],
                        "idCardNo":res_query["data"]["projCustEnterpriseVMList"][0]["idCardNo"],
                        "mobile":None,
                        "country":res_query["data"]["projCustEnterpriseVMList"][0]["country"],
                        "countryName":res_query["data"]["projCustEnterpriseVMList"][0]["countryName"],
                        "interIndustryClassifyOneName":res_query["data"]["projCustEnterpriseVMList"][0]["interIndustryClassifyOneName"],
                        "interIndustryClassifyOne":res_query["data"]["projCustEnterpriseVMList"][0]["interIndustryClassifyOne"],
                        "interIndustryClassifyTwoName":res_query["data"]["projCustEnterpriseVMList"][0]["interIndustryClassifyTwoName"],
                        "interIndustryClassifyTwo":res_query["data"]["projCustEnterpriseVMList"][0]["interIndustryClassifyTwo"],
                        "interIndustryClassifyThreeName":res_query["data"]["projCustEnterpriseVMList"][0]["interIndustryClassifyThreeName"],
                        "interIndustryClassifyThree":res_query["data"]["projCustEnterpriseVMList"][0]["interIndustryClassifyThree"],
                        "interIndustryClassifyFourName":res_query["data"]["projCustEnterpriseVMList"][0]["interIndustryClassifyFourName"],
                        "interIndustryClassifyFour":res_query["data"]["projCustEnterpriseVMList"][0]["interIndustryClassifyFour"],
                        "industryClassifyOneName":res_query["data"]["projCustEnterpriseVMList"][0]["industryClassifyOneName"],
                        "industryClassifyOne":res_query["data"]["projCustEnterpriseVMList"][0]["industryClassifyOne"],
                        "industryClassifyTwoName":res_query["data"]["projCustEnterpriseVMList"][0]["industryClassifyTwoName"],
                        "industryClassifyTwo":res_query["data"]["projCustEnterpriseVMList"][0]["industryClassifyTwo"],
                        "registrationProvinceName":res_query["data"]["projCustEnterpriseVMList"][0]["registrationProvinceName"],
                        "registrationProvince":res_query["data"]["projCustEnterpriseVMList"][0]["registrationProvince"],
                        "registrationCityName":res_query["data"]["projCustEnterpriseVMList"][0]["registrationCityName"],
                        "registrationCity":res_query["data"]["projCustEnterpriseVMList"][0]["registrationCity"],
                        "registrationRegionName":res_query["data"]["projCustEnterpriseVMList"][0]["registrationRegionName"],
                        "registrationRegion":res_query["data"]["projCustEnterpriseVMList"][0]["registrationRegion"],
                        "registrationAddress":res_query["data"]["projCustEnterpriseVMList"][0]["registrationAddress"],
                        "officeProvinceName":res_query["data"]["projCustEnterpriseVMList"][0]["officeProvinceName"],
                        "officeProvince":res_query["data"]["projCustEnterpriseVMList"][0]["officeProvince"],
                        "officeCityName":res_query["data"]["projCustEnterpriseVMList"][0]["officeCityName"],
                        "officeCity":res_query["data"]["projCustEnterpriseVMList"][0]["officeCity"],
                        "officeLocationName":res_query["data"]["projCustEnterpriseVMList"][0]["officeLocationName"],
                        "officeLocation":res_query["data"]["projCustEnterpriseVMList"][0]["officeLocation"],
                        "officeAddress":res_query["data"]["projCustEnterpriseVMList"][0]["officeAddress"],
                        "actualBusinessProvinceName":res_query["data"]["projCustEnterpriseVMList"][0]["actualBusinessProvinceName"],
                        "actualBusinessProvince":res_query["data"]["projCustEnterpriseVMList"][0]["actualBusinessProvince"],
                        "actualBusinessCityName":res_query["data"]["projCustEnterpriseVMList"][0]["actualBusinessCityName"],
                        "actualBusinessCity":res_query["data"]["projCustEnterpriseVMList"][0]["actualBusinessCity"],
                        "actualBusinessLocationName":res_query["data"]["projCustEnterpriseVMList"][0]["actualBusinessLocationName"],
                        "actualBusinessLocation":res_query["data"]["projCustEnterpriseVMList"][0]["actualBusinessLocation"],
                        "actualBusinessAddress":res_query["data"]["projCustEnterpriseVMList"][0]["actualBusinessAddress"],
                        "rentStockholderRelated":res_query["data"]["projCustEnterpriseVMList"][0]["rentStockholderRelated"],
                        "rentRelated":res_query["data"]["projCustEnterpriseVMList"][0]["rentRelated"],
                        "ruralUrbanSignageName":res_query["data"]["projCustEnterpriseVMList"][0]["ruralUrbanSignageName"],
                        "ruralUrbanSignage":res_query["data"]["projCustEnterpriseVMList"][0]["ruralUrbanSignage"],
                        "projectSourceName":res_query["data"]["projCustEnterpriseVMList"][0]["projectSourceName"],
                        "projectSource":res_query["data"]["projCustEnterpriseVMList"][0]["projectSource"],
                        "licProjectInvestmentOneName":res_query["data"]["projCustEnterpriseVMList"][0]["licProjectInvestmentOneName"],
                        "licProjectInvestmentOne":res_query["data"]["projCustEnterpriseVMList"][0]["licProjectInvestmentOne"],
                        "licProjectInvestmentTwoName":res_query["data"]["projCustEnterpriseVMList"][0]["licProjectInvestmentTwoName"],
                        "licProjectInvestmentTwo":res_query["data"]["projCustEnterpriseVMList"][0]["licProjectInvestmentTwo"],
                        "licProjectInvestmentThreeName":res_query["data"]["projCustEnterpriseVMList"][0]["licProjectInvestmentThreeName"],
                        "licProjectInvestmentThree":res_query["data"]["projCustEnterpriseVMList"][0]["licProjectInvestmentThree"],
                        "licProjectInvestmentFourName":res_query["data"]["projCustEnterpriseVMList"][0]["licProjectInvestmentFourName"],
                        "licProjectInvestmentFour":res_query["data"]["projCustEnterpriseVMList"][0]["licProjectInvestmentFour"],
                        "businessScope":res_query["data"]["projCustEnterpriseVMList"][0]["businessScope"],
                        "mainBusinessProducts":res_query["data"]["projCustEnterpriseVMList"][0]["mainBusinessProducts"],
                        "enterpriseSizeName":res_query["data"]["projCustEnterpriseVMList"][0]["enterpriseSizeName"],
                        "enterpriseSize":res_query["data"]["projCustEnterpriseVMList"][0]["enterpriseSize"],
                        "enterpriseType":res_query["data"]["projCustEnterpriseVMList"][0]["enterpriseType"],
                        "enterpriseTypeName":None,
                        "institutionRegistCertNumber":None,
                        "financialInstitutionCode":None,
                        "holdingType":res_query["data"]["projCustEnterpriseVMList"][0]["holdingType"],
                        "holdingTypeName":res_query["data"]["projCustEnterpriseVMList"][0]["holdingTypeName"],
                        "zhongzhengCode":res_query["data"]["projCustEnterpriseVMList"][0]["zhongzhengCode"],
                        "currencyName":res_query["data"]["projCustEnterpriseVMList"][0]["currencyName"],
                        "currency":res_query["data"]["projCustEnterpriseVMList"][0]["currency"],
                        "registeredCapital":res_query["data"]["projCustEnterpriseVMList"][0]["registeredCapital"],
                        "paidinCapital":res_query["data"]["projCustEnterpriseVMList"][0]["paidinCapital"],
                        "capitalization":res_query["data"]["projCustEnterpriseVMList"][0]["capitalization"],
                        "revenue":res_query["data"]["projCustEnterpriseVMList"][0]["revenue"],
                        "establishmentTime":res_query["data"]["projCustEnterpriseVMList"][0]["establishmentTime"],
                        "businessLicenseExpirationDate":res_query["data"]["projCustEnterpriseVMList"][0]["businessLicenseExpirationDate"],
                        "businessStatus":res_query["data"]["projCustEnterpriseVMList"][0]["businessStatus"],
                        "businessStatusName":res_query["data"]["projCustEnterpriseVMList"][0]["businessStatusName"],
                        "employeeNumber":res_query["data"]["projCustEnterpriseVMList"][0]["employeeNumber"],
                        "legalRepresentative":res_query["data"]["projCustEnterpriseVMList"][0]["legalRepresentative"],
                        "legalRepresentativeMobile":res_query["data"]["projCustEnterpriseVMList"][0]["legalRepresentativeMobile"],
                        "idProvince": "120000",
                        "idProvinceName": None,
                        "idCity": "120100",
                        "idCityName": None,
                        "idLocation": "120101",
                        "idLocationName": None,
                        "idAddress": res_query["data"]["projCustEnterpriseVMList"][0]["idAddress"],
                        "legalPersonPhone": res_query["data"]["projCustEnterpriseVMList"][0]["legalPersonPhone"],
                        "actualController": res_query["data"]["projCustEnterpriseVMList"][0]["actualController"],
                        "nationalEconomy":res_query["data"]["projCustEnterpriseVMList"][0]["nationalEconomy"],
                        "nationalEconomyName": res_query["data"]["projCustEnterpriseVMList"][0]["nationalEconomyName"],
                        "listedCompanyLogoName": res_query["data"]["projCustEnterpriseVMList"][0]["listedCompanyLogoName"],
                        "listedCompanyLogo":res_query["data"]["projCustEnterpriseVMList"][0]["listedCompanyLogo"],
                        "resolutionType": res_query["data"]["projCustEnterpriseVMList"][0]["resolutionType"],
                        "resolutionTypeName": res_query["data"]["projCustEnterpriseVMList"][0]["resolutionTypeName"],
                        "email": res_query["data"]["projCustEnterpriseVMList"][0]["email"],
                        "authId":  res_query["data"]["projCustEnterpriseVMList"][0]["authId"],
                        "shareholdingStructureList": [],
                        "idArray": ["120000", "120100", "120101"],
                        "internationalIndustryType": ["A", "A01", "A011", "A0111"],
                        "registration": ["110000", "110100", "110101"]
                    }]
            }
        res = self.api(method = 'POST', url =url,json = data)

    '''交易结构-增加'''
    def projTradeAdd(self,projectNo):
        trade = []
        url = 'ifc/api/credit-apply/trades/addProjTrades'
        data = {
            "projectNo": projectNo
        }
        for i in range(9):
            res = self.api(method='POST', url=url, json=data)
            trade.append(res)
        return trade


    '''供应商保存'''
    def supplierSave(self, projectNo, custName, id_1, id_2, id_3, id_4, id_5, id_6, id_7, id_8, id_9):
        url = 'ifc/api/credit-apply/trades/saveSupplier'
        data = {"xzw": {"supplierId":"9820",
                        "supplierName":"测试Z500供应商合同公司1",
                        "certId":"91350102315514081E",
                        "artificialPerson":"夏紫文",
                        "registerFullAddress":"110000|110100|110111;北京市|市辖区|房山区|123123",
                        "businessAddress":"110000|110100|110111;北京市|市辖区|房山区|123123"},
                "jxw": {"supplierId": "9836",
                        "supplierName": "测试Z500供应商合同公司J1",
                        "certId": "91110000FB0RBU0R7P",
                        "artificialPerson": "季晓伟",
                        "registerFullAddress": "110000|110100|110101;北京市|市辖区|东城区",
                        "businessAddress": "110000|110100|110101;北京市|市辖区|东城区"},
                "fht": {"supplierId": "9847",
                        "supplierName": "测试供应商F1",
                        "certId": "91410100732484450T",
                        "artificialPerson": "范怀通",
                        "registerFullAddress": "410000|410100|410102;河南省|郑州市|中原区|宇工路88号",
                        "businessAddress": "410000|410100|410102;河南省|郑州市|中原区|宇工路88号"},
                "zll": {"supplierId": "9841",
                        "supplierName": "测试Z500供应商合同公司J2",
                        "certId": "91120000WH9CX8CE5N",
                        "artificialPerson": "季晓伟",
                        "registerFullAddress": "120000|120100|120101;天津市|市辖区|和平区",
                        "businessAddress": "120000|120100|120101;天津市|市辖区|和平区"},
                "cm": {"supplierId": "9852",
                        "supplierName": "测试Z500特斯拉",
                        "certId": "91310115MA1H9YGWXX",
                        "artificialPerson": "陈鸣",
                        "registerFullAddress": "110000|110100|110105;北京市|市辖区|朝阳区|注册详细地址",
                        "businessAddress": "110000|110100|110105;北京市|市辖区|朝阳区|注册详细地址"}
                }
        list = []
        data_1 = {
            "id": None,
            "projectNo": projectNo,
            "projTradesId": id_1,
            "supplierId": data[custName]["supplierId"],
            "supplierName": data[custName]["supplierName"],
            "certType": "200",
            "certId": data[custName]["certId"],
            "artificialPerson": data[custName]["artificialPerson"],
            "registerFullAddress": data[custName]["registerFullAddress"],
	        "businessAddress": data[custName]["businessAddress"],
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
            "braceletInstallNode": "AfterPayment",
            "braceletInstallNodeName": "付款后安装",
            "productNodeType": "LS-DFL-I",
            "productNodeTypeName": "直接租赁",
            "isInstallBracelet": 1,
            "isInstallBraceletName": "是",
            "notePeriod": "01",
            "notePeriodName": "60天",
        }
        data_2 = {
            "id": None,
            "projectNo": projectNo,
            "projTradesId": id_2,
            "supplierId": data[custName]["supplierId"],
            "supplierName": data[custName]["supplierName"],
            "certType": "200",
            "certId": data[custName]["certId"],
            "artificialPerson": data[custName]["artificialPerson"],
            "registerFullAddress": data[custName]["registerFullAddress"],
	        "businessAddress": data[custName]["businessAddress"],
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
            "braceletInstallNode": "AfterPayment",
            "braceletInstallNodeName": "付款后安装",
            "productNodeType": "LS-DFL-I",
            "productNodeTypeName": "直接租赁",
            "isInstallBracelet": 1,
            "isInstallBraceletName": "是",
            "notePeriod": "01",
            "notePeriodName": "60天",
        }
        data_3 = {
            "id": None,
            "projectNo": projectNo,
            "projTradesId": id_3,
            "supplierId": data[custName]["supplierId"],
            "supplierName": data[custName]["supplierName"],
            "certType": "200",
            "certId": data[custName]["certId"],
            "artificialPerson": data[custName]["artificialPerson"],
            "registerFullAddress": data[custName]["registerFullAddress"],
	        "businessAddress": data[custName]["businessAddress"],
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
            "braceletInstallNode": "AfterPayment",
            "braceletInstallNodeName": "付款后安装",
            "productNodeType": "LS-DFL-I",
            "productNodeTypeName": "直接租赁",
            "isInstallBracelet": 1,
            "isInstallBraceletName": "是",
            "notePeriod": "01",
            "notePeriodName": "60天",
        }


        data_4 = {
            "id": None,
            "projectNo": projectNo,
            "projTradesId": id_4,
            "supplierId": data[custName]["supplierId"],
            "supplierName": data[custName]["supplierName"],
            "certType": "200",
            "certId": data[custName]["certId"],
            "artificialPerson": data[custName]["artificialPerson"],
            "registerFullAddress": data[custName]["registerFullAddress"],
	        "businessAddress": data[custName]["businessAddress"],
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
            "notePeriodName": "60天",
        }
        data_5 = {
            "id": None,
            "projectNo": projectNo,
            "projTradesId": id_5,
            "supplierId": data[custName]["supplierId"],
            "supplierName": data[custName]["supplierName"],
            "certType": "200",
            "certId": data[custName]["certId"],
            "artificialPerson": data[custName]["artificialPerson"],
            "registerFullAddress": data[custName]["registerFullAddress"],
	        "businessAddress": data[custName]["businessAddress"],
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
            "notePeriodName": "60天",
        }
        data_6 = {
            "id": None,
            "projectNo": projectNo,
            "projTradesId": id_6,
            "supplierId": data[custName]["supplierId"],
            "supplierName": data[custName]["supplierName"],
            "certType": "200",
            "certId": data[custName]["certId"],
            "artificialPerson": data[custName]["artificialPerson"],
            "registerFullAddress": data[custName]["registerFullAddress"],
	        "businessAddress": data[custName]["businessAddress"],
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
            "notePeriodName": "60天",
        }



        data_7 = {
            "id": None,
            "projectNo": projectNo,
            "projTradesId": id_7,
            "supplierId": data[custName]["supplierId"],
            "supplierName": data[custName]["supplierName"],
            "certType": "200",
            "certId": data[custName]["certId"],
            "artificialPerson": data[custName]["artificialPerson"],
            "registerFullAddress": data[custName]["registerFullAddress"],
	        "businessAddress": data[custName]["businessAddress"],
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
            "tradeMode": "01",
            "tradeModeName": "预付货款",
            "settleMode": "TelegraphicTransfer",
            "settleModeName": "转账",
            "braceletInstallNode": "AfterPayment",
            "braceletInstallNodeName": "付款后安装",
            "productNodeType": "LS-DFL-I",
            "productNodeTypeName": "直接租赁",
            "isInstallBracelet": 1,
            "isInstallBraceletName": "是",
            "notePeriod": "01",
            "notePeriodName": None,
        }
        data_8 = {
            "id": None,
            "projectNo": projectNo,
            "projTradesId": id_8,
            "supplierId": data[custName]["supplierId"],
            "supplierName": data[custName]["supplierName"],
            "certType": "200",
            "certId": data[custName]["certId"],
            "artificialPerson": data[custName]["artificialPerson"],
            "registerFullAddress": data[custName]["registerFullAddress"],
	        "businessAddress": data[custName]["businessAddress"],
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
            "tradeMode": "01",
            "tradeModeName": "预付货款",
            "settleMode": "TelegraphicTransfer",
            "settleModeName": "转账",
            "braceletInstallNode": "AfterPayment",
            "braceletInstallNodeName": "付款后安装",
            "productNodeType": "LS-DFL-I",
            "productNodeTypeName": "直接租赁",
            "isInstallBracelet": 1,
            "isInstallBraceletName": "是",
            "notePeriod": "01",
            "notePeriodName": None,
        }
        data_9 = {
            "id": None,
            "projectNo": projectNo,
            "projTradesId": id_9,
            "supplierId": data[custName]["supplierId"],
            "supplierName": data[custName]["supplierName"],
            "certType": "200",
            "certId": data[custName]["certId"],
            "artificialPerson": data[custName]["artificialPerson"],
            "registerFullAddress": data[custName]["registerFullAddress"],
	        "businessAddress": data[custName]["businessAddress"],
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
            "tradeMode": "01",
            "tradeModeName": "预付货款",
            "settleMode": "TelegraphicTransfer",
            "settleModeName": "转账",
            "braceletInstallNode": "AfterPayment",
            "braceletInstallNodeName": "付款后安装",
            "productNodeType": "LS-DFL-I",
            "productNodeTypeName": "直接租赁",
            "isInstallBracelet": 1,
            "isInstallBraceletName": "是",
            "notePeriod": "01",
            "notePeriodName": None,
        }

        list.append(data_1)
        list.append(data_2)
        list.append(data_3)
        list.append(data_4)
        list.append(data_5)
        list.append(data_6)
        list.append(data_7)
        list.append(data_8)
        list.append(data_9)
        for i in list:
            res = self.api(method='POST', url=url, json=i)

    '''查询品牌'''
    def pageSerach(self):
        url = 'ifc/api/proj/pageSearchBrands'
        data = {
            "searchParam": "",
            "current": 1,
            "size": 50
        }
        res = self.api(method='POST', url=url, json=data)
        return res

    '''添加租赁物'''
    def leaseSave(self,projectNo,id):
        res = self.pageSerach()
        url = 'ifc/api/credit-apply/trades/saveLeasehold'
        data = {
            "projectNo": projectNo,
            "projTradesId": id,
            "tradesLeaseholdList": [{
                "showMore": True,
                "projectNo": "",
                "projTradesId": None,
                "leaseholdName": "第一个租赁物",
                "brandId": jsonpath.jsonpath(res,"$..idArtlBrand")[49],
                "brandFullName": jsonpath.jsonpath(res,"$..brandFullName")[49],
                "spec": "123",
                "leaseholdType": "625304010101",
                "industryClassify": ["A", "A01", "A011"],
                "industryClassifyName": "",
                "industryClassifyOne": "A",
                "industryClassifyOneName": "",
                "industryClassifyTwo": "A01",
                "industryClassifyTwoName": "",
                "price": "10000.00",
                "amount": "1",
                "financeAmt": 1000,
                "financeScale": "10.00",
                "bookAmt": "10000.00",
                "isInstallBracelet": 1,
                "isLesseeRegisterAddress": 1,
                "isLesseeTheOwner": 0,
                "ownerType": "",
                "ownerName": "",
                "place": [],
                "placeProvince": "",
                "placeProvinceName": "",
                "placeCity": "",
                "placeCityName": "",
                "placeDistrict": "",
                "placeDistrictName": "",
                "placeDetailAddress": "",
                "directReversalUniqueIdentifier": "",
                "leaseholdTypeList": ["625001000000", "625101010000", "625201010100", "625304010101"],
                "leaseholdTypeOne": "625001000000",
                "leaseholdTypeTwo": "625101010000",
                "leaseholdTypeThree": "625201010100",
                "industryClassifyThree": "A011",
                "brandLevel": jsonpath.jsonpath(res,"$..brandLevel")[49],
                "facilityName": jsonpath.jsonpath(res,"$..facilityName")[49]
            }]
        }
        res = self.api(method='POST', url=url, json=data)

    '''查询融资信息'''
    def financeQuery(self,projectNo,projTradesId):
        url = 'ifc/api/credit-apply/trades/queryFinanceInfo'
        data = {
            "projectNo": projectNo,
            "projTradesId": projTradesId
        }
        res = self.api(method='POST', url=url, json=data)

        return res

    '''租金测算'''
    def rentCalc(self,projectNo,projTradesId,id):
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
            "preditRentDate": str(datetime.datetime.now().date()),
            "financeTerm": 12,
            "yearPaymentTimes": "12",
            "totalPaymentTimes": "12",
            "financeTotalAmt": 1000,
            "totalBookAmt": "10000.00",
            "financingPaymentDirection": "Supplier",
            "financingPaymentDirectionName": "供应商",
            "isExistDownPayment": 1,
            "isExistDownPaymentName": "是",
            "downPaymentCalcMode": "FIX_AMOUNT",
            "downPaymentCalcModeName": "固定金额",
            "downPaymentRatio": 0.9,
            "downPaymentAmt": 9000,
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
            "rentAmt": "100",
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
        res = self.api(method='POST', url=url, json=data)
        return res

    # def rentCalc(self,projectNo,projTradesId,id):
    #     '''租金测算'''
    #     url = 'ifc/api/credit-apply/trades/rentCalc'
    #     data = {
    #             "projectNo": projectNo,
    #             "projTradesId": projTradesId,
    #             "id": id,
    #             "rateAppearMode": "Implication",
    #             "lprBaseRate": None,
    #             "rentRate": None,
    #             "bpFloatValue": None,
    #             "preditRentDate": datetime.datetime.now().date(),
    #             "financeTerm": 12,
    #             "yearPaymentTimes": "12",
    #             "totalPaymentTimes": "12",
    #             "financeTotalAmt": "1000.00",
    #             "totalBookAmt": 10000,
    #             "financingPaymentDirection": "Supplier",
    #             "financingPaymentDirectionName": "供应商",
    #             "isExistDownPayment": 1,
    #             "downPaymentCalcMode": "FIX_AMOUNT",
    #             "downPaymentRatio": 0.9,
    #             "downPaymentAmt": 9000,
    #             "downPaymentPayDirection": "Supplier",
    #             "isExistMargin": 0,
    #             "isExistMarginName": None,
    #             "marginCalcMode": None,
    #             "marginRatio": None,
    #             "marginAmt": None,
    #             "marginDeductMode": None,
    #             "retentionPriceAmt": "100.00",
    #             "discountAmt": None,
    #             "firstTermAmt": None,
    #             "rentalMode": "Prepay",
    #             "rentalModeName": None,
    #             "rentCalcMode": "EquivalentRent",
    #             "rentAmt": "100",
    #             "quickPaymentAmt": None,
    #             "rentTotalAmt": None,
    #             "interestTotalAmt": None,
    #             "recoveryPrincipalTotalAmt": None,
    #             "incomeTotalAmt": None,
    #             "xirrRate": None,
    #             "xirrPureRate": None,
    #             "irrRate": None,
    #             "irrPureRate": None,
    #             "financeSegmentList": [],
    #             "repayScheduleList": []
    #         }
    #     res = self.api(method='POST', url=url, json=data)
    #     return res

    '''融资信息'''
    def rentSave(self,projectNo,projTradesId):
        res = self.financeQuery(projectNo,projTradesId)
        id = jsonpath.jsonpath(res,'$..id')[0]
        self.rentCalc(projectNo,projTradesId,id)
        url = 'ifc/api/credit-apply/trades/rentSave'
        data = {
            "projectNo": projectNo,
            "projTradesId": projTradesId,
            "id": id,
            "rateAppearMode": "Implication",
            "lprBaseRate": "3.65",
            "rentRate": 0.4204,
            "bpFloatValue": "3,838.61",
            "preditRentDate": str(datetime.datetime.now().date()),
            "financeTerm": 12,
            "yearPaymentTimes": "12",
            "totalPaymentTimes": "12",
            "financeTotalAmt": "1000.00",
            "totalBookAmt": 10000,
            "financingPaymentDirection": "Supplier",
            "financingPaymentDirectionName": "供应商",
            "isExistDownPayment": 1,
            "downPaymentCalcMode": "FIX_AMOUNT",
            "downPaymentRatio": 0.9,
            "downPaymentAmt": 9000,
            "downPaymentPayDirection": "Supplier",
            "isExistMargin": 0,
            "isExistMarginName": None,
            "marginCalcMode": None,
            "marginRatio": None,
            "marginAmt": None,
            "marginDeductMode": None,
            "retentionPriceAmt": "100.00",
            "discountAmt": None,
            "firstTermAmt": None,
            "rentalMode": "Prepay",
            "rentalModeName": None,
            "rentCalcMode": "EquivalentRent",
            "rentAmt": "100.00",
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
        res = self.api(method='POST', url=url, json=data)

    '''评估主体类型'''
    def evaluationSubjectQuery(self,projectNo):
        url = 'ifc/api/risk-info/queryEvaluationSubjectBase'
        data = {
            "projectNo": projectNo,
            "roleType": "1"
        }
        res = self.api(method='POST', url=url, json=data)
        return res

    def evaluationSubjectScoreQuery(self,projectNo):
        '''评估主体得分'''
        res_subject = self.evaluationSubjectQuery(projectNo)
        url = 'ifc/api/risk-info/queryEvaluationSubjectScore'
        data = {
            "projectNo": projectNo,
            "evaluationSubjectId": jsonpath.jsonpath(res_subject,'$..evaluationSubjectId')[0],
            "evaluationSubjectType": "1"
        }
        res_score = self.api(method='POST', url=url, json=data)
        return res_subject,res_score

    '''评估主体保存'''
    def evaluationSubjectSave(self,projectNo):
        res = self.evaluationSubjectScoreQuery(projectNo)
        url = 'ifc/api/risk-info/saveEvaluationSubject'
        data = {
            "id": None,
            "projectNo": projectNo,
            "evaluationSubjectId": jsonpath.jsonpath(res[0],'$..evaluationSubjectId')[0],
            "evaluationSubjectType": "1",
            "evaluationSubjectTypeName": None,
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
                "projectNo": None,
                "scoreItemCode": "houseProperty",
                "scoreItemName": "房产（单价超1万，且净值覆盖敞口）",
                "elementValue": "是",
                "ratingScore": 1
            }, {
                "id": None,
                "projectNo": None,
                "scoreItemCode": "houseProperty",
                "scoreItemName": "房产（单价超1万，且净值覆盖敞口）",
                "elementValue": "否",
                "ratingScore": 0
            }, {
                "id": None,
                "projectNo": None,
                "scoreItemCode": "depositGt5timesRent6Mon",
                "scoreItemName": "近6个月内日均存款余额大于最高租金5倍",
                "elementValue": "是",
                "ratingScore": 1
            }, {
                "id": None,
                "projectNo": None,
                "scoreItemCode": "depositGt5timesRent6Mon",
                "scoreItemName": "近6个月内日均存款余额大于最高租金5倍",
                "elementValue": "否",
                "ratingScore": 0
            }, {
                "id": None,
                "projectNo": None,
                "scoreItemCode": "personDishonestExecutee",
                "scoreItemName": "当前未决诉讼达20万或2年内曾失信限高等",
                "elementValue": "是",
                "ratingScore": -1
            }, {
                "id": None,
                "projectNo": None,
                "scoreItemCode": "personDishonestExecutee",
                "scoreItemName": "当前未决诉讼达20万或2年内曾失信限高等",
                "elementValue": "否",
                "ratingScore": 0
            }, {
                "id": None,
                "projectNo": None,
                "scoreItemCode": "loansAndConsume6mGe3",
                "scoreItemName": "近六个月小贷、消费类金融查询超3次（含）",
                "elementValue": "是",
                "ratingScore": -1
            }, {
                "id": None,
                "projectNo": None,
                "scoreItemCode": "loansAndConsume6mGe3",
                "scoreItemName": "近六个月小贷、消费类金融查询超3次（含）",
                "elementValue": "否",
                "ratingScore": 0
            }, {
                "id": None,
                "projectNo": None,
                "scoreItemCode": "businessTeam60AndOverdueRateOver2Percent",
                "scoreItemName": "业务团队60+逾期率超2%",
                "elementValue": "是",
                "ratingScore": -2
            }, {
                "id": None,
                "projectNo": None,
                "scoreItemCode": "businessTeam60AndOverdueRateOver2Percent",
                "scoreItemName": "业务团队60+逾期率超2%",
                "elementValue": "否",
                "ratingScore": 0
            }],
            "scoreItemVMList": jsonpath.jsonpath(res[1],'$..scoreItemVMList')[0]
        }
        res = self.api(method='POST', url=url, json=data)

    '''授信要素查询'''
    def creditElementQuery(self,projectNo):
            url = 'ifc/api/risk-info/queryCreditElement'
            data = {
                "projectNo": projectNo
            }
            res = self.api(method='POST', url=url, json=data)
            return res

    '''授信归属公司查询'''
    def queryEnterpriseByproject(self,projectNo):
        url = 'ifc/api/proj_cust_enterprise_related_info/queryEnterpriseByProjectNoAndRoleType'
        data = {
            "projectNo": projectNo
        }
        res = self.api(method='POST', url=url, json=data)
        return res

    '''授信要素'''
    def creditElementSave(self,projectNo):
        res = self.queryEnterpriseByproject(projectNo)
        url = 'ifc/api/risk-info/saveCreditElement'
        data ={
            "projectNo": projectNo,
            "custRelatedList": [],
            "shareholderStructureList": [],
            "projCustEnterpriseIncomeVerification": {
                "id": None,
                "confirmableIncome": "10",
                "currentYearIncome": "10.00",
                "previousYearIncome": "10.00",
                "projectNo": None
            },
            "bankStatementList": [],
            "electricChargeList": [{
                "billDate": "2023-08",
                "billAmount": "10.00"
            }, {
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
            }],
            "rigidLiabilityList": [{
                "customerType": "1",
                "liabilityType": "BankLoan",
                "belongingCompanyId": jsonpath.jsonpath(res,'$..id')[0],
                "rigidLiabilityAmount": "100.00",
                "mortgageLiabilityAmount": "100.00"
            }],
            "totalAmount": 800,
            "recentElecDate": "2023-08"
        }
        res = self.api(method='POST', url=url, json=data)

    '''准入要求'''
    def accessRquirementSave(self,projectNo):
        url = 'ifc/api/risk-info/saveAccessRequirement'
        data = {
                "projectNo": projectNo,
                "list": [{
                    "accessItemCode": "",
                    "arSubTypeName": "其他",
                    "arDesc": "其他",
                    "comment": "其他备注",
                    "projectNo": projectNo,
                    "arCode": "ar6",
                    "arSubCode": "arSub16"
                }]
            }
        res = self.api(method='POST', url=url, json=data)

    '''影像信息'''
    def attachmentSave(self,projectNo,fileId,fileName,subCategoryCode):
        url = 'ifc/api/attachment/saveFileRelation'
        data = {
            "fileId": fileId,
            "fileName": fileName,
            "subCategoryCode": subCategoryCode,
            "isUpdate": False,
            "code": "projectCreditApproval",
            "businessKey": projectNo,
            "businessType": "PROJECT"
        }
        res = self.api(method='POST', url=url, json=data)

    '''影像信息下一步校验'''
    def attachmentNextStep(self,projectNo):
        url = 'ifc/api/attachment/nextStep'
        data = {
            "businessKey": projectNo,
            "templateCode": "projectCreditApproval"
        }
        res = self.api(method='POST', url=url, json=data)

    '''补充资料'''
    def reqTextSave(self,projectNo):
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
        res = self.api(method='POST', url=url, json=data)

    def detectorExec(self,itemCode,taskid,detectorCode):
        url = 'ifc/api/common/detector/exec'
        data = {
            "detectorCode": detectorCode,
            "itemCode": itemCode,
            "taskId": taskid
            }
        res = self.api(method='POST', url=url, json=data)

    def todoListApp(self):
        '''审批列表'''
        url = 'bpm/api/v2/cmapp-filter/mytask/todo-list?channel=appstore&os=ios&page=0&size=20&timeString=1692588472.32&version=1.1.4'
        res = self.api(method='GET', url=url)
        return res

    def todoListPc(self):
        url = 'bpm/api/v2/mytask/todo-list?page=0&size=50&sort='
        res = self.api(method='GET', url=url)
        return res

    def getPcTask(self,projectNo):
        res = self.todoListPc()
        for i in res["content"]:
            if i["businessKey"] == projectNo:
                taskid = i["id"]
                break;
        return taskid

    def completeInit(self,taskId):
        url = 'ifc/api/flow/task-complete/init?taskId=%s'%taskId
        res = self.api(method='GET', url=url)
        return res

    def result(self,start_time,projectNo):
        end_time = time.time()
        run_time = round(end_time - start_time, 2)
        result = {
            "code": 200,
            "status": True,
            "message": 'success,耗时%ss,打开app项目列表查看新建项目！！！' % run_time,
            "data": "项目编号：%s" % projectNo
        }
        return result
