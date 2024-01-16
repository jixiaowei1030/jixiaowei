from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from Z500.tools import test_data
from Z500.common.login import login




import time
import requests
import jsonpath
import datetime
import logging
import PyPDF2


class xiaoWeiNew():

    def __init__(self, headers, env):
        if env == 'sit':
            self.url = 'https://sit-vrip.msfl.com.cn/'
        else:
            self.url = 'https://test-vrip.msfl.com.cn/'
        self.headers = headers
        self.req = requests.session()
        self.req_again = requests.session()

    def api(self,**kwargs):
        url = self.url + kwargs.get("url")
        kwargs.pop("url")

        retries = Retry(total=2,
                        status_forcelist=[400, 500, 502, 503, 504])

        self.req.mount('http://', HTTPAdapter(max_retries=retries))
        self.req.mount('https://', HTTPAdapter(max_retries=retries))

        try:
            res = self.req.request(url =url, verify=False, headers=self.headers, **kwargs).json()
            print(url,"响应json:",res)
            return res
        except Exception as e:
            # print("发生异常：", str(e))
            time.sleep(30)
            res_again = self.req_again.request(url=url, verify=False, headers=self.headers, **kwargs).json()
            try:
                if res_again["code"] == 0:
                # print(url)
                    return res_again
                else:
                    raise Exception(url, res_again)
            except:
                raise Exception(url, res_again)
            # print(url, res_again)

            # try:
            #     print("发生异常：", str(e))
            #     time.sleep(30)
            #     res_again = self.req.request(url=url, verify=False, headers=self.headers, **kwargs).json()
            #     print(url, res_again)
            #     return res_again
            # except:
            #     print(res_again)

    def updateHeader(self,custName,env):
        res = login(custName,env)
        print(res)
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

    def creditAuthSave(self,projectNo,custName,guarantor,env):
        '''创建征信授权'''
        if env == 'sit':
            url = 'https://sit-asp.msfl.com.cn/asp/ifc/notice/credit-auth/save'
        else:
            url = 'https://test-asp.msfl.com.cn/asp/ifc/notice/credit-auth/save'
        retries = Retry(total=2,
                        status_forcelist=[400, 404, 500, 502, 503, 504])
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

    def creditAuthBack(self,projectNo,custName,guarantor,env):
        '''征信授权完成'''
        if env == 'sit':
            url = 'https://sit-asp.msfl.com.cn/asp/ifc/notice/credit-auth/signOffCallback'
        else:
            url = 'https://test-asp.msfl.com.cn/asp/ifc/notice/credit-auth/signOffCallback'
        retries = Retry(total=2,
                        status_forcelist=[400, 404, 500, 502, 503, 504])
        req = requests.session()
        req.mount('http://', HTTPAdapter(max_retries=retries))
        req.mount('https://', HTTPAdapter(max_retries=retries))

        data = test_data.getBackData(projectNo,custName,guarantor)
        for i in data:
            try:
                res = req.request(method='POST', url=url, json=i,verify=False, headers=self.headers)
                time.sleep(1)
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
        elif guarantor == '2':
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
        elif guarantor == '3':
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
                    },
                    {
                        "id": jsonpath.jsonpath(res_query, '$..id')[2],
                        "creditCustomerType": jsonpath.jsonpath(res_query, '$..creditCustomerType')[2],
                        "creditCustomerTypeName": jsonpath.jsonpath(res_query, '$..creditCustomerTypeName')[2],
                        "creditCustomerName": jsonpath.jsonpath(res_query, '$..creditCustomerName')[2],
                        "creditCustomerNo": jsonpath.jsonpath(res_query, '$..creditCustomerNo')[2],
                        "creditCustomerIdType": jsonpath.jsonpath(res_query, '$..creditCustomerIdType')[2],
                        "creditCustomerIdTypeName": jsonpath.jsonpath(res_query, '$..creditCustomerIdTypeName')[2],
                        "roleType": "2"
                    },
                    {
                        "id": jsonpath.jsonpath(res_query, '$..id')[3],
                        "creditCustomerType": jsonpath.jsonpath(res_query, '$..creditCustomerType')[3],
                        "creditCustomerTypeName": jsonpath.jsonpath(res_query, '$..creditCustomerTypeName')[3],
                        "creditCustomerName": jsonpath.jsonpath(res_query, '$..creditCustomerName')[3],
                        "creditCustomerNo": jsonpath.jsonpath(res_query, '$..creditCustomerNo')[3],
                        "creditCustomerIdType": jsonpath.jsonpath(res_query, '$..creditCustomerIdType')[3],
                        "creditCustomerIdTypeName": jsonpath.jsonpath(res_query, '$..creditCustomerIdTypeName')[3],
                        "roleType": "3"
                    },
                    {
                        "id": jsonpath.jsonpath(res_query, '$..id')[4],
                        "creditCustomerType": jsonpath.jsonpath(res_query, '$..creditCustomerType')[4],
                        "creditCustomerTypeName": jsonpath.jsonpath(res_query, '$..creditCustomerTypeName')[4],
                        "creditCustomerName": jsonpath.jsonpath(res_query, '$..creditCustomerName')[4],
                        "creditCustomerNo": jsonpath.jsonpath(res_query, '$..creditCustomerNo')[4],
                        "creditCustomerIdType": jsonpath.jsonpath(res_query, '$..creditCustomerIdType')[4],
                        "creditCustomerIdTypeName": jsonpath.jsonpath(res_query, '$..creditCustomerIdTypeName')[4],
                        "roleType": "2"
                    },
                    {
                        "id": jsonpath.jsonpath(res_query, '$..id')[5],
                        "creditCustomerType": jsonpath.jsonpath(res_query, '$..creditCustomerType')[5],
                        "creditCustomerTypeName": jsonpath.jsonpath(res_query, '$..creditCustomerTypeName')[5],
                        "creditCustomerName": jsonpath.jsonpath(res_query, '$..creditCustomerName')[5],
                        "creditCustomerNo": jsonpath.jsonpath(res_query, '$..creditCustomerNo')[5],
                        "creditCustomerIdType": jsonpath.jsonpath(res_query, '$..creditCustomerIdType')[5],
                        "creditCustomerIdTypeName": jsonpath.jsonpath(res_query, '$..creditCustomerIdTypeName')[5],
                        "roleType": "3"
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
                "financialInstitutionCode": "123",
                "holdingTypeOne": "A",
                "holdingTypeTwo": "A01",
                "holdingTypeThree": "A0101",
                "holdingTypeOneName": "公有控股经济",
                "holdingTypeTwoName": "国有控股",
                "holdingTypeThreeName": "国有相对控股",
                # "zhongzhengCode": jsonpath.jsonpath(res_query,'$..zhongzhengCode')[0],
                "zhongzhengCode":"OZMWEWOT5MSJGE89",
                "currency": "CNY",
                "currencyName": "人民币",
                "registeredCapital": "1000.00",
                "paidinCapital": "1000.00",
                "capitalization": "1000.00",
                "revenue": "1000.00",
                "establishmentTime": "2023-09-14 00:00:00",
                "businessLicenseExpirationDate": "2025-07-19 00:00:00",
                "businessStatus": "01",
                "businessStatusName": "正常运营",
                "employeeNumber": "1000",
                "legalRepresentative": jsonpath.jsonpath(res_query,'$..legalRepresentative')[0],
                "legalRepresentativeMobile": jsonpath.jsonpath(res_query,'$..legalRepresentativeMobile')[0],
                "legalPersonPhone": jsonpath.jsonpath(res_query,'$..legalPersonPhone')[0],
                "actualController": jsonpath.jsonpath(res_query,'$..actualController')[0],
                "nationalEconomyOne": "A",
                "nationalEconomyOneName": "广义政府",
                "nationalEconomyTwo": "A01",
                "nationalEconomyTwoName": "  中央政府",
                "listedCompanyLogo": "A",
                "listedCompanyLogoName": "A股",
                "resolutionType": jsonpath.jsonpath(res_query,'$..resolutionType')[0],
                "resolutionTypeName": jsonpath.jsonpath(res_query,'$..resolutionTypeName')[0],
                "email": "123@163.com",
                "shareholdingStructureList": [],
                "registration": ["110000", "110100", "110101"],
                "actualBusiness": ["110000", "110100", "110101"],
                "internationalIndustryType": ["A", "A01", "A011", "A0111"],
                "licProjectInvestment": ["A", "A01", "A011", "A0111"],
                "industryType": ["A", "A01"],
                "office": ["110000", "110100", "110101"],
                "holdingType": ["A", "A01", "A0101"],
                "isRefinedNew": "002",
                "isHighTechEnterprise": "Y",
                "isDownLoan": "Y"
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
                    "idArray": ["110000", "110100", "110101"],
                    "certificateValidStartDate": "2023-12-25",
                    "industryExperYears": "10",
                    "certificateValidEndDate": "2099-12-31"
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
                    "idArray": ["110000", "110100", "110101"],
                    "certificateValidStartDate": "2023-12-25",
                    "certificateValidEndDate": "2099-12-31"
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
                    "idLocation": "110101",
                    "certificateValidEndDate": "2099-12-31",
                    "certificateValidStartDate": "2023-12-25"
                },
                "personalIds": [],
                "custEnterpriseIds": [],
                "personalInfoModels": [{
                    "id": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].id')[0],
                    "name": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].name')[0],
                    "mobile": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].mobile')[0],
                    "email": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].email')[0],
                    "customerId": None,
                    "roleType": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].roleType')[0],
                    "roleTypeName": None,
                    "idCardType": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].idCardType')[0],
                    "idCardTypeName": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].idCardTypeName')[0],
                    "idCardNo": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].idCardNo')[0],
                    "validityPeriod": None,
                    "shareholdingRatio": None,
                    "actualControllerRelationship": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].actualControllerRelationship')[0],
                    "actualControllerRelationshipName": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].actualControllerRelationshipName')[0],
                    "renterRelationship": None,
                    "renterRelationshipName": None,
                    "maritalStatus": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].maritalStatus')[0],
                    "maritalStatusName": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].maritalStatusName')[0],
                    "gender": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].gender')[0],
                    "genderName": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].genderName')[0],
                    "birthDate": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].birthDate')[0],
                    "idLocation": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].idLocation')[0],
                    "idLocationName": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].idLocationName')[0],
                    "idAddress": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].idAddress')[0],
                    "country": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].country')[0],
                    "countryName": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].countryName')[0],
                    "nation": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].nation')[0],
                    "nationName": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].nationName')[0],
                    "education": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].education')[0],
                    "educationName": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].educationName')[0],
                    "annualIncome": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].annualIncome')[0],
                    "projectNo": projectNo,
                    "sourceId": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].sourceId')[0],
                    "enterpriseInfoId": None,
                    "resolutionType": None,
                    "resolutionTypeName": None,
                    "residenceAddress": None,
                    "creditReportTime": None,
                    "authId": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].authId')[0],
                    "idProvince": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].idProvince')[0],
                    "idProvinceName": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].idProvinceName')[0],
                    "idCity": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].idCity')[0],
                    "idCityName": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].idCityName')[0],
                    "annualIncomeFamily": None,
                    "projectCustomerInfoId":  jsonpath.jsonpath(res_query,'$..personalInfoModels[0].projectCustomerInfoId')[0],
                    "certificateValidStartDate":  jsonpath.jsonpath(res_query,'$..personalInfoModels[0].certificateValidStartDate')[0],
                    "certificateValidEndDate": jsonpath.jsonpath(res_query,'$..personalInfoModels[0].certificateValidEndDate')[0],
                    "industryExperYears": None,
                    "idArray": [jsonpath.jsonpath(res_query,'$..personalInfoModels[0].idProvince')[0], jsonpath.jsonpath(res_query,'$..personalInfoModels[0].idCity')[0], jsonpath.jsonpath(res_query,'$..personalInfoModels[0].idLocation')[0]]
                }],
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
                    "resolutionTypeName": None,
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
                    "idArray": ["110000", "110100", "110101"],
                    "certificateValidStartDate": "2023-12-25",
                    "certificateValidEndDate": "2099-12-31"
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
                    "idArray": ["110000", "110100", "110101"],
                    "certificateValidStartDate": "2023-12-25",
                    "certificateValidEndDate": "2099-12-31"
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
                        "idLocation": "110101",
                        "certificateValidStartDate": "2023-12-25",
                        "certificateValidEndDate": "2099-12-31"
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
                        # "idArray":[
                        #     "110000",
                        #     "110100",
                        #     "110101"
                        # ],
                        "idArray": [jsonpath.jsonpath(res_query, '$..personalInfoModels[0].idProvince')[0],
                                    jsonpath.jsonpath(res_query, '$..personalInfoModels[0].idCity')[0],
                                    jsonpath.jsonpath(res_query, '$..personalInfoModels[0].idLocation')[0]],
                        "certificateValidStartDate": "2023-12-25",
                        "certificateValidEndDate": "2099-12-31"
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
                        "holdingTypeOne": res_query["data"]["projCustEnterpriseVMList"][0]["holdingTypeOne"],
                        "holdingTypeTwo": res_query["data"]["projCustEnterpriseVMList"][0]["holdingTypeTwo"],
                        "holdingTypeThree": res_query["data"]["projCustEnterpriseVMList"][0]["holdingTypeThree"],
                        "holdingTypeOneName": res_query["data"]["projCustEnterpriseVMList"][0]["holdingTypeOneName"],
                        "holdingTypeTwoName": res_query["data"]["projCustEnterpriseVMList"][0]["holdingTypeTwoName"],
                        "holdingTypeThreeName": res_query["data"]["projCustEnterpriseVMList"][0]["holdingTypeThreeName"],
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
                        "nationalEconomyOne": res_query["data"]["projCustEnterpriseVMList"][0]["nationalEconomyOne"],
                        "nationalEconomyOneName": res_query["data"]["projCustEnterpriseVMList"][0]["nationalEconomyOneName"],
                        "nationalEconomyTwo": res_query["data"]["projCustEnterpriseVMList"][0]["nationalEconomyTwo"],
                        "nationalEconomyTwoName": res_query["data"]["projCustEnterpriseVMList"][0]["nationalEconomyTwoName"],
                        "listedCompanyLogoName": res_query["data"]["projCustEnterpriseVMList"][0]["listedCompanyLogoName"],
                        "listedCompanyLogo":res_query["data"]["projCustEnterpriseVMList"][0]["listedCompanyLogo"],
                        "resolutionType": res_query["data"]["projCustEnterpriseVMList"][0]["resolutionType"],
                        "resolutionTypeName": res_query["data"]["projCustEnterpriseVMList"][0]["resolutionTypeName"],
                        "email": res_query["data"]["projCustEnterpriseVMList"][0]["email"],
                        "authId":  res_query["data"]["projCustEnterpriseVMList"][0]["authId"],
                        "shareholdingStructureList": [],
                        "idArray": ["120000", "120100", "120101"],
                        "internationalIndustryType": ["A", "A01", "A011", "A0111"],
                        "registration": ["110000", "110100", "110101"],
                        "certificateValidStartDate": "2023-12-25",
                        "certificateValidEndDate": "2099-12-31",
                    }]
            }
        elif guarantor == '3':
            data = {
                "projectNo": projectNo,
                "actualController": {
                    "id": jsonpath.jsonpath(res_query, '$..actualController.id')[0],
                    "projectNo": projectNo,
                    "sourceId": jsonpath.jsonpath(res_query, '$..actualController.sourceId')[0],
                    "enterpriseInfoId": jsonpath.jsonpath(res_query, '$..actualController.enterpriseInfoId')[0],
                    "roleType": "6",
                    "resolutionType": None,
                    "resolutionTypeName": None,
                    "name": jsonpath.jsonpath(res_query, '$..actualController.name')[0],
                    "idCardType": jsonpath.jsonpath(res_query, '$..actualController.idCardType')[0],
                    "idCardTypeName": jsonpath.jsonpath(res_query, '$..actualController.idCardTypeName')[0],
                    "idCardNo": jsonpath.jsonpath(res_query, '$..actualController.idCardNo')[0],
                    "mobile": jsonpath.jsonpath(res_query, '$..actualController.mobile')[0],
                    "shareholdingRatio": None,
                    "renterRelationship": None,
                    "residenceAddress": None,
                    "creditReportTime": None,
                    "authId": jsonpath.jsonpath(res_query, '$..actualController.authId')[0],
                    "idProvince": "110000",
                    "idProvinceName": "北京市",
                    "idCity": "110100",
                    "idCityName": "市辖区",
                    "idLocation": "110101",
                    "idLocationName": "东城区",
                    "idAddress": "上海",
                    "idArray": ["110000", "110100", "110101"],
                    "certificateValidStartDate": "2023-12-25",
                    "certificateValidEndDate": "2099-12-31",
                },
                "legalRepresentative": {
                    "id": jsonpath.jsonpath(res_query, '$..legalRepresentative.id')[0],
                    "projectNo": projectNo,
                    "sourceId": jsonpath.jsonpath(res_query, '$..legalRepresentative.sourceId')[0],
                    "enterpriseInfoId": jsonpath.jsonpath(res_query, '$..legalRepresentative.enterpriseInfoId')[0],
                    "roleType": "4",
                    "resolutionType": None,
                    "name": jsonpath.jsonpath(res_query, '$..legalRepresentative.name')[0],
                    "idCardType": jsonpath.jsonpath(res_query, '$..legalRepresentative.idCardType')[0],
                    "idCardTypeName": jsonpath.jsonpath(res_query, '$..legalRepresentative.idCardTypeName')[0],
                    "idCardNo": jsonpath.jsonpath(res_query, '$..legalRepresentative.idCardNo')[0],
                    "mobile": jsonpath.jsonpath(res_query, '$..legalRepresentative.mobile')[0],
                    "shareholdingRatio": None,
                    "renterRelationship": None,
                    "residenceAddress": None,
                    "creditReportTime": None,
                    "authId": jsonpath.jsonpath(res_query, '$..legalRepresentative.authId')[0],
                    "idProvince": "110000",
                    "idProvinceName": "北京市",
                    "idCity": "110100",
                    "idCityName": "市辖区",
                    "idLocation": "110101",
                    "idLocationName": "东城区",
                    "idAddress": "上海",
                    "idArray": ["110000", "110100", "110101"],
                    "certificateValidStartDate": "2023-12-25",
                    "certificateValidEndDate": "2099-12-31",
                },
                "beneficiary": {
                    "authId": jsonpath.jsonpath(res_credit, '$..id')[0],
                    "name": jsonpath.jsonpath(res_credit, '$..creditCustomerName')[0],
                    "idCardNo": jsonpath.jsonpath(res_credit, '$..creditCustomerNo')[0],
                    "idCardType": jsonpath.jsonpath(res_credit, '$..creditCustomerIdType')[0],
                    "idCardTypeName": jsonpath.jsonpath(res_credit, '$..creditCustomerIdTypeName')[0],
                    "residenceAddress": jsonpath.jsonpath(res_credit, '$..creditCustomerAddress')[0],
                    "idArray": ["110000", "110100", "110101"],
                    "idProvince": "110000",
                    "idCity": "110100",
                    "idLocation": "110101",
                    "certificateValidStartDate": "2023-12-25",
                    "certificateValidEndDate": "2099-12-31",
                },
                "personalIds": [],
                "custEnterpriseIds": [],
                "personalInfoModels": [
                    {
                        "id": res_query["data"]["personalInfoModels"][0]["id"],
                        "projectNo": projectNo,
                        "projectCustomerInfoId": res_query["data"]["personalInfoModels"][0]["projectCustomerInfoId"],
                        "sourceId": res_query["data"]["personalInfoModels"][0]["sourceId"],
                        "roleType": res_query["data"]["personalInfoModels"][0]["roleType"],
                        "name": res_query["data"]["personalInfoModels"][0]["name"],
                        "idCardType": res_query["data"]["personalInfoModels"][0]["idCardType"],
                        "idCardTypeName": res_query["data"]["personalInfoModels"][0]["idCardTypeName"],
                        "idCardNo": res_query["data"]["personalInfoModels"][0]["idCardNo"],
                        "mobile": res_query["data"]["personalInfoModels"][0]["mobile"],
                        "country": "156",
                        "countryName": None,
                        "actualControllerRelationship": "director",
                        "actualControllerRelationshipName": None,
                        "maritalStatus": "MARRIED",
                        "maritalStatusName": None,
                        "gender": "1",
                        "genderName": None,
                        "birthDate": "1980-07-28",
                        "nation": "22",
                        "nationName": None,
                        "education": "1010",
                        "educationName": None,
                        "annualIncome": "1000.00",
                        "idProvince": "110000",
                        "idProvinceName": None,
                        "idCity": "110100",
                        "idCityName": None,
                        "idLocation": "110101",
                        "idLocationName": None,
                        "idAddress": res_query["data"]["personalInfoModels"][0]["idAddress"],
                        "creditReportTime": None,
                        "email": "666@163.com",
                        "authId": res_query["data"]["personalInfoModels"][0]["authId"],
                        "idArray": [
                            "110000",
                            "110100",
                            "110101"
                        ],
                        "certificateValidStartDate": "2023-12-25",
                        "certificateValidEndDate": "2099-12-31",
                    },
                    {
                        "id": res_query["data"]["personalInfoModels"][1]["id"],
                        "projectNo": projectNo,
                        "projectCustomerInfoId": res_query["data"]["personalInfoModels"][1]["projectCustomerInfoId"],
                        "sourceId": res_query["data"]["personalInfoModels"][1]["sourceId"],
                        "roleType": res_query["data"]["personalInfoModels"][1]["roleType"],
                        "name": res_query["data"]["personalInfoModels"][1]["name"],
                        "idCardType": res_query["data"]["personalInfoModels"][1]["idCardType"],
                        "idCardTypeName": res_query["data"]["personalInfoModels"][1]["idCardTypeName"],
                        "idCardNo": res_query["data"]["personalInfoModels"][1]["idCardNo"],
                        "mobile": res_query["data"]["personalInfoModels"][1]["mobile"],
                        "country": "156",
                        "countryName": None,
                        "actualControllerRelationship": "director",
                        "actualControllerRelationshipName": None,
                        "maritalStatus": "MARRIED",
                        "maritalStatusName": None,
                        "gender": "1",
                        "genderName": None,
                        "birthDate": "1980-07-28",
                        "nation": "22",
                        "nationName": None,
                        "education": "1010",
                        "educationName": None,
                        "annualIncome": "1000.00",
                        "idProvince": "110000",
                        "idProvinceName": None,
                        "idCity": "110100",
                        "idCityName": None,
                        "idLocation": "110101",
                        "idLocationName": None,
                        "idAddress": res_query["data"]["personalInfoModels"][1]["idAddress"],
                        "creditReportTime": None,
                        "email": "666@163.com",
                        "authId": res_query["data"]["personalInfoModels"][1]["authId"],
                        "idArray": [
                            "110000",
                            "110100",
                            "110101"
                        ],
                        "certificateValidStartDate": "2023-12-25",
                        "certificateValidEndDate": "2099-12-31",
                    }
                ],
                "projCustEnterpriseVMList": [
                    {
                        "id": res_query["data"]["projCustEnterpriseVMList"][0]["id"],
                        "projectNo": projectNo,
                        "sourceId": res_query["data"]["projCustEnterpriseVMList"][0]["sourceId"],
                        "projectCustomerInfoId": res_query["data"]["projCustEnterpriseVMList"][0]["projectCustomerInfoId"],
                        "roleType": res_query["data"]["projCustEnterpriseVMList"][0]["roleType"],
                        "name": res_query["data"]["projCustEnterpriseVMList"][0]["name"],
                        "idCardType": res_query["data"]["projCustEnterpriseVMList"][0]["idCardType"],
                        "idCardTypeName": res_query["data"]["projCustEnterpriseVMList"][0]["idCardTypeName"],
                        "idCardNo": res_query["data"]["projCustEnterpriseVMList"][0]["idCardNo"],
                        "mobile": None,
                        "country": res_query["data"]["projCustEnterpriseVMList"][0]["country"],
                        "countryName": res_query["data"]["projCustEnterpriseVMList"][0]["countryName"],
                        "interIndustryClassifyOneName": res_query["data"]["projCustEnterpriseVMList"][0]["interIndustryClassifyOneName"],
                        "interIndustryClassifyOne": res_query["data"]["projCustEnterpriseVMList"][0]["interIndustryClassifyOne"],
                        "interIndustryClassifyTwoName": res_query["data"]["projCustEnterpriseVMList"][0]["interIndustryClassifyTwoName"],
                        "interIndustryClassifyTwo": res_query["data"]["projCustEnterpriseVMList"][0]["interIndustryClassifyTwo"],
                        "interIndustryClassifyThreeName": res_query["data"]["projCustEnterpriseVMList"][0]["interIndustryClassifyThreeName"],
                        "interIndustryClassifyThree": res_query["data"]["projCustEnterpriseVMList"][0]["interIndustryClassifyThree"],
                        "interIndustryClassifyFourName": res_query["data"]["projCustEnterpriseVMList"][0]["interIndustryClassifyFourName"],
                        "interIndustryClassifyFour": res_query["data"]["projCustEnterpriseVMList"][0]["interIndustryClassifyFour"],
                        "industryClassifyOneName": res_query["data"]["projCustEnterpriseVMList"][0]["industryClassifyOneName"],
                        "industryClassifyOne": res_query["data"]["projCustEnterpriseVMList"][0]["industryClassifyOne"],
                        "industryClassifyTwoName": res_query["data"]["projCustEnterpriseVMList"][0]["industryClassifyTwoName"],
                        "industryClassifyTwo": res_query["data"]["projCustEnterpriseVMList"][0]["industryClassifyTwo"],
                        "registrationProvinceName": res_query["data"]["projCustEnterpriseVMList"][0]["registrationProvinceName"],
                        "registrationProvince": res_query["data"]["projCustEnterpriseVMList"][0]["registrationProvince"],
                        "registrationCityName": res_query["data"]["projCustEnterpriseVMList"][0]["registrationCityName"],
                        "registrationCity": res_query["data"]["projCustEnterpriseVMList"][0]["registrationCity"],
                        "registrationRegionName": res_query["data"]["projCustEnterpriseVMList"][0]["registrationRegionName"],
                        "registrationRegion": res_query["data"]["projCustEnterpriseVMList"][0]["registrationRegion"],
                        "registrationAddress": res_query["data"]["projCustEnterpriseVMList"][0]["registrationAddress"],
                        "officeProvinceName": res_query["data"]["projCustEnterpriseVMList"][0]["officeProvinceName"],
                        "officeProvince": res_query["data"]["projCustEnterpriseVMList"][0]["officeProvince"],
                        "officeCityName": res_query["data"]["projCustEnterpriseVMList"][0]["officeCityName"],
                        "officeCity": res_query["data"]["projCustEnterpriseVMList"][0]["officeCity"],
                        "officeLocationName": res_query["data"]["projCustEnterpriseVMList"][0]["officeLocationName"],
                        "officeLocation": res_query["data"]["projCustEnterpriseVMList"][0]["officeLocation"],
                        "officeAddress": res_query["data"]["projCustEnterpriseVMList"][0]["officeAddress"],
                        "actualBusinessProvinceName": res_query["data"]["projCustEnterpriseVMList"][0]["actualBusinessProvinceName"],
                        "actualBusinessProvince": res_query["data"]["projCustEnterpriseVMList"][0]["actualBusinessProvince"],
                        "actualBusinessCityName": res_query["data"]["projCustEnterpriseVMList"][0]["actualBusinessCityName"],
                        "actualBusinessCity": res_query["data"]["projCustEnterpriseVMList"][0]["actualBusinessCity"],
                        "actualBusinessLocationName": res_query["data"]["projCustEnterpriseVMList"][0]["actualBusinessLocationName"],
                        "actualBusinessLocation": res_query["data"]["projCustEnterpriseVMList"][0]["actualBusinessLocation"],
                        "actualBusinessAddress": res_query["data"]["projCustEnterpriseVMList"][0]["actualBusinessAddress"],
                        "rentStockholderRelated": res_query["data"]["projCustEnterpriseVMList"][0]["rentStockholderRelated"],
                        "rentRelated": res_query["data"]["projCustEnterpriseVMList"][0]["rentRelated"],
                        "ruralUrbanSignageName": res_query["data"]["projCustEnterpriseVMList"][0]["ruralUrbanSignageName"],
                        "ruralUrbanSignage": res_query["data"]["projCustEnterpriseVMList"][0]["ruralUrbanSignage"],
                        "projectSourceName": res_query["data"]["projCustEnterpriseVMList"][0]["projectSourceName"],
                        "projectSource": res_query["data"]["projCustEnterpriseVMList"][0]["projectSource"],
                        "licProjectInvestmentOneName": res_query["data"]["projCustEnterpriseVMList"][0]["licProjectInvestmentOneName"],
                        "licProjectInvestmentOne": res_query["data"]["projCustEnterpriseVMList"][0]["licProjectInvestmentOne"],
                        "licProjectInvestmentTwoName": res_query["data"]["projCustEnterpriseVMList"][0]["licProjectInvestmentTwoName"],
                        "licProjectInvestmentTwo": res_query["data"]["projCustEnterpriseVMList"][0]["licProjectInvestmentTwo"],
                        "licProjectInvestmentThreeName": res_query["data"]["projCustEnterpriseVMList"][0]["licProjectInvestmentThreeName"],
                        "licProjectInvestmentThree": res_query["data"]["projCustEnterpriseVMList"][0]["licProjectInvestmentThree"],
                        "licProjectInvestmentFourName": res_query["data"]["projCustEnterpriseVMList"][0]["licProjectInvestmentFourName"],
                        "licProjectInvestmentFour": res_query["data"]["projCustEnterpriseVMList"][0]["licProjectInvestmentFour"],
                        "businessScope": res_query["data"]["projCustEnterpriseVMList"][0]["businessScope"],
                        "mainBusinessProducts": res_query["data"]["projCustEnterpriseVMList"][0]["mainBusinessProducts"],
                        "enterpriseSizeName": res_query["data"]["projCustEnterpriseVMList"][0]["enterpriseSizeName"],
                        "enterpriseSize": res_query["data"]["projCustEnterpriseVMList"][0]["enterpriseSize"],
                        "enterpriseType": res_query["data"]["projCustEnterpriseVMList"][0]["enterpriseType"],
                        "enterpriseTypeName": None,
                        "institutionRegistCertNumber": None,
                        "financialInstitutionCode": None,
                        "holdingTypeOne": res_query["data"]["projCustEnterpriseVMList"][0]["holdingTypeOne"],
                        "holdingTypeTwo": res_query["data"]["projCustEnterpriseVMList"][0]["holdingTypeTwo"],
                        "holdingTypeThree": res_query["data"]["projCustEnterpriseVMList"][0]["holdingTypeThree"],
                        "holdingTypeOneName": res_query["data"]["projCustEnterpriseVMList"][0]["holdingTypeOneName"],
                        "holdingTypeTwoName": res_query["data"]["projCustEnterpriseVMList"][0]["holdingTypeTwoName"],
                        "holdingTypeThreeName": res_query["data"]["projCustEnterpriseVMList"][0]["holdingTypeThreeName"],
                        "zhongzhengCode": res_query["data"]["projCustEnterpriseVMList"][0]["zhongzhengCode"],
                        "currencyName": res_query["data"]["projCustEnterpriseVMList"][0]["currencyName"],
                        "currency": res_query["data"]["projCustEnterpriseVMList"][0]["currency"],
                        "registeredCapital": res_query["data"]["projCustEnterpriseVMList"][0]["registeredCapital"],
                        "paidinCapital": res_query["data"]["projCustEnterpriseVMList"][0]["paidinCapital"],
                        "capitalization": res_query["data"]["projCustEnterpriseVMList"][0]["capitalization"],
                        "revenue": res_query["data"]["projCustEnterpriseVMList"][0]["revenue"],
                        "establishmentTime": res_query["data"]["projCustEnterpriseVMList"][0]["establishmentTime"],
                        "businessLicenseExpirationDate": res_query["data"]["projCustEnterpriseVMList"][0]["businessLicenseExpirationDate"],
                        "businessStatus": res_query["data"]["projCustEnterpriseVMList"][0]["businessStatus"],
                        "businessStatusName": res_query["data"]["projCustEnterpriseVMList"][0]["businessStatusName"],
                        "employeeNumber": res_query["data"]["projCustEnterpriseVMList"][0]["employeeNumber"],
                        "legalRepresentative": res_query["data"]["projCustEnterpriseVMList"][0]["legalRepresentative"],
                        "legalRepresentativeMobile": res_query["data"]["projCustEnterpriseVMList"][0]["legalRepresentativeMobile"],
                        "idProvince": "120000",
                        "idProvinceName": None,
                        "idCity": "120100",
                        "idCityName": None,
                        "idLocation": "120101",
                        "idLocationName": None,
                        "idAddress": res_query["data"]["projCustEnterpriseVMList"][0]["idAddress"],
                        "legalPersonPhone": res_query["data"]["projCustEnterpriseVMList"][0]["legalPersonPhone"],
                        "actualController": res_query["data"]["projCustEnterpriseVMList"][0]["actualController"],
                        "nationalEconomyOne": res_query["data"]["projCustEnterpriseVMList"][0]["nationalEconomyOne"],
                        "nationalEconomyOneName": res_query["data"]["projCustEnterpriseVMList"][0]["nationalEconomyOneName"],
                        "nationalEconomyTwo": res_query["data"]["projCustEnterpriseVMList"][0]["nationalEconomyTwo"],
                        "nationalEconomyTwoName": res_query["data"]["projCustEnterpriseVMList"][0]["nationalEconomyTwoName"],
                        "listedCompanyLogoName": res_query["data"]["projCustEnterpriseVMList"][0]["listedCompanyLogoName"],
                        "listedCompanyLogo": res_query["data"]["projCustEnterpriseVMList"][0]["listedCompanyLogo"],
                        "resolutionType": res_query["data"]["projCustEnterpriseVMList"][0]["resolutionType"],
                        "resolutionTypeName": res_query["data"]["projCustEnterpriseVMList"][0]["resolutionTypeName"],
                        "email": res_query["data"]["projCustEnterpriseVMList"][0]["email"],
                        "authId": res_query["data"]["projCustEnterpriseVMList"][0]["authId"],
                        "shareholdingStructureList": [],
                        "idArray": ["120000", "120100", "120101"],
                        "internationalIndustryType": ["A", "A01", "A011", "A0111"],
                        "registration": ["110000", "110100", "110101"],
                        "certificateValidStartDate": "2023-12-25",
                        "certificateValidEndDate": "2099-12-31",
                    },
                    {
                        "id": res_query["data"]["projCustEnterpriseVMList"][1]["id"],
                        "projectNo": projectNo,
                        "sourceId": res_query["data"]["projCustEnterpriseVMList"][1]["sourceId"],
                        "projectCustomerInfoId": res_query["data"]["projCustEnterpriseVMList"][1]["projectCustomerInfoId"],
                        "roleType": res_query["data"]["projCustEnterpriseVMList"][1]["roleType"],
                        "name": res_query["data"]["projCustEnterpriseVMList"][1]["name"],
                        "idCardType": res_query["data"]["projCustEnterpriseVMList"][1]["idCardType"],
                        "idCardTypeName": res_query["data"]["projCustEnterpriseVMList"][1]["idCardTypeName"],
                        "idCardNo": res_query["data"]["projCustEnterpriseVMList"][1]["idCardNo"],
                        "mobile": None,
                        "country": res_query["data"]["projCustEnterpriseVMList"][1]["country"],
                        "countryName": res_query["data"]["projCustEnterpriseVMList"][1]["countryName"],
                        "interIndustryClassifyOneName": res_query["data"]["projCustEnterpriseVMList"][1]["interIndustryClassifyOneName"],
                        "interIndustryClassifyOne": res_query["data"]["projCustEnterpriseVMList"][1]["interIndustryClassifyOne"],
                        "interIndustryClassifyTwoName": res_query["data"]["projCustEnterpriseVMList"][1]["interIndustryClassifyTwoName"],
                        "interIndustryClassifyTwo": res_query["data"]["projCustEnterpriseVMList"][1]["interIndustryClassifyTwo"],
                        "interIndustryClassifyThreeName": res_query["data"]["projCustEnterpriseVMList"][1]["interIndustryClassifyThreeName"],
                        "interIndustryClassifyThree": res_query["data"]["projCustEnterpriseVMList"][1]["interIndustryClassifyThree"],
                        "interIndustryClassifyFourName": res_query["data"]["projCustEnterpriseVMList"][1]["interIndustryClassifyFourName"],
                        "interIndustryClassifyFour": res_query["data"]["projCustEnterpriseVMList"][1]["interIndustryClassifyFour"],
                        "industryClassifyOneName": res_query["data"]["projCustEnterpriseVMList"][1]["industryClassifyOneName"],
                        "industryClassifyOne": res_query["data"]["projCustEnterpriseVMList"][1]["industryClassifyOne"],
                        "industryClassifyTwoName": res_query["data"]["projCustEnterpriseVMList"][1]["industryClassifyTwoName"],
                        "industryClassifyTwo": res_query["data"]["projCustEnterpriseVMList"][1]["industryClassifyTwo"],
                        "registrationProvinceName": res_query["data"]["projCustEnterpriseVMList"][1]["registrationProvinceName"],
                        "registrationProvince": res_query["data"]["projCustEnterpriseVMList"][1]["registrationProvince"],
                        "registrationCityName": res_query["data"]["projCustEnterpriseVMList"][1]["registrationCityName"],
                        "registrationCity": res_query["data"]["projCustEnterpriseVMList"][1]["registrationCity"],
                        "registrationRegionName": res_query["data"]["projCustEnterpriseVMList"][1]["registrationRegionName"],
                        "registrationRegion": res_query["data"]["projCustEnterpriseVMList"][1]["registrationRegion"],
                        "registrationAddress": res_query["data"]["projCustEnterpriseVMList"][1]["registrationAddress"],
                        "officeProvinceName": res_query["data"]["projCustEnterpriseVMList"][1]["officeProvinceName"],
                        "officeProvince": res_query["data"]["projCustEnterpriseVMList"][1]["officeProvince"],
                        "officeCityName": res_query["data"]["projCustEnterpriseVMList"][1]["officeCityName"],
                        "officeCity": res_query["data"]["projCustEnterpriseVMList"][1]["officeCity"],
                        "officeLocationName": res_query["data"]["projCustEnterpriseVMList"][1]["officeLocationName"],
                        "officeLocation": res_query["data"]["projCustEnterpriseVMList"][1]["officeLocation"],
                        "officeAddress": res_query["data"]["projCustEnterpriseVMList"][1]["officeAddress"],
                        "actualBusinessProvinceName": res_query["data"]["projCustEnterpriseVMList"][1]["actualBusinessProvinceName"],
                        "actualBusinessProvince": res_query["data"]["projCustEnterpriseVMList"][1]["actualBusinessProvince"],
                        "actualBusinessCityName": res_query["data"]["projCustEnterpriseVMList"][1]["actualBusinessCityName"],
                        "actualBusinessCity": res_query["data"]["projCustEnterpriseVMList"][1]["actualBusinessCity"],
                        "actualBusinessLocationName": res_query["data"]["projCustEnterpriseVMList"][1]["actualBusinessLocationName"],
                        "actualBusinessLocation": res_query["data"]["projCustEnterpriseVMList"][1]["actualBusinessLocation"],
                        "actualBusinessAddress": res_query["data"]["projCustEnterpriseVMList"][1]["actualBusinessAddress"],
                        "rentStockholderRelated": res_query["data"]["projCustEnterpriseVMList"][1]["rentStockholderRelated"],
                        "rentRelated": res_query["data"]["projCustEnterpriseVMList"][1]["rentRelated"],
                        "ruralUrbanSignageName": res_query["data"]["projCustEnterpriseVMList"][1]["ruralUrbanSignageName"],
                        "ruralUrbanSignage": res_query["data"]["projCustEnterpriseVMList"][1]["ruralUrbanSignage"],
                        "projectSourceName": res_query["data"]["projCustEnterpriseVMList"][1]["projectSourceName"],
                        "projectSource": res_query["data"]["projCustEnterpriseVMList"][1]["projectSource"],
                        "licProjectInvestmentOneName": res_query["data"]["projCustEnterpriseVMList"][1]["licProjectInvestmentOneName"],
                        "licProjectInvestmentOne": res_query["data"]["projCustEnterpriseVMList"][1]["licProjectInvestmentOne"],
                        "licProjectInvestmentTwoName": res_query["data"]["projCustEnterpriseVMList"][1]["licProjectInvestmentTwoName"],
                        "licProjectInvestmentTwo": res_query["data"]["projCustEnterpriseVMList"][1]["licProjectInvestmentTwo"],
                        "licProjectInvestmentThreeName": res_query["data"]["projCustEnterpriseVMList"][1]["licProjectInvestmentThreeName"],
                        "licProjectInvestmentThree": res_query["data"]["projCustEnterpriseVMList"][1]["licProjectInvestmentThree"],
                        "licProjectInvestmentFourName": res_query["data"]["projCustEnterpriseVMList"][1]["licProjectInvestmentFourName"],
                        "licProjectInvestmentFour": res_query["data"]["projCustEnterpriseVMList"][1]["licProjectInvestmentFour"],
                        "businessScope": res_query["data"]["projCustEnterpriseVMList"][1]["businessScope"],
                        "mainBusinessProducts": res_query["data"]["projCustEnterpriseVMList"][1]["mainBusinessProducts"],
                        "enterpriseSizeName": res_query["data"]["projCustEnterpriseVMList"][1]["enterpriseSizeName"],
                        "enterpriseSize": res_query["data"]["projCustEnterpriseVMList"][1]["enterpriseSize"],
                        "enterpriseType": res_query["data"]["projCustEnterpriseVMList"][1]["enterpriseType"],
                        "enterpriseTypeName": None,
                        "institutionRegistCertNumber": None,
                        "financialInstitutionCode": None,
                        "holdingTypeOne": res_query["data"]["projCustEnterpriseVMList"][1]["holdingTypeOne"],
                        "holdingTypeTwo": res_query["data"]["projCustEnterpriseVMList"][1]["holdingTypeTwo"],
                        "holdingTypeThree": res_query["data"]["projCustEnterpriseVMList"][1]["holdingTypeThree"],
                        "holdingTypeOneName": res_query["data"]["projCustEnterpriseVMList"][1]["holdingTypeOneName"],
                        "holdingTypeTwoName": res_query["data"]["projCustEnterpriseVMList"][1]["holdingTypeTwoName"],
                        "holdingTypeThreeName": res_query["data"]["projCustEnterpriseVMList"][1]["holdingTypeThreeName"],
                        "zhongzhengCode": res_query["data"]["projCustEnterpriseVMList"][1]["zhongzhengCode"],
                        "currencyName": res_query["data"]["projCustEnterpriseVMList"][1]["currencyName"],
                        "currency": res_query["data"]["projCustEnterpriseVMList"][1]["currency"],
                        "registeredCapital": res_query["data"]["projCustEnterpriseVMList"][1]["registeredCapital"],
                        "paidinCapital": res_query["data"]["projCustEnterpriseVMList"][1]["paidinCapital"],
                        "capitalization": res_query["data"]["projCustEnterpriseVMList"][1]["capitalization"],
                        "revenue": res_query["data"]["projCustEnterpriseVMList"][1]["revenue"],
                        "establishmentTime": res_query["data"]["projCustEnterpriseVMList"][1]["establishmentTime"],
                        "businessLicenseExpirationDate": res_query["data"]["projCustEnterpriseVMList"][1]["businessLicenseExpirationDate"],
                        "businessStatus": res_query["data"]["projCustEnterpriseVMList"][1]["businessStatus"],
                        "businessStatusName": res_query["data"]["projCustEnterpriseVMList"][1]["businessStatusName"],
                        "employeeNumber": res_query["data"]["projCustEnterpriseVMList"][1]["employeeNumber"],
                        "legalRepresentative": res_query["data"]["projCustEnterpriseVMList"][1]["legalRepresentative"],
                        "legalRepresentativeMobile": res_query["data"]["projCustEnterpriseVMList"][1]["legalRepresentativeMobile"],
                        "idProvince": "120000",
                        "idProvinceName": None,
                        "idCity": "120100",
                        "idCityName": None,
                        "idLocation": "120101",
                        "idLocationName": None,
                        "idAddress": res_query["data"]["projCustEnterpriseVMList"][1]["idAddress"],
                        "legalPersonPhone": res_query["data"]["projCustEnterpriseVMList"][1]["legalPersonPhone"],
                        "actualController": res_query["data"]["projCustEnterpriseVMList"][1]["actualController"],
                        "nationalEconomyOne": res_query["data"]["projCustEnterpriseVMList"][1]["nationalEconomyOne"],
                        "nationalEconomyOneName": res_query["data"]["projCustEnterpriseVMList"][1]["nationalEconomyOneName"],
                        "nationalEconomyTwo": res_query["data"]["projCustEnterpriseVMList"][1]["nationalEconomyTwo"],
                        "nationalEconomyTwoName": res_query["data"]["projCustEnterpriseVMList"][1]["nationalEconomyTwoName"],
                        "listedCompanyLogoName": res_query["data"]["projCustEnterpriseVMList"][1]["listedCompanyLogoName"],
                        "listedCompanyLogo": res_query["data"]["projCustEnterpriseVMList"][1]["listedCompanyLogo"],
                        "resolutionType": res_query["data"]["projCustEnterpriseVMList"][1]["resolutionType"],
                        "resolutionTypeName": res_query["data"]["projCustEnterpriseVMList"][1]["resolutionTypeName"],
                        "email": res_query["data"]["projCustEnterpriseVMList"][1]["email"],
                        "authId": res_query["data"]["projCustEnterpriseVMList"][1]["authId"],
                        "shareholdingStructureList": [],
                        "idArray": ["120000", "120100", "120101"],
                        "internationalIndustryType": ["A", "A01", "A011", "A0111"],
                        "registration": ["110000", "110100", "110101"],
                        "certificateValidStartDate": "2023-12-25",
                        "certificateValidEndDate": "2099-12-31",
                    }
                ]
            }
        res = self.api(method = 'POST', url =url,json = data)

    # '''交易结构-增加'''
    # def projTradeAdd(self,projectNo):
    #     trade = []
    #     url = 'ifc/api/credit-apply/trades/addProjTrades'
    #     data = {
    #         "projectNo": projectNo
    #     }
    #     for i in range(9):
    #         res = self.api(method='POST', url=url, json=data)
    #         trade.append(res)
    #     return trade

    '''交易结构-增加'''

    def projTradeAdd(self, projectNo):
        url = 'ifc/api/credit-apply/trades/addProjTrades'
        data = {
            "projectNo": projectNo
        }
        res = self.api(method='POST', url=url, json=data)
        return res



    # '''供应商保存'''
    # def supplierSave(self, projectNo, custName,env, id_1, id_2, id_3, id_4, id_5, id_6, id_7, id_8, id_9):
    #     if custName == 'ph_sd':
    #         custName = 'jxw'
    #     url = 'ifc/api/credit-apply/trades/saveSupplier'
    #     if env == 'sit':
    #         data_before = {"xzw": {"supplierId": "311258",
    #                         "supplierName": "测试Z500供应商合同公司J2",
    #                         "certId": "91120000WH9CX8CE5N",
    #                         "artificialPerson": "季晓伟",
    #                         "registerFullAddress": "120000|120100|120102;天津市|市辖区|河东区|注册地详细地址",
	# 		                "businessAddress": "120000|120100|120102;天津市|市辖区|河东区|实际经营地址\n"},
    #                 "jxw": {"supplierId": "311258",
    #                         "supplierName": "测试Z500供应商合同公司J2",
    #                         "certId": "91120000WH9CX8CE5N",
    #                         "artificialPerson": "季晓伟",
    #                         "registerFullAddress": "120000|120100|120102;天津市|市辖区|河东区|注册地详细地址",
	# 		                "businessAddress": "120000|120100|120102;天津市|市辖区|河东区|实际经营地址\n"},
    #                 "fht": {"supplierId": "311226",
    #                         "supplierName": "测试进秧贸易有限公司",
    #                         "certId": "91140105MA0KKTAU26",
    #                         "artificialPerson": "范怀通",
    #                         "registerFullAddress": "410000|411600|411681;河南省|周口市|项城市|迎宾大道1号",
	# 		                "businessAddress": "410000|411600|411681;河南省|周口市|项城市|迎宾大道1号"},
    #                 "zll": {"supplierId": "311230",
    #                         "supplierName": "测试Z500供应商合同公司1",
    #                         "certId": "91350102315514081E",
    #                         "artificialPerson": "张玲玲",
    #                         "registerFullAddress": "130000|130300|130306;河北省|秦皇岛市|抚宁区|阜宁",
	# 		                "businessAddress": "130000|130300|130306;河北省|秦皇岛市|抚宁区|阜宁"},
    #                 "cm": {"supplierId": "311225",
    #                         "supplierName": "测试Z500供应商合同公司J1",
    #                         "certId": "91110000FB0RBU0R7P",
    #                         "artificialPerson": "季晓伟",
    #                         "registerFullAddress": "130000|130300|130304;河北省|秦皇岛市|北戴河区|测试",
	# 		                "businessAddress": "130000|130300|130304;河北省|秦皇岛市|北戴河区|测试"}
    #             }
    #         data_after = {"xzw": {"supplierId": "311258",
    #                                "supplierName": "测试Z500供应商合同公司J2",
    #                                "certId": "91120000WH9CX8CE5N",
    #                                "artificialPerson": "季晓伟",
    #                                "registerFullAddress": "120000|120100|120102;天津市|市辖区|河东区|注册地详细地址",
    #                                "businessAddress": "120000|120100|120102;天津市|市辖区|河东区|实际经营地址\n"},
    #                        "jxw": {"supplierId": "311225",
    #                                "supplierName": "测试Z500供应商合同公司J1",
    #                                "certId": "91110000FB0RBU0R7P",
    #                                "artificialPerson": "季晓伟",
    #                                "registerFullAddress": "130000|130300|130304;河北省|秦皇岛市|北戴河区|测试",
    #                                "businessAddress": "130000|130300|130304;河北省|秦皇岛市|北戴河区|测试"},
    #                        "fht": {"supplierId": "311261",
    #                                "supplierName": "测试供应商F1",
    #                                "certId": "91410100732484450",
    #                                "artificialPerson": "范怀通",
    #                                "registerFullAddress": "410000|410100|410102;河南省|郑州市|中原区|宇工路88号",
    #                                "businessAddress": "410000|410100|410102;河南省|郑州市|中原区|宇工路88号"},
    #                        "zll": {"supplierId": "311231",
    #                                "supplierName": "测试Z500上海锦珂供应商公司",
    #                                "certId": "91510104MA69KTF77Q",
    #                                "artificialPerson": "张玲玲",
    #                                "registerFullAddress": "130000|130600|130608;河北省|保定市|清苑区|浦东",
    #                                "businessAddress": "130000|130600|130608;河北省|保定市|清苑区|浦东"},
    #                        "cm": {"supplierId": "311225",
    #                               "supplierName": "测试Z500供应商合同公司J1",
    #                               "certId": "91110000FB0RBU0R7P",
    #                               "artificialPerson": "季晓伟",
    #                               "registerFullAddress": "130000|130300|130304;河北省|秦皇岛市|北戴河区|测试",
    #                               "businessAddress": "130000|130300|130304;河北省|秦皇岛市|北戴河区|测试"}
    #                        }
    #     else:
    #         data_before = {"xzw": {"supplierId": "9820",
    #                         "supplierName": "测试Z500供应商合同公司1",
    #                         "certId": "91350102315514081E",
    #                         "artificialPerson": "夏紫文",
    #                         "registerFullAddress": "110000|110100|110111;北京市|市辖区|房山区|123123",
    #                         "businessAddress": "110000|110100|110111;北京市|市辖区|房山区|123123"},
    #                 "jxw": {"supplierId": "9871",
    #                         "supplierName": "测试Z500供应商合同公司J3",
    #                         "certId": "91330100ANTABEFN09",
    #                         "artificialPerson": "季晓伟",
    #                         "registerFullAddress": "120000|120100|120102;天津市|市辖区|河东区|测试",
    #                         "businessAddress": "120000|120100|120102;天津市|市辖区|河东区|测试"},
    #                 "fht": {"supplierId": "9837",
    #                         "supplierName": "测试Z500公司F4",
    #                         "certId": "9131000071785090X1",
    #                         "artificialPerson": "范怀通",
    #                         "registerFullAddress": "310000|310100|310104;上海市|市辖区|徐汇区|龙华中路1号",
    #                         "businessAddress": "310000|310100|310104;上海市|市辖区|徐汇区|龙华中路1号"},
    #                 "zll": {"supplierId": "9841",
    #                         "supplierName": "测试Z500供应商合同公司J2",
    #                         "certId": "91120000WH9CX8CE5N",
    #                         "artificialPerson": "季晓伟",
    #                         "registerFullAddress": "120000|120100|120101;天津市|市辖区|和平区",
    #                         "businessAddress": "120000|120100|120101;天津市|市辖区|和平区"},
    #                 "cm": {"supplierId": "9852",
    #                        "supplierName": "测试Z500特斯拉",
    #                        "certId": "91310115MA1H9YGWXX",
    #                        "artificialPerson": "陈鸣",
    #                        "registerFullAddress": "110000|110100|110105;北京市|市辖区|朝阳区|注册详细地址",
    #                        "businessAddress": "110000|110100|110105;北京市|市辖区|朝阳区|注册详细地址"}
    #                 }
    #         data_after = {"xzw": {"supplierId": "9820",
    #                                "supplierName": "测试Z500供应商合同公司1",
    #                                "certId": "91350102315514081E",
    #                                "artificialPerson": "夏紫文",
    #                                "registerFullAddress": "110000|110100|110111;北京市|市辖区|房山区|123123",
    #                                "businessAddress": "110000|110100|110111;北京市|市辖区|房山区|123123"},
    #                        "jxw": {"supplierId": "9836",
    #                                "supplierName": "测试Z500供应商合同公司J1",
    #                                "certId": "91110000FB0RBU0R7P",
    #                                "artificialPerson": "季晓伟",
    #                                "registerFullAddress": "110000|110100|110101;北京市|市辖区|东城区",
    #                                "businessAddress": "110000|110100|110101;北京市|市辖区|东城区"},
    #                        "fht": {"supplierId": "9847",
    #                                "supplierName": "测试供应商F1",
    #                                "certId": "91410100732484450T",
    #                                "artificialPerson": "范怀通",
    #                                "registerFullAddress": "410000|410100|410102;河南省|郑州市|中原区|宇工路88号",
    #                                "businessAddress": "410000|410100|410102;河南省|郑州市|中原区|宇工路88号"},
    #                        "zll": {"supplierId": "9841",
    #                                "supplierName": "测试Z500供应商合同公司J2",
    #                                "certId": "91120000WH9CX8CE5N",
    #                                "artificialPerson": "季晓伟",
    #                                "registerFullAddress": "120000|120100|120101;天津市|市辖区|和平区",
    #                                "businessAddress": "120000|120100|120101;天津市|市辖区|和平区"},
    #                        "cm": {"supplierId": "9852",
    #                               "supplierName": "测试Z500特斯拉",
    #                               "certId": "91310115MA1H9YGWXX",
    #                               "artificialPerson": "陈鸣",
    #                               "registerFullAddress": "110000|110100|110105;北京市|市辖区|朝阳区|注册详细地址",
    #                               "businessAddress": "110000|110100|110105;北京市|市辖区|朝阳区|注册详细地址"}
    #                        }
    #     list = []
    #     data_1 = {
    #         "id": None,
    #         "projectNo": projectNo,
    #         "projTradesId": id_1,
    #         "supplierId": data_before[custName]["supplierId"],
    #         "supplierName": data_before[custName]["supplierName"],
    #         "certType": "200",
    #         "certId": data_before[custName]["certId"],
    #         "artificialPerson": data_before[custName]["artificialPerson"],
    #         "registerFullAddress": data_before[custName]["registerFullAddress"],
	#         "businessAddress": data_before[custName]["businessAddress"],
    #         "contacts": None,
    #         "phone": None,
    #         "openingBank": None,
    #         "openingBankNum": None,
    #         "account": None,
    #         "accountNo": None,
    #         "invoiceTitle": None,
    #         "taxQualification": None,
    #         "taxId": None,
    #         "taxTel": None,
    #         "taxAddress": None,
    #         "contractType": None,
    #         "tradeMode": "02",
    #         "tradeModeName": "货到付款",
    #         "settleMode": "BankAcceptanceBill",
    #         "settleModeName": "银行承兑汇票",
    #         "braceletInstallNode": "AfterPayment",
    #         "braceletInstallNodeName": "付款后安装",
    #         "productNodeType": "LS-DFL-I",
    #         "productNodeTypeName": "直接租赁",
    #         "isInstallBracelet": 1,
    #         "isInstallBraceletName": "是",
    #         "notePeriod": "01",
    #         "notePeriodName": "60天",
    #     }
    #     data_2 = {
    #         "id": None,
    #         "projectNo": projectNo,
    #         "projTradesId": id_2,
    #         "supplierId": data_before[custName]["supplierId"],
    #         "supplierName": data_before[custName]["supplierName"],
    #         "certType": "200",
    #         "certId": data_before[custName]["certId"],
    #         "artificialPerson": data_before[custName]["artificialPerson"],
    #         "registerFullAddress": data_before[custName]["registerFullAddress"],
	#         "businessAddress": data_before[custName]["businessAddress"],
    #         "contacts": None,
    #         "phone": None,
    #         "openingBank": None,
    #         "openingBankNum": None,
    #         "account": None,
    #         "accountNo": None,
    #         "invoiceTitle": None,
    #         "taxQualification": None,
    #         "taxId": None,
    #         "taxTel": None,
    #         "taxAddress": None,
    #         "contractType": None,
    #         "tradeMode": "02",
    #         "tradeModeName": "货到付款",
    #         "settleMode": "BankAcceptanceBill",
    #         "settleModeName": "银行承兑汇票",
    #         "braceletInstallNode": "AfterPayment",
    #         "braceletInstallNodeName": "付款后安装",
    #         "productNodeType": "LS-DFL-I",
    #         "productNodeTypeName": "直接租赁",
    #         "isInstallBracelet": 1,
    #         "isInstallBraceletName": "是",
    #         "notePeriod": "01",
    #         "notePeriodName": "60天",
    #     }
    #     data_3 = {
    #         "id": None,
    #         "projectNo": projectNo,
    #         "projTradesId": id_3,
    #         "supplierId": data_before[custName]["supplierId"],
    #         "supplierName": data_before[custName]["supplierName"],
    #         "certType": "200",
    #         "certId": data_before[custName]["certId"],
    #         "artificialPerson": data_before[custName]["artificialPerson"],
    #         "registerFullAddress": data_before[custName]["registerFullAddress"],
	#         "businessAddress": data_before[custName]["businessAddress"],
    #         "contacts": None,
    #         "phone": None,
    #         "openingBank": None,
    #         "openingBankNum": None,
    #         "account": None,
    #         "accountNo": None,
    #         "invoiceTitle": None,
    #         "taxQualification": None,
    #         "taxId": None,
    #         "taxTel": None,
    #         "taxAddress": None,
    #         "contractType": None,
    #         "tradeMode": "02",
    #         "tradeModeName": "货到付款",
    #         "settleMode": "BankAcceptanceBill",
    #         "settleModeName": "银行承兑汇票",
    #         "braceletInstallNode": "AfterPayment",
    #         "braceletInstallNodeName": "付款后安装",
    #         "productNodeType": "LS-DFL-I",
    #         "productNodeTypeName": "直接租赁",
    #         "isInstallBracelet": 1,
    #         "isInstallBraceletName": "是",
    #         "notePeriod": "01",
    #         "notePeriodName": "60天",
    #     }
    #
    #
    #     data_4 = {
    #         "id": None,
    #         "projectNo": projectNo,
    #         "projTradesId": id_4,
    #         "supplierId": data_before[custName]["supplierId"],
    #         "supplierName": data_before[custName]["supplierName"],
    #         "certType": "200",
    #         "certId": data_before[custName]["certId"],
    #         "artificialPerson": data_before[custName]["artificialPerson"],
    #         "registerFullAddress": data_before[custName]["registerFullAddress"],
	#         "businessAddress": data_before[custName]["businessAddress"],
    #         "contacts": None,
    #         "phone": None,
    #         "openingBank": None,
    #         "openingBankNum": None,
    #         "account": None,
    #         "accountNo": None,
    #         "invoiceTitle": None,
    #         "taxQualification": None,
    #         "taxId": None,
    #         "taxTel": None,
    #         "taxAddress": None,
    #         "contractType": None,
    #         "tradeMode": "02",
    #         "tradeModeName": "货到付款",
    #         "settleMode": "LetterCredit",
    #         "settleModeName": "信用证",
    #         "braceletInstallNode": "BeforePayment",
    #         "braceletInstallNodeName": "付款前安装",
    #         "productNodeType": "LS-DFL-I",
    #         "productNodeTypeName": "直接租赁",
    #         "isInstallBracelet": 1,
    #         "isInstallBraceletName": "是",
    #         "notePeriod": "01",
    #         "notePeriodName": "60天",
    #     }
    #     data_5 = {
    #         "id": None,
    #         "projectNo": projectNo,
    #         "projTradesId": id_5,
    #         "supplierId": data_before[custName]["supplierId"],
    #         "supplierName": data_before[custName]["supplierName"],
    #         "certType": "200",
    #         "certId": data_before[custName]["certId"],
    #         "artificialPerson": data_before[custName]["artificialPerson"],
    #         "registerFullAddress": data_before[custName]["registerFullAddress"],
	#         "businessAddress": data_before[custName]["businessAddress"],
    #         "contacts": None,
    #         "phone": None,
    #         "openingBank": None,
    #         "openingBankNum": None,
    #         "account": None,
    #         "accountNo": None,
    #         "invoiceTitle": None,
    #         "taxQualification": None,
    #         "taxId": None,
    #         "taxTel": None,
    #         "taxAddress": None,
    #         "contractType": None,
    #         "tradeMode": "02",
    #         "tradeModeName": "货到付款",
    #         "settleMode": "LetterCredit",
    #         "settleModeName": "信用证",
    #         "braceletInstallNode": "BeforePayment",
    #         "braceletInstallNodeName": "付款前安装",
    #         "productNodeType": "LS-DFL-I",
    #         "productNodeTypeName": "直接租赁",
    #         "isInstallBracelet": 1,
    #         "isInstallBraceletName": "是",
    #         "notePeriod": "01",
    #         "notePeriodName": "60天",
    #     }
    #     data_6 = {
    #         "id": None,
    #         "projectNo": projectNo,
    #         "projTradesId": id_6,
    #         "supplierId": data_after[custName]["supplierId"],
    #         "supplierName": data_after[custName]["supplierName"],
    #         "certType": "200",
    #         "certId": data_after[custName]["certId"],
    #         "artificialPerson": data_after[custName]["artificialPerson"],
    #         "registerFullAddress": data_after[custName]["registerFullAddress"],
	#         "businessAddress": data_after[custName]["businessAddress"],
    #         "contacts": None,
    #         "phone": None,
    #         "openingBank": None,
    #         "openingBankNum": None,
    #         "account": None,
    #         "accountNo": None,
    #         "invoiceTitle": None,
    #         "taxQualification": None,
    #         "taxId": None,
    #         "taxTel": None,
    #         "taxAddress": None,
    #         "contractType": None,
    #         "tradeMode": "02",
    #         "tradeModeName": "货到付款",
    #         "settleMode": "LetterCredit",
    #         "settleModeName": "信用证",
    #         "braceletInstallNode": "BeforePayment",
    #         "braceletInstallNodeName": "付款前安装",
    #         "productNodeType": "LS-DFL-I",
    #         "productNodeTypeName": "直接租赁",
    #         "isInstallBracelet": 1,
    #         "isInstallBraceletName": "是",
    #         "notePeriod": "01",
    #         "notePeriodName": "60天",
    #     }
    #
    #
    #
    #     data_7 = {
    #         "id": None,
    #         "projectNo": projectNo,
    #         "projTradesId": id_7,
    #         "supplierId": data_after[custName]["supplierId"],
    #         "supplierName": data_after[custName]["supplierName"],
    #         "certType": "200",
    #         "certId": data_after[custName]["certId"],
    #         "artificialPerson": data_after[custName]["artificialPerson"],
    #         "registerFullAddress": data_after[custName]["registerFullAddress"],
	#         "businessAddress": data_after[custName]["businessAddress"],
    #         "contacts": None,
    #         "phone": None,
    #         "openingBank": None,
    #         "openingBankNum": None,
    #         "account": None,
    #         "accountNo": None,
    #         "invoiceTitle": None,
    #         "taxQualification": None,
    #         "taxId": None,
    #         "taxTel": None,
    #         "taxAddress": None,
    #         "contractType": None,
    #         "tradeMode": "01",
    #         "tradeModeName": "预付货款",
    #         "settleMode": "TelegraphicTransfer",
    #         "settleModeName": "转账",
    #         "braceletInstallNode": "AfterPayment",
    #         "braceletInstallNodeName": "付款后安装",
    #         "productNodeType": "LS-DFL-I",
    #         "productNodeTypeName": "直接租赁",
    #         "isInstallBracelet": 1,
    #         "isInstallBraceletName": "是",
    #         "notePeriod": "01",
    #         "notePeriodName": None,
    #     }
    #     data_8 = {
    #         "id": None,
    #         "projectNo": projectNo,
    #         "projTradesId": id_8,
    #         "supplierId": data_after[custName]["supplierId"],
    #         "supplierName": data_after[custName]["supplierName"],
    #         "certType": "200",
    #         "certId": data_after[custName]["certId"],
    #         "artificialPerson": data_after[custName]["artificialPerson"],
    #         "registerFullAddress": data_after[custName]["registerFullAddress"],
	#         "businessAddress": data_after[custName]["businessAddress"],
    #         "contacts": None,
    #         "phone": None,
    #         "openingBank": None,
    #         "openingBankNum": None,
    #         "account": None,
    #         "accountNo": None,
    #         "invoiceTitle": None,
    #         "taxQualification": None,
    #         "taxId": None,
    #         "taxTel": None,
    #         "taxAddress": None,
    #         "contractType": None,
    #         "tradeMode": "01",
    #         "tradeModeName": "预付货款",
    #         "settleMode": "TelegraphicTransfer",
    #         "settleModeName": "转账",
    #         "braceletInstallNode": "AfterPayment",
    #         "braceletInstallNodeName": "付款后安装",
    #         "productNodeType": "LS-DFL-I",
    #         "productNodeTypeName": "直接租赁",
    #         "isInstallBracelet": 1,
    #         "isInstallBraceletName": "是",
    #         "notePeriod": "01",
    #         "notePeriodName": None,
    #     }
    #     data_9 = {
    #         "id": None,
    #         "projectNo": projectNo,
    #         "projTradesId": id_9,
    #         "supplierId": data_after[custName]["supplierId"],
    #         "supplierName": data_after[custName]["supplierName"],
    #         "certType": "200",
    #         "certId": data_after[custName]["certId"],
    #         "artificialPerson": data_after[custName]["artificialPerson"],
    #         "registerFullAddress": data_after[custName]["registerFullAddress"],
	#         "businessAddress": data_after[custName]["businessAddress"],
    #         "contacts": None,
    #         "phone": None,
    #         "openingBank": None,
    #         "openingBankNum": None,
    #         "account": None,
    #         "accountNo": None,
    #         "invoiceTitle": None,
    #         "taxQualification": None,
    #         "taxId": None,
    #         "taxTel": None,
    #         "taxAddress": None,
    #         "contractType": None,
    #         "tradeMode": "01",
    #         "tradeModeName": "预付货款",
    #         "settleMode": "TelegraphicTransfer",
    #         "settleModeName": "转账",
    #         "braceletInstallNode": "AfterPayment",
    #         "braceletInstallNodeName": "付款后安装",
    #         "productNodeType": "LS-DFL-I",
    #         "productNodeTypeName": "直接租赁",
    #         "isInstallBracelet": 1,
    #         "isInstallBraceletName": "是",
    #         "notePeriod": "01",
    #         "notePeriodName": None,
    #     }
    #
    #     list.append(data_1)
    #     list.append(data_2)
    #     list.append(data_3)
    #     list.append(data_4)
    #     list.append(data_5)
    #     list.append(data_6)
    #     list.append(data_7)
    #     list.append(data_8)
    #     list.append(data_9)
    #     for i in list:
    #         res = self.api(method='POST', url=url, json=i)

    '''供应商保存'''

    def supplierSave(self, projectNo, custName, env, projTradesId, count):
        if custName == 'ph_sd':
            custName = 'jxw'
        url = 'ifc/api/credit-apply/trades/saveSupplier'

        data = test_data.getSupplier(projectNo, custName, env, projTradesId)


        res = self.api(method='POST', url=url, json=data[count])


    '''查询品牌'''
    def pageSerach(self):
        url = 'ifc/api/proj/pageSearchBrands'
        data = {
            "searchParam": "测试Z500品牌三级",
            "current": 1,
            "size": 10
        }
        res = self.api(method='POST', url=url, json=data)
        return res

    '''添加租赁物'''
    def leaseSave(self,projectNo,id):
        res_search = self.pageSerach()
        url = 'ifc/api/credit-apply/trades/saveLeasehold'
        data = {
            "projectNo": projectNo,
            "projTradesId": id,
            "tradesLeaseholdList": [{
                "showMore": True,
                "projectNo": "",
                "projTradesId": None,
                "leaseholdName": "第一个租赁物",
                "brandId": jsonpath.jsonpath(res_search, "$..idArtlBrand")[0],
                "brandFullName": jsonpath.jsonpath(res_search, "$..brandFullName")[0],
                "brandSplicingName": jsonpath.jsonpath(res_search, "$..brandSplicingName")[0],
                "spec": "123",
                "leaseholdType": "625304010101",
                "industryClassify": ["A", "A01", "A011"],
                "industryClassifyName": "",
                "industryClassifyOne": "A",
                "industryClassifyOneName": "",
                "industryClassifyTwo": "A01",
                "industryClassifyTwoName": "",
                "price": "11000.00",
                "amount": "1",
                "financeAmt": 1100,
                "financeScale": "10.00",
                "bookAmt": "11000.00",
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
                "placeDetailAddress": "上海详细地址",
                "directReversalUniqueIdentifier": "",
                "isShowGreaterThanMsg": False,
                "leaseholdTypeList": ["625001000000", "625101010000", "625201010100", "625304010101"],
                "leaseholdTypeOne": "625001000000",
                "leaseholdTypeTwo": "625101010000",
                "leaseholdTypeThree": "625201010100",
                "industryClassifyThree": "A011",
                "equipmentCategoryTypeOne": jsonpath.jsonpath(res_search, "$..equipmentCategoryTypeOne")[0],
                "equipmentCategoryTypeTwo": jsonpath.jsonpath(res_search, "$..equipmentCategoryTypeTwo")[0],
                "equipmentCategoryTypeThree": jsonpath.jsonpath(res_search, "$..equipmentCategoryTypeThree")[0],
                "brandLevel": jsonpath.jsonpath(res_search, "$..brandLevel")[0],
                "facilityName": jsonpath.jsonpath(res_search, "$..facilityName")[0]
            },{
                "showMore": True,
                "projectNo": "",
                "projTradesId": None,
                "leaseholdName": "第二个租赁物",
                "brandId": jsonpath.jsonpath(res_search, "$..idArtlBrand")[0],
                "brandFullName": jsonpath.jsonpath(res_search, "$..brandFullName")[0],
                "brandSplicingName": jsonpath.jsonpath(res_search, "$..brandSplicingName")[0],
                "spec": "456",
                "leaseholdType": "625304010101",
                "industryClassify": ["A", "A01", "A011"],
                "industryClassifyName": "",
                "industryClassifyOne": "A",
                "industryClassifyOneName": "",
                "industryClassifyTwo": "A01",
                "industryClassifyTwoName": "",
                "price": "22000.00",
                "amount": "2",
                "financeAmt": "4400.00",
                "financeScale": "10.00",
                "bookAmt": "44000.00",
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
                "placeDetailAddress": "上海详细地址",
                "directReversalUniqueIdentifier": "",
                "leaseholdTypeList": ["625001000000", "625101010000", "625201010100", "625304010101"],
                "leaseholdTypeOne": "625001000000",
                "leaseholdTypeTwo": "625101010000",
                "leaseholdTypeThree": "625201010100",
                "industryClassifyThree": "A011",
                "equipmentCategoryTypeOne": jsonpath.jsonpath(res_search, "$..equipmentCategoryTypeOne")[0],
                "equipmentCategoryTypeTwo": jsonpath.jsonpath(res_search, "$..equipmentCategoryTypeTwo")[0],
                "equipmentCategoryTypeThree": jsonpath.jsonpath(res_search, "$..equipmentCategoryTypeThree")[0],
                "brandLevel": jsonpath.jsonpath(res_search, "$..brandLevel")[0],
                "facilityName": jsonpath.jsonpath(res_search, "$..facilityName")[0],
                "isShowGreaterThanMsg": False
            },{
                "showMore": True,
                "projectNo": "",
                "projTradesId": None,
                "leaseholdName": "第三个租赁物",
                "brandId": jsonpath.jsonpath(res_search, "$..idArtlBrand")[0],
                "brandFullName": jsonpath.jsonpath(res_search, "$..brandFullName")[0],
                "brandSplicingName": jsonpath.jsonpath(res_search, "$..brandSplicingName")[0],
                "spec": "789",
                "leaseholdType": "625304010101",
                "industryClassify": ["A", "A01", "A011"],
                "industryClassifyName": "",
                "industryClassifyOne": "A",
                "industryClassifyOneName": "",
                "industryClassifyTwo": "A01",
                "industryClassifyTwoName": "",
                "price": "33000.00",
                "amount": "3",
                "financeAmt": 9900,
                "financeScale": "10.00",
                "bookAmt": "99000.00",
                "isInstallBracelet": 0,
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
                "placeDetailAddress": "上海详细地址",
                "directReversalUniqueIdentifier": "",
                "leaseholdTypeList": ["625001000000", "625101010000", "625201010100", "625304010101"],
                "leaseholdTypeOne": "625001000000",
                "leaseholdTypeTwo": "625101010000",
                "leaseholdTypeThree": "625201010100",
                "industryClassifyThree": "A011",
                "equipmentCategoryTypeOne": jsonpath.jsonpath(res_search, "$..equipmentCategoryTypeOne")[0],
                "equipmentCategoryTypeTwo": jsonpath.jsonpath(res_search, "$..equipmentCategoryTypeTwo")[0],
                "equipmentCategoryTypeThree": jsonpath.jsonpath(res_search, "$..equipmentCategoryTypeThree")[0],
                "brandLevel": jsonpath.jsonpath(res_search, "$..brandLevel")[0],
                "facilityName": jsonpath.jsonpath(res_search, "$..facilityName")[0],
                "isShowGreaterThanMsg": False
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
            "lprBaseRate": None,
            "rentRate": None,
            "bpFloatValue": None,
            "preditRentDate": str(datetime.datetime.now().date()+datetime.timedelta(days=5)),
            "financeTerm": 12,
            "yearPaymentTimes": "12",
            "totalPaymentTimes": "12",
            "financeTotalAmt": "15400.00",
            "totalBookAmt": 154000,
            "financingPaymentDirection": "Supplier",
            "financingPaymentDirectionName": "供应商",
            "isExistDownPayment": 1,
            "downPaymentCalcMode": "FIX_AMOUNT",
            "downPaymentRatio": 0.9,
            "downPaymentAmt": 138600,
            "downPaymentPayDirection": "Supplier",
            "isExistMargin": 0,
            "isExistMarginName": None,
            "marginCalcMode": None,
            "marginRatio": 0,
            "marginAmt": 0,
            "marginDeductMode": None,
            "retentionPriceAmt": "100.00",
            "discountAmt": "200.00",
            "firstTermAmt": "300.00",
            "rentalMode": "Prepay",
            "rentalModeName": None,
            "rentCalcMode": "EquivalentRent",
            "rentAmt": "1386",
            "quickPaymentAmt": None,
            "rentTotalAmt": 0,
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
            "rentRate": 0.1718,
            "bpFloatValue": "1,352.57",
            "preditRentDate": str(datetime.datetime.now().date()+datetime.timedelta(days=5)),
            "financeTerm": 12,
            "yearPaymentTimes": "12",
            "totalPaymentTimes": "12",
            "financeTotalAmt": "15400.00",
            "totalBookAmt": 154000,
            "financingPaymentDirection": "Supplier",
            "financingPaymentDirectionName": "供应商",
            "isExistDownPayment": 1,
            "downPaymentCalcMode": "FIX_AMOUNT",
            "downPaymentRatio": 0.9,
            "downPaymentAmt": 138600,
            "downPaymentPayDirection": "Supplier",
            "isExistMargin": 0,
            "isExistMarginName": None,
            "marginCalcMode": None,
            "marginRatio": 0,
            "marginAmt": 0,
            "marginDeductMode": None,
            "retentionPriceAmt": "100.00",
            "discountAmt": "200.00",
            "firstTermAmt": "300.00",
            "rentalMode": "Prepay",
            "rentalModeName": None,
            "rentCalcMode": "EquivalentRent",
            "rentAmt": "1386.00",
            "quickPaymentAmt": None,
            "rentTotalAmt": 0,
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

    def evaluationSubjectQuery(self,projectNo):
        url = 'ifc/api/risk-info/queryEvaluationSubject'
        data = {
            "projectNo": projectNo
        }
        res = self.api(method='POST', url=url, json=data)
        return res

    '''评估主体类型'''
    def evaluationSubjectBaseQuery(self,projectNo):
        url = 'ifc/api/risk-info/queryEvaluationSubjectBase'
        data = {
            "projectNo": projectNo,
            "roleType": "1"
        }
        res = self.api(method='POST', url=url, json=data)
        return res

    def evaluationSubjectScoreQuery(self,projectNo):
        '''评估主体得分'''
        res_subject = self.evaluationSubjectBaseQuery(projectNo)
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
        res_subject = self.evaluationSubjectQuery(projectNo)
        url = 'ifc/api/risk-info/saveEvaluationSubject'
        data = {
            "id": jsonpath.jsonpath(res_subject,'$..id')[0],
            "projectNo": projectNo,
            "evaluationSubjectId": jsonpath.jsonpath(res[0],'$..evaluationSubjectId')[0],
            "evaluationSubjectType": jsonpath.jsonpath(res[0],'$..evaluationSubjectType')[0],
            "evaluationSubjectTypeName": jsonpath.jsonpath(res_subject,'$..evaluationSubjectTypeName')[0],
            "evaluationSubjectName": jsonpath.jsonpath(res_subject,'$..evaluationSubjectName')[0],
            "generalScore": jsonpath.jsonpath(res_subject,'$..generalScore')[0],
            "scheme": jsonpath.jsonpath(res_subject,'$..scheme')[0],
            "riskScoreItemMap": {
                "depositGt5timesRent6Mon": 1,
                "houseProperty": 1,
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
            "projCustEnterpriseIncomeVerification" : None,
            # "projCustEnterpriseIncomeVerification": {
                # "id": None,
                # "confirmableIncome": "10",
                # "currentYearIncome": "10.00",
                # "previousYearIncome": "10.00",
                # "projectNo": None
            # },
            "bankStatementList": [],
            "electricChargeList": [{
                "billDate": "2023-11",
                "billAmount": "10.00"
            },{
                "billDate": "2023-10",
                "billAmount": "10.00"
            }, {
                "billDate": "2023-09",
                "billAmount": "10.00"
            }, {
                "billDate": "2023-08",
                "billAmount": "10.00"
            }, {
                "billDate": "2023-07",
                "billAmount": "10.00"
            }, {
                "billDate": "2023-06",
                "billAmount": "10.00"
            }],
            "rigidLiabilityList" : None,
            # "rigidLiabilityList": [
            #     {
            #     "customerType": "1",
            #     "liabilityType": "BankLoan",
            #     "belongingCompanyId": jsonpath.jsonpath(res,'$..id')[0],
            #     "rigidLiabilityAmount": "100.00",
            #     "mortgageLiabilityAmount": "100.00"
            # }
            # ],
            "totalAmount": 12474,
            "recentElecDate": "2023-11"
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
    def attachmentNextStep(self,projectNo, templateCode):
        url = 'ifc/api/attachment/nextStep'
        data = {
            "businessKey": projectNo,
            "templateCode": templateCode
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

    def getAppTask(self,projectNo):
        res = self.todoListApp()
        for i in res["content"] :
            if i["businessKey"] == projectNo:
                taskid = i["id"]
                break;
        return taskid

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
            "code": 0,
            # "status": True,
            "message": 'success,耗时%ss,打开app项目列表查看新建项目！！！' % run_time,
            "data": "项目编号：%s" % projectNo
        }
        # result = '耗时%ss, 打开app项目列表查看新建项目！！！项目编号: %s' % (run_time,projectNo)

        return result

    def result_approve(self,start_time,projectNo):
        end_time = time.time()
        run_time = round(end_time - start_time, 2)
        result = {
            "code": 0,
            # "status": True,
            "message": 'success,耗时%ss,打开app项目列表查看已审批的项目！！！' % run_time,
            "data": "项目编号：%s" % projectNo
        }
        # result = '耗时%ss, 打开app项目列表查看新建项目！！！项目编号: %s' % (run_time,projectNo)

        return result

    def result_contract(self,start_time,payMainNo):
        end_time = time.time()
        run_time = round(end_time - start_time, 2)
        result = {
            "code": 0,
            # "status": True,
            "message": 'success,耗时%ss,请去小程序签署合同！！！' % run_time,
            "data": "合同编号：%s" % payMainNo
        }
        # result = '耗时%ss, 打开app项目列表查看新建项目！！！项目编号: %s' % (run_time,projectNo)

        return result

    def result_payment(self,start_time,payMainNo):
        end_time = time.time()
        run_time = round(end_time - start_time, 2)
        result = {
            "code": 0,
            # "status": True,
            "message": 'success,耗时%ss,打开app合同付款列表查看已提交审批的项目！！！' % run_time,
            "data": "合同编号：%s" % payMainNo
        }
        # result = '耗时%ss, 打开app项目列表查看新建项目！！！项目编号: %s' % (run_time,projectNo)

        return result

    def resultPaymentApprove(self,start_time,payMainNo):
        end_time = time.time()
        run_time = round(end_time - start_time, 2)
        result = {
            "code": 0,
            # "status": True,
            "message": 'success,耗时%ss,打开app合同付款列表查看已审批的项目！！！' % run_time,
            "data": "合同编号：%s" % payMainNo
        }
        # result = '耗时%ss, 打开app项目列表查看新建项目！！！项目编号: %s' % (run_time,projectNo)

        return result



    def payApplyList(self,projectNo):
        url = 'ifc/api/pay-apply/list'
        data = {
            "current": 1,
            "size": 1000,
            "projectNo": projectNo
        }
        res = self.api(method='POST', url=url, json=data)
        return res




    def payApplyListNo(self,payInfoNo):

        url = 'ifc/api/pay-apply/list/%s'%payInfoNo
        res = self.api(method='POST', url=url)
        return res


    def payCustEnterpriseQuery(self,payInfoNo):
        '''合同付款-客户信息-承租人-查询'''
        url = 'ifc/api/pay_cust_enterprise_info/initLessee'
        data = {
            "payInfoNo": payInfoNo
        }
        res = self.api(method='POST', url=url, json=data)
        return res

    def payCustEnterpriseSave(self,payInfoNo,projectNo):
        '''合同付款-客户信息-承租人-保存'''
        url = 'ifc/api/pay_cust_enterprise_info/saveLessee'
        res_query = self.payCustEnterpriseQuery(payInfoNo)
        data = {
                "id": jsonpath.jsonpath(res_query,'$..id')[0],
                "projCustId": jsonpath.jsonpath(res_query,'$..projCustId')[0],
                "payInfoNo": payInfoNo,
                "enterpriseName": jsonpath.jsonpath(res_query,'$..enterpriseName')[0],
                "resolutionType": jsonpath.jsonpath(res_query,'$..resolutionType')[0],
                "resolutionTypeName": jsonpath.jsonpath(res_query,'$..resolutionTypeName')[0],
                "contacts": jsonpath.jsonpath(res_query,'$..contacts')[0],
                "contactsType": jsonpath.jsonpath(res_query,'$..contactsType')[0],
                "contactsTypeName": jsonpath.jsonpath(res_query,'$..contactsTypeName')[0],
                "resolutionsList": [{
                    "signingName": jsonpath.jsonpath(res_query,'$..signingName')[0],
                    "signingType": jsonpath.jsonpath(res_query,'$..signingType')[0],
                    "signingTypeName": jsonpath.jsonpath(res_query,'$..signingTypeName')[0],
                    "signingMobile": jsonpath.jsonpath(res_query,'$..signingMobile')[0]
                }],
                "invoicingInfo": {
                    "payInfoNo": None,
                    "invoicingMethod": "mergeInvoice",
                    "invoicingMethodName": None,
                    "invoiceHeader": jsonpath.jsonpath(res_query,'$..invoiceHeader')[0],
                    "taxQualification": "10",
                    "taxQualificationName": None,
                    "dutyParagraph": "123456789123456",
                    "invoicingPhone": "15712345678",
                    "bank": "上海开户银行",
                    "bankAccount": "622212345678123",
                    "invoicingAddress": "开票地址"
                },
                "projectNo": projectNo
            }
        res = self.api(method='POST', url=url, json=data)

    def payCustGuarantorSave(self,payInfoNo,projectNo):
        '''合同付款-客户信息-担保方-保存'''
        url = 'ifc/api/pay_cust_enterprise_info/saveGuarantor'
        data ={
            "guarantorList": [],
            "payInfoNo": payInfoNo,
            "projectNo": projectNo
        }
        res = self.api(method='POST', url=url, json=data)

    def payTradesSupplierInit(self,payInfoNo,projectNo):
        '''合同付款-交易结构-供应商-查询'''
        url = 'ifc/api/pay-trades-supplier/initPram?projectNo=%s&payInfoNo=%s'%(projectNo,payInfoNo)
        res = self.api(method="GET", url=url)
        return res

    def payContractListQuery(self,supplierId):
        '''合同付款-交易结构-供应商-联系人-查询'''
        url = 'ifc/api/pay-trades-supplier/getSupplierContactsList?supplierId=%s&contactsType=0'%supplierId
        res = self.api(method="GET", url=url)
        return res

    def payOpenBankListQuery(self,supplierId):
        '''合同付款-交易结构-供应商-开户行-查询'''
        url = 'ifc/api/pay-trades-supplier/getSupplierOpenBankList?customerName=&current=1&size=20&supplierId=%s'%supplierId
        res = self.api(method="GET", url=url)
        return res

    def payTradesSupplierSave(self,payInfoNo,projectNo):
        '''合同付款-交易结构-供应商-保存'''
        url = 'ifc/api/pay-trades-supplier/save'
        res_init = self.payTradesSupplierInit(payInfoNo,projectNo)
        print(jsonpath.jsonpath(res_init,'$..supplierId')[0])
        res_contact_list = self.payContractListQuery(jsonpath.jsonpath(res_init,'$..supplierId')[0])
        res_bank_list = self.payOpenBankListQuery(jsonpath.jsonpath(res_init,'$..supplierId')[0])
        data = {
            "id": jsonpath.jsonpath(res_init,'$..id')[0],
            "payInfoNo": payInfoNo,
            "projectNo": projectNo,
            "supplierId":jsonpath.jsonpath(res_init,'$..supplierId')[0],
            "supplierCertId": jsonpath.jsonpath(res_init,'$..supplierCertId')[0],
            "supplierName": jsonpath.jsonpath(res_init,'$..supplierName')[0],
            "supplierLegalRepresentative": jsonpath.jsonpath(res_init,'$..supplierLegalRepresentative')[0],
            "supplierContactId": jsonpath.jsonpath(res_contact_list,'$..custId')[0],
            "supplierContactType": "0",
            "supplierContactTypeName": "联系人",
            "supplierContacts": jsonpath.jsonpath(res_contact_list,'$..supplierContacts')[0],
            "supplierTel": jsonpath.jsonpath(res_contact_list,'$..supplierTel')[0],
            "openingBank": jsonpath.jsonpath(res_bank_list,'$..openingBank')[0],
            "openingBankNum": jsonpath.jsonpath(res_bank_list,'$..openingBankNum')[0],
            "accountId": jsonpath.jsonpath(res_bank_list,'$..accountId')[0],
            "accountName": jsonpath.jsonpath(res_bank_list,'$..accountName')[0],
            "accountNo": jsonpath.jsonpath(res_bank_list,'$..accountNo')[0],
            "isUpdateContractType": 1,
            "contractType": "SALE_CONTRACT",
            "contractTypeName": "",
            "paidNonFinancingFunds": "",
            "unpaidNonFinancingFunds": "",
            "contractDataList": [],
            "email": jsonpath.jsonpath(res_contact_list,'$..email')[0],
            "faxNo": None
        }
        res = self.api(method='POST', url=url, json=data)

    def payTradesLeaseholdInit(self,payInfoNo,projectNo):
        '''合同付款-交易结构-租赁物-查询'''
        url = 'ifc/api/pay-trades-leasehold/initPram?payInfoNo=%s&projectNo=%s'%(payInfoNo,projectNo)
        res = self.api(method="GET", url=url)
        return res

    def payTradesLeaseholdSave(self,payInfoNo,projectNo):
        '''合同付款-交易结构-租赁物-保存'''
        url = 'ifc/api/pay-trades-leasehold/save'
        res_query = self.payTradesLeaseholdInit(payInfoNo,projectNo)
        data = {
            "id": None,
            "projectNo": projectNo,
            "payInfoNo": payInfoNo,
            "tradeMode": jsonpath.jsonpath(res_query,'$..tradeMode')[0],
            "deliveryDateType": "1",
            "deliveryDateTypeName": None,
            "deliveryDateTypeReadOnly": False,
            "leaseholdDeliveryDate": str(datetime.datetime.now().date()+datetime.timedelta(days=5)),
            "leaseholdInspectionDate": str(datetime.datetime.now().date()+datetime.timedelta(days=5)),
            "equipmentQualityGuaranteePeriod": "12",
            "infos": []
        }
        res = self.api(method='POST', url=url, json=data)

    def paySupplementQuery(self,payInfoNo):
        url = 'ifc/api/pay-apply/contract-supplement/contact/%s'%payInfoNo
        res = self.api(method="GET", url=url)
        return res

    def paySupplementSave(self,payInfoNo,projectNo):
        url = 'ifc/api/pay-apply/contract-supplement/save'
        res_query = self.paySupplementQuery(payInfoNo)
        data = {
            "payInfoNo": payInfoNo,
            "paySignContactList": [{
                "paySignContactNo": jsonpath.jsonpath(res_query,'$..paySignContactNo')[0],
                "projectNo": projectNo,
                "payInfoNo": payInfoNo,
                "customerNo": jsonpath.jsonpath(res_query,'$..customerNo')[0],
                "customerName": jsonpath.jsonpath(res_query,'$..customerName')[0],
                "customerType":jsonpath.jsonpath(res_query,'$..customerType')[0],
                "customerTypeName": jsonpath.jsonpath(res_query,'$..customerTypeName')[0],
                "signContactType": jsonpath.jsonpath(res_query,'$..signContactType')[0],
                "signContactTypeName":jsonpath.jsonpath(res_query,'$..signContactTypeName')[0],
                "customerSignType": jsonpath.jsonpath(res_query,'$..customerSignType')[0],
                "customerSignTypeName": jsonpath.jsonpath(res_query,'$..customerSignTypeName')[0],
                "signatoryName": jsonpath.jsonpath(res_query,'$..signatoryName')[0],
                "phone": jsonpath.jsonpath(res_query,'$..phone')[0],
                "signatoryType": jsonpath.jsonpath(res_query,'$..signatoryType')[0],
                "signatoryTypeName": jsonpath.jsonpath(res_query,'$..signatoryTypeName')[0],
                "certNo": jsonpath.jsonpath(res_query,'$..certNo')[0],
                "expire": None,
                "resolutions": [{
                    "paySignContactNo": jsonpath.jsonpath(res_query,'$..paySignContactNo')[0],
                    "projectNo": projectNo,
                    "payInfoNo": payInfoNo,
                    "customerNo": jsonpath.jsonpath(res_query,'$..customerNo')[0],
                    "customerName": jsonpath.jsonpath(res_query,'$..customerName')[0],
                    "customerType": jsonpath.jsonpath(res_query,'$..customerType')[0],
                    "customerTypeName": jsonpath.jsonpath(res_query,'$..customerTypeName')[0],
                    "signContactType": jsonpath.jsonpath(res_query,'$..signContactType')[0],
                    "signContactTypeName": jsonpath.jsonpath(res_query,'$..signContactTypeName')[0],
                    "customerSignType": jsonpath.jsonpath(res_query,'$..customerSignType')[0],
                    "customerSignTypeName": jsonpath.jsonpath(res_query,'$..customerSignTypeName')[0],
                    "signatoryName": jsonpath.jsonpath(res_query,'$..signatoryName')[0],
                    "phone": jsonpath.jsonpath(res_query,'$..phone')[0],
                    "signatoryType": jsonpath.jsonpath(res_query,'$..signatoryType')[0],
                    "signatoryTypeName": jsonpath.jsonpath(res_query,'$..signatoryTypeName')[0],
                    "certNo": None
                }],
                "id": 0
            }, {
                "paySignContactNo": jsonpath.jsonpath(res_query,'$..paySignContactNo')[0],
                "projectNo": projectNo,
                "payInfoNo": payInfoNo,
                "customerNo": jsonpath.jsonpath(res_query,'$..customerNo')[0],
                "customerName": jsonpath.jsonpath(res_query,'$..customerName')[0],
                "customerType":jsonpath.jsonpath(res_query,'$..customerType')[0],
                "customerTypeName": jsonpath.jsonpath(res_query,'$..customerTypeName')[0],
                "signContactType": jsonpath.jsonpath(res_query,'$..signContactType')[0],
                "signContactTypeName": jsonpath.jsonpath(res_query,'$..signContactTypeName')[0],
                "customerSignType": jsonpath.jsonpath(res_query,'$..customerSignType')[0],
                "customerSignTypeName": jsonpath.jsonpath(res_query,'$..customerSignTypeName')[0],
                "signatoryName": jsonpath.jsonpath(res_query,'$..signatoryName')[0],
                "phone": jsonpath.jsonpath(res_query,'$..phone')[0],
                "signatoryType": jsonpath.jsonpath(res_query,'$..signatoryType')[0],
                "signatoryTypeName": jsonpath.jsonpath(res_query,'$..signatoryTypeName')[0],
                "certNo": None,
                "expire": None,
                "resolutions": [],
                "id": 1
            }]
        }
        res = self.api(method='POST', url=url, json=data)

    def signatoryQuery(self,payInfoNo):
        url = 'ifc/api/pay-apply/contract/signatory/%s'%payInfoNo
        res = self.api(method="POST", url=url)
        return res

    def riskInformationQuery(self,payInfoNo,projectNo):
        '''付款申请-风险信息-查询'''
        url = 'ifc/api/request-funds/risk/init'
        data = {
                "projectNo": projectNo,
                "payInfoNo": payInfoNo
            }
        res = self.api(method='POST', url=url, json=data)
        return res

    def riskInformationSave(self,payInfoNo,projectNo):
        '''付款申请-风险信息-保存'''
        url = 'ifc/api/request-funds/risk/save'
        res_query = self.riskInformationQuery(payInfoNo,projectNo)
        data = {
            "riskInfoVMS": jsonpath.jsonpath(res_query,'$..riskInfoVMList')[0]
        }
        res = self.api(method='POST', url=url, json=data)
        return res

    def requestFundsQuery(self,payInfoNo,projectNo):
        '''付款申请-付款信息-查询'''
        url = 'ifc/api/request-funds/pay/init'
        data = {
            "projectNo": projectNo,
            "payInfoNo": payInfoNo
        }
        res = self.api(method='POST', url=url, json=data)
        return res

    def requestFundsSave(self,payInfoNo,projectNo):
        '''付款申请-付款信息-保存'''
        url = 'ifc/api/request-funds/pay/invoice/save'
        res_query = self.requestFundsQuery(payInfoNo,projectNo)
        data = {
            "settlementMethod": "BankAcceptanceBill",
            "projectNo": projectNo,
            "payInfoNo": payInfoNo,
            "invoiceList": [{
                "num": "1",
                "singleAmount": jsonpath.jsonpath(res_query,'$..actualPaymentAmount')[0],
                "totalAmount": int(jsonpath.jsonpath(res_query,'$..actualPaymentAmount')[0])
            }]
        }
        res = self.api(method='POST', url=url, json=data)
        return res

    def requestFundsSendQuery(self,payInfoNo,projectNo):
        '''付款申请-寄送信息-查询'''
        url = 'ifc/api/request-funds/send/init'
        data = {
            "projectNo": projectNo,
            "payInfoNo": payInfoNo
        }
        res = self.api(method='POST', url=url, json=data)
        return res

    def payTradesSupplierQuery(self,supplierId):
        url = 'ifc/api/pay-trades-supplier/getSupplierContactsList?supplierId=%s&contactsType=0' %supplierId
        res = self.api(method='GET', url=url)
        return res


    def requestFundsSendSave(self,payInfoNo,projectNo):
        '''付款申请-寄送信息-查询'''
        url = 'ifc/api/request-funds/send/save'
        res_query = self.requestFundsSendQuery(payInfoNo,projectNo)
        res_supplier = self.payTradesSupplierQuery(jsonpath.jsonpath(res_query,'$..supplierId')[0])
        data = {
            "projectNo": projectNo,
            "payInfoNo": payInfoNo,
            "renter": {
                "contactName": jsonpath.jsonpath(res_query,'$..contactName')[0],
                "contactMobile": jsonpath.jsonpath(res_query,'$..contactMobile')[0],
                "email": "123@163.con",
                "postalCode": "222000",
                "sendAddress": jsonpath.jsonpath(res_query,'$..sendAddress')[0],
                "province": jsonpath.jsonpath(res_query,'$..province')[0],
                "city": jsonpath.jsonpath(res_query,'$..city')[0],
                "region": jsonpath.jsonpath(res_query,'$..region')[0],
                "provinceName": jsonpath.jsonpath(res_query,'$..provinceName')[0],
                "cityName": jsonpath.jsonpath(res_query,'$..cityName')[0],
                "regionName": jsonpath.jsonpath(res_query,'$..regionName')[0],
                "sendMethod": jsonpath.jsonpath(res_query,'$..sendMethod')[0],
                "sendMethodName": jsonpath.jsonpath(res_query,'$..sendMethodName')[0],
                "receiveTickets": jsonpath.jsonpath(res_query,'$..receiveTickets')[0],
                "receiveTicketsName": jsonpath.jsonpath(res_query,'$..receiveTicketsName')[0],
                "userId": jsonpath.jsonpath(res_query,'$..userId')[0],
                "sendType":jsonpath.jsonpath(res_query,'$..sendType')[0],
                "address": [jsonpath.jsonpath(res_query,'$..province')[0], jsonpath.jsonpath(res_query,'$..city')[0], jsonpath.jsonpath(res_query,'$..region')[0]]
            },
            "supplier": {
                "supplierContacts": jsonpath.jsonpath(res_supplier,'$..supplierContacts')[0],
                "supplierTel": jsonpath.jsonpath(res_supplier,'$..supplierTel')[0],
                "faxNo": None,
                "email": jsonpath.jsonpath(res_supplier,'$..email')[0],
                "custId": jsonpath.jsonpath(res_supplier,'$..custId')[0],
                "contractAdress": jsonpath.jsonpath(res_supplier,'$..contractAdress')[0],
                "fullContractAdress": jsonpath.jsonpath(res_supplier,'$..fullContractAdress')[0],
                "postalCode": jsonpath.jsonpath(res_supplier,'$..postalCode')[0],
                "province":  jsonpath.jsonpath(res_supplier,'$..province')[0],
                "city": jsonpath.jsonpath(res_supplier,'$..city')[0],
                "region": jsonpath.jsonpath(res_supplier,'$..region')[0],
                "provinceName": jsonpath.jsonpath(res_supplier,'$..provinceName')[0],
                "cityName": jsonpath.jsonpath(res_supplier,'$..cityName')[0],
                "regionName": jsonpath.jsonpath(res_supplier,'$..regionName')[0],
                "userId": jsonpath.jsonpath(res_supplier,'$..custId')[0],
                "contactMobile": jsonpath.jsonpath(res_supplier,'$..supplierTel')[0],
                "sendAddress": jsonpath.jsonpath(res_supplier,'$..contractAdress')[0],
                "contactName": jsonpath.jsonpath(res_supplier,'$..supplierContacts')[0],
                "supplierId": jsonpath.jsonpath(res_query,'$..supplierId')[0],
                "sendMethod": jsonpath.jsonpath(res_query,'$..sendMethod')[1],
                "receiveTickets": jsonpath.jsonpath(res_query,'$..receiveTickets')[1],
                "sendMethodName": jsonpath.jsonpath(res_query,'$..sendMethodName')[1],
                "receiveTicketsName": jsonpath.jsonpath(res_query,'$..receiveTicketsName')[1],
                "address":  [jsonpath.jsonpath(res_supplier,'$..province')[0], jsonpath.jsonpath(res_supplier,'$..city')[0], jsonpath.jsonpath(res_supplier,'$..region')[0]]
            }
        }
        res = self.api(method='POST', url=url, json=data)
        return res



    def departmentInit(self,payInfoNo):
        '''金融市场部审批页面-初始化接口'''
        url = 'ifc/api/financial-markets-department/init?payInfoNo=%s'%payInfoNo
        res = self.api(method='GET', url=url)
        return res



    def departmentSave(self,payInfoNo):
        '''金融市场部审批页面-保存接口'''
        url = 'ifc/api/financial-markets-department/save'
        res = self.departmentInit(payInfoNo)
        data = {
            "id": None,
            "projectNo": jsonpath.jsonpath(res,"$..projectNo")[0],
            "payInfoNo": jsonpath.jsonpath(res,"$..payInfoNo")[0],
            "settlementMode": None,
            "payAccountName": jsonpath.jsonpath(res,"$..payAccountName")[0],
            "payAccountNumber": jsonpath.jsonpath(res,"$..payAccountNumber")[0],
            "payAccountBank": jsonpath.jsonpath(res,"$..payAccountBank")[0]
        }
        res = self.api(method='POST', url=url, json=data)
        return  res


    def check(self,payInfoNo):
        res = self.signatoryQuery(payInfoNo)
        print(len(jsonpath.jsonpath(res,'$..contracts')[0]))
        print(len(jsonpath.jsonpath(res,'$..contracts')[1]))
        print(len(jsonpath.jsonpath(res,'$..contracts')[2]))
        assert len(jsonpath.jsonpath(res,'$..contracts')[0]) == 11
        assert len(jsonpath.jsonpath(res,'$..contracts')[1]) == 1
        assert len(jsonpath.jsonpath(res,'$..contracts')[2]) == 5




if __name__ == "__main__":



    custName = "jxw"
    env = "uat"
    payInfoNo = "202310080001"
    res = login(custName, env)
    headers_cust = {"AccessToken": res["access_token"]}
    xiaoWei = xiaoWeiNew(headers_cust, env)
    xiaoWei.check(payInfoNo)





