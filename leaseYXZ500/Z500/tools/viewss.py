#encoding='utf-8'

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
from Z500.tools.xiaoWeiNew import xiaoWeiNew


import time
import requests
import jsonpath
import datetime


# Create your views here.





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
def test_add_pr(request):
    start_time = time.time()
    '''获取客户经理'''
    custName = request.GET["custName"]
    lesaseName = custName + "测试项目"
    node = int(request.GET["node"])
    guarantor = request.GET["guarantor"]
    if guarantor == '':
        guarantor = '2'
    '''登录'''
    res = login(custName)
    headers_cust = {"AccessToken": res["access_token"]}
    xiaoWei = xiaoWeiNew(headers_cust)

    # projectNo = 'PJ202308210055'
    res = xiaoWei.add_pro(lesaseName)
    projectNo = res["data"]["projectNo"]
    '''征信授权'''
    xiaoWei.creditAuthSave(projectNo,custName,guarantor)
    xiaoWei.creditAuthBack(projectNo,custName,guarantor)

    '''预审提交'''
    res = xiaoWei.proSubmit(projectNo,guarantor)
    taskId = jsonpath.jsonpath(res,'$..taskId')[0]
    xiaoWei.opinionSumit(taskId)

    # if node >= 0:
    #     result = xiaoWei.result(start_time,projectNo)
    #     # end_time = time.time()
    #     # run_time = round(end_time - start_time, 2)
    #     # result = {
    #     #     "code": 200,
    #     #     "status": True,
    #     #     "message": 'success,耗时%ss,打开app项目列表查看新建项目！！！' % run_time,
    #     #     "data": "项目编号：%s" % projectNo
    #     # }
    #     return JsonResponse(result, json_dumps_params={'ensure_ascii': False})

    if node >= 1:
        print("风控预审中")
        '''风控预审'''
        time.sleep(75)
        while True:
            time.sleep(1)
            count = 0
            res = xiaoWei.pro_page()
            for i in res["data"]["records"]:
                if i["projectNo"] == projectNo:
                    if i["statusName"] == "待授信申请":
                        count = 1
                        break;
            if count == 1:
                break;
        '''授信-客户信息'''
        xiaoWei.custEnterpriseSave(projectNo)
        xiaoWei.custEnterpriseRelateSave(projectNo,guarantor)


        '''交易结构'''
        projTrades = []
        for i in xiaoWei.projTradeAdd(projectNo):
            projTradesId = jsonpath.jsonpath(i, '$..id')[0]
            projTrades.append(projTradesId)
        '''供应商'''
        xiaoWei.supplierSave(projectNo, custName, projTrades[0],projTrades[1],projTrades[2],projTrades[3],projTrades[4],projTrades[5],projTrades[6],projTrades[7],projTrades[8])
        for i in projTrades:
            '''租赁物'''
            xiaoWei.leaseSave(projectNo, i)
            '''融资信息'''
            xiaoWei.rentSave(projectNo, i)
        '''风险信息'''
        '''评估主体'''
        xiaoWei.evaluationSubjectSave(projectNo)
        '''授信要素'''
        xiaoWei.creditElementSave(projectNo)
        '''准入要求'''
        xiaoWei.accessRquirementSave(projectNo)
        '''影像信息'''
        file = test_data.file
        for i in file:
            xiaoWei.attachmentSave(projectNo,i["fileId"],i["fileName"],i["subCategoryCode"])
        xiaoWei.attachmentNextStep(projectNo)
        xiaoWei.reqTextSave(projectNo)

        '''风险探测'''
        res_taskid = xiaoWei.getPro(projectNo)
        taskid = jsonpath.jsonpath(res_taskid, '$..taskId')[0]
        exec = ["authLetterValidDate", "supplierQuota", "antiTerrorism", "relatedPartyQueries", "financingAmount",
                "projectAmtEvaluateSubject", "totalRecoveryPrincipal", "leaseQuota"]
        detectorCode = "project_credit:auditApply"
        for i in exec:
            xiaoWei.detectorExec(i, taskid, detectorCode)
        '''提交审核'''
        xiaoWei.opinionSumit(taskid)



    '''业务主管登录'''
    if node >= 2:
        '''获取数据库xirr值'''
        res_sql = Sys_param_config.objects.filter(config_type="xirr_guidance").all()
        xirr = float(res_sql[0].config_value)
        '''获取项目xirr值'''
        res_xirr = float(xiaoWei.getPro(projectNo)["data"]["projectTotalXirrRate"])
        # if res_xirr > xirr :
        #     Sys_param_config.objects.filter(config_type="xirr_guidance").update(config_value=res_xirr+1)
        if res_xirr < xirr:
            Sys_param_config.objects.filter(config_type="xirr_guidance").update(config_value=res_xirr-1)
        if custName == "xzw":
            xiaoWei.updateHeader("moziluo")
            res = xiaoWei.todoListApp()
            for i in res["content"] :
                if i["businessKey"] == projectNo:
                    taskid = i["id"]
                    break;
            xiaoWei.opinionSumit(taskid)
        else:
            xiaoWei.updateHeader("huangzuning")
            res = xiaoWei.todoListApp()
            for i in res["content"]:
                if i["businessKey"] == projectNo:
                    taskid = i["id"]
                    break;
            xiaoWei.opinionSumit(taskid)

    #
    # '''区域部负责人登录'''
    # if node >= 3:
    #     if custName == "xzw":
    #         xiaoWei.updateHeader("fengyong")
    #         res = xiaoWei.todoListApp()
    #         for i in res["content"]:
    #             if i["businessKey"] == projectNo:
    #                 taskid = i["id"]
    #                 break;
    #         exec = ["antiTerrorism"]
    #         detectorCode = "project_credit:areaManagerApprove"
    #         for i in exec:
    #             xiaoWei.detectorExec(i, taskid, detectorCode)
    #         xiaoWei.opinionSumit(taskid)
    #     else:
    #         xiaoWei.updateHeader("majie")
    #         res = xiaoWei.todoListApp()
    #         for i in res["content"]:
    #             if i["businessKey"] == projectNo:
    #                 taskid = i["id"]
    #                 break;
    #         exec = ["antiTerrorism"]
    #         detectorCode = "project_credit:areaManagerApprove"
    #         for i in exec:
    #             xiaoWei.detectorExec(i, taskid, detectorCode)
    #         xiaoWei.opinionSumit(taskid)


    '''风控终审'''
    if node >= 4:
        time.sleep(60)
        xiaoWei.headers = headers_cust
        while True:
            count = 0
            res = xiaoWei.pro_page()
            for i in res["data"]["records"]:
                if i["projectNo"] == projectNo:
                    if i["statusName"] == "评审经理审批中":
                        count = 1
                        break;
            if count == 1:
                break;
        '''评审经理登录'''
        xiaoWei.updateHeader("zonghao")
        taskid = xiaoWei.getPcTask(projectNo)
        exec = ["supplierBlackAndGreyList", "antiTerrorism"]
        detectorCode = "project_credit:auditManagerApprove"
        for i in exec:
            xiaoWei.detectorExec(i, taskid, detectorCode)
        xiaoWei.opinionSumit(taskid)


    '''评审主管登录'''
    if node >= 5:
        time.sleep(1)
        if custName == "xzw":
            xiaoWei.updateHeader("jiaohailong")
            taskid = xiaoWei.getPcTask(projectNo)
            exec = ["supplierBlackAndGreyList", "antiTerrorism"]
            detectorCode = "project_credit:auditSupervisorApprove"
            for i in exec:
                xiaoWei.detectorExec(i, taskid, detectorCode)
            xiaoWei.opinionSumit(taskid)
        else:
            xiaoWei.updateHeader("uat")
            taskid = xiaoWei.getPcTask(projectNo)
            exec = ["supplierBlackAndGreyList", "antiTerrorism"]
            detectorCode = "project_credit:auditSupervisorApprove"
            for i in exec:
                xiaoWei.detectorExec(i, taskid, detectorCode)
            time.sleep(1)
            xiaoWei.opinionSumit(taskid)


    '''有权人登录'''
    if node >= 6:
        if custName == "xzw":
            xiaoWei.updateHeader("caijieru")

            taskid = xiaoWei.getPcTask(projectNo)

            xiaoWei.opinionSumit(taskid)
        else:
            taskid = xiaoWei.getPcTask(projectNo)

            xiaoWei.opinionSumit(taskid)


    result = xiaoWei.result(start_time, projectNo)
    send_notify(custName,projectNo)
    return JsonResponse(result, json_dumps_params={'ensure_ascii': False})




    # end_time = time.time()
    # run_time = round(end_time - start_time,2)
    # #
    # # result = {
    # #     "code": 200,
    # #     "status": True,
    # #     "message": 'success,耗时%ss,打开app项目列表查看新建项目！！！'% run_time,
    # #     "data": "项目编号：%s" %projectNo
    # # }
    #
    # # return HttpResponse("提交成功,打开app项目列表查看新建项目！！！")
    # return JsonResponse(result,json_dumps_params={'ensure_ascii':False})












