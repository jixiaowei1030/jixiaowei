#encoding='utf-8'

from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from Z500.tools import test_data
from Z500.common.login import login
# from Z500.models import Test
from Z500.models import Pay_main_info
from Z500.models import Sys_param_config
from Z500.models import Biz_flow_info
from Z500.models import Auth_user_sync_record
from Z500.models import Z500_test
from Z500.models import Proj_trades_supplier

from Z500.models import Auth_group
from Z500.tools.dingtalk import send_notify,send_notify_approve
from Z500.tools.xiaoWeiNew import xiaoWeiNew
from random import choice

from django.contrib import messages


import random
import time
import requests
import jsonpath
import datetime
import asyncio
import logging


# Create your views here.





def index(request):
    return HttpResponse("Hello world !  django ~~")

def demo(request):
    # asyncio.run(main(request))

    return render(request, 'demo.html')

    # messages.success(request, "哈哈哈哈")

    # print(request.GET["custName"])
    # cust = {"cust": request.GET["custName"]
    #            }
    #
    # return render(request, 'demo.html',cust)

async def foo(request):

    await asyncio.sleep(20)  # 模拟耗时操作
    print("异步任务完成1")
    return render(request, 'demo.html')


async def foo1(request):
    await asyncio.sleep(2)  # 模拟耗时操作
    print("异步任务完成2")
    return HttpResponse("Hello world !  django ~~")


async def main(request):
    print("开始执行异步任务")
    await asyncio.gather(foo(request), foo1(request))  # 同时执行多个异步任务
    print("所有异步任务执行完毕")
    return render(request, 'demo.html')



# 测试QQ号访问页面
def testMakeData(request):
    # return HttpResponse("Hello world !  django ~~")

    return render(request, 'get_demo.html')

def test_qq(request):
    return render(request, 'get_direction.html')

def testApprove(request):
    return render(request, 'get_demo1.html')

def testContract(request):
    return render(request, 'get_contract.html')

def testMiddleCode(request):
    return render(request, 'get_middleCode.html')

def testDirect(request):
    return render(request, 'get_direct.html')

def testPayment(request):
    return render(request, 'get_payment.html')

def testCheckMiddleCode(request):
    return render(request, 'get_checkMiddleCode.html')

def testPaymentApprove(request):
    return render(request, 'get_paymentApprove.html')



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





'''新建Z500项目'''
def test_add_pr(request):

    start_time = time.time()

    '''获取客户经理'''
    custName = request.GET["custName"]
    lesaseName = custName + "测试项目"
    node = int(request.GET["node"][-1])
    guarantor = request.GET["guarantor"]
    env = request.GET["env"]
    print(env)
    # if env == '':
    #     env = 'test'
    if guarantor == '':
        guarantor = '2'
    '''登录'''
    res = login(custName,env)
    headers_cust = {"AccessToken": res["access_token"]}
    xiaoWei = xiaoWeiNew(headers_cust,env)

    # projectNo = 'PJ202308210055'
    res = xiaoWei.add_pro(lesaseName)
    projectNo = res["data"]["projectNo"]
    '''征信授权'''
    xiaoWei.creditAuthSave(projectNo,custName,guarantor,env)
    xiaoWei.creditAuthBack(projectNo,custName,guarantor,env)

    '''预审提交'''
    res = xiaoWei.proSubmit(projectNo,guarantor)
    taskId = jsonpath.jsonpath(res,'$..taskId')[0]
    xiaoWei.opinionSumit(taskId)


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
        xiaoWei.supplierSave(projectNo, custName, env,projTrades[0],projTrades[1],projTrades[2],projTrades[3],projTrades[4],projTrades[5],projTrades[6],projTrades[7],projTrades[8])
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
        if env == 'sit':
            file = test_data.file_sit
        else:
            file = test_data.file_uat
        for i in file:
            xiaoWei.attachmentSave(projectNo,i["fileId"],i["fileName"],i["subCategoryCode"])
        templateCode = "projectCreditApproval"
        xiaoWei.attachmentNextStep(projectNo,templateCode)
        xiaoWei.reqTextSave(projectNo)

    if node >= 2:
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

    if env == 'sit':
        mysql_xiaowei = 'msdata_sit'
        mysql_ifc = 'ifc_dev'
    else:
        mysql_xiaowei = 'msdata_uat'
        mysql_ifc = 'default'

    '''业务主管登录'''
    if node >= 3:
        '''获取数据库xirr值'''
        res_sql = Sys_param_config.objects.using(mysql_ifc).filter(config_type="xirr_guidance").all()
        xirr = float(res_sql[0].config_value)
        '''获取项目xirr值'''
        res_xirr = float(xiaoWei.getPro(projectNo)["data"]["projectTotalXirrRate"])
        print(xirr,res_xirr)
        if res_xirr > xirr :
            Sys_param_config.objects.using(mysql_ifc).filter(config_type="xirr_guidance").update(config_value=res_xirr + 0.1)
        # if res_xirr < xirr:
        #     Sys_param_config.objects.filter(config_type="xirr_guidance").update(config_value=res_xirr-1)


        res_default = Biz_flow_info.objects.using(mysql_ifc).filter(business_key=projectNo).all()
        assignee = res_default[0].assignee
        print(res_default[0].assignee)
        print(res_default[0].task_id)
        res_msdata_uat = Auth_user_sync_record.objects.using(mysql_xiaowei).filter(UC_SYNC_ID=assignee).all()
        print(res_msdata_uat[0].USER_ID)
        user = res_msdata_uat[0].USER_ID

        xiaoWei.updateHeader(user, env)
        taskid = xiaoWei.getAppTask(projectNo)

        # res = xiaoWei.todoListApp()
        # for i in res["content"] :
        #     if i["businessKey"] == projectNo:
        #         taskid = i["id"]
        #         break;

        xiaoWei.opinionSumit(taskid)

    '''区域部负责人登录'''
    if node >= 4:

        res_default = Biz_flow_info.objects.using(mysql_ifc).filter(business_key=projectNo).all()
        # assignee = res_default[0].assignee

        if env == 'sit':
            assignee = "2c92948c892006ed01892a12b9ed0021"
        else:
            assignee = "2c9283aa897261430189fcdbf26c0022"
        print(res_default[0].assignee)
        print(res_default[0].task_id)
        res_msdata_uat = Auth_user_sync_record.objects.using(mysql_xiaowei).filter(UC_SYNC_ID=assignee).all()
        print(res_msdata_uat[0].USER_ID)
        user = res_msdata_uat[0].USER_ID

        xiaoWei.updateHeader(user,env)
        res = xiaoWei.todoListApp()
        for i in res["content"]:
            if i["businessKey"] == projectNo:
                taskid = i["id"]
                break;
        exec = ["antiTerrorism"]
        detectorCode = "project_credit:areaManagerApprove"
        for i in exec:
            xiaoWei.detectorExec(i, taskid, detectorCode)
        xiaoWei.opinionSumit(taskid)




    '''风控终审'''
    if node >= 5:
        print("风控终审")
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
        res_default = Biz_flow_info.objects.using(mysql_ifc).filter(business_key=projectNo).all()
        assignee = res_default[0].assignee
        print(res_default[0].assignee)
        print(res_default[0].task_id)
        res_msdata_uat = Auth_user_sync_record.objects.using(mysql_xiaowei).filter(UC_SYNC_ID=assignee).all()
        print(res_msdata_uat[0].USER_ID)
        user = res_msdata_uat[0].USER_ID

        xiaoWei.updateHeader(user,env)
        taskid = xiaoWei.getPcTask(projectNo)
        exec = ["supplierBlackAndGreyList", "antiTerrorism","supplierFrozenStatus"]
        detectorCode = "project_credit:auditManagerApprove"
        for i in exec:
            xiaoWei.detectorExec(i, taskid, detectorCode)
        xiaoWei.opinionSumit(taskid)


    '''评审主管登录'''
    if node >= 6:
        time.sleep(1)
        res_default = Biz_flow_info.objects.using(mysql_ifc).filter(business_key=projectNo).all()
        assignee = res_default[0].assignee
        print(res_default[0].assignee)
        print(res_default[0].task_id)
        res_msdata_uat = Auth_user_sync_record.objects.using(mysql_xiaowei).filter(UC_SYNC_ID=assignee).all()
        print(res_msdata_uat[0].USER_ID)
        user = res_msdata_uat[0].USER_ID
        xiaoWei.updateHeader(user, env)
        taskid = xiaoWei.getPcTask(projectNo)
        exec = ["supplierBlackAndGreyList", "antiTerrorism","supplierFrozenStatus"]
        detectorCode = "project_credit:auditSupervisorApprove"
        for i in exec:
            xiaoWei.detectorExec(i, taskid, detectorCode)
        xiaoWei.opinionSumit(taskid)



    '''有权人登录'''
    if node >= 7:
        res_default = Biz_flow_info.objects.using(mysql_ifc).filter(business_key=projectNo).all()
        assignee = res_default[0].assignee
        print(res_default[0].assignee)
        print(res_default[0].task_id)
        res_msdata_uat = Auth_user_sync_record.objects.using(mysql_xiaowei).filter(UC_SYNC_ID=assignee).all()
        print(res_msdata_uat[0].USER_ID)
        user = res_msdata_uat[0].USER_ID
        xiaoWei.updateHeader(user, env)

        taskid = xiaoWei.getPcTask(projectNo)

        xiaoWei.opinionSumit(taskid)




    result = xiaoWei.result(start_time, projectNo)
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    Z500_test.objects.using("local").create(name = custName, projectNo = projectNo, node = node, type = '0',create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    send_notify(env,custName,projectNo)
    return JsonResponse(result, json_dumps_params={'ensure_ascii': False})
    # return HttpResponse(result)

'''已有项目审批'''
def testApproveFlow(request):

    start_time = time.time()


    '''获取项目编号'''
    projectNo = request.GET["projectNo"].strip()
    print(projectNo)
    custName = request.GET["custName"]
    node = int(request.GET["node"][-1])
    env = request.GET["env"]
    print(env)


    if env == 'sit':
        mysql_xiaowei = 'msdata_sit'
        mysql_ifc = 'ifc_dev'
    else:
        mysql_xiaowei = 'msdata_uat'
        mysql_ifc = 'default'


    res_default = Biz_flow_info.objects.using(mysql_ifc).filter(business_key=projectNo).all()
    task_name = res_default[0].task_name

    if task_name == "业务主管审批":
        node_before = 2
    if task_name == "区域部负责人" or task_name == "区域部负责人审批":
        node_before = 3
    if task_name == "风控终审":
        node_before = 4
    if task_name == "评审经理审批":
        node_before = 4
    if task_name == "评审主管审批":
        node_before = 5


    # res_ifc = Z500_test.objects.using("local").filter(projectNo = projectNo).all()
    # node_before = int(res_ifc[0].node)

    '''登录'''
    res = login(custName, env)
    print(res)
    headers_cust = {"AccessToken": res["access_token"]}
    xiaoWei = xiaoWeiNew(headers_cust, env)

    '''业务主管登录'''
    if node >= 3 and node_before <3:

        res_default = Biz_flow_info.objects.using(mysql_ifc).filter(business_key=projectNo).all()
        assignee = res_default[0].assignee
        print(res_default[0].assignee)
        print(res_default[0].task_id)
        res_msdata_uat = Auth_user_sync_record.objects.using(mysql_xiaowei).filter(UC_SYNC_ID=assignee).all()
        print(res_msdata_uat[0].USER_ID)
        user = res_msdata_uat[0].USER_ID

        xiaoWei.updateHeader(user,env)

        # res = login(user, env)
        # headers_cust = {"AccessToken": res["access_token"]}
        # xiaoWei = xiaoWeiNew(headers_cust, env)
        #
        # # xiaoWei.updateHeader(user, env)
        taskid = xiaoWei.getAppTask(projectNo)

        '''获取数据库xirr值'''
        res_sql = Sys_param_config.objects.using(mysql_ifc).filter(config_type="xirr_guidance").all()
        xirr = float(res_sql[0].config_value)
        '''获取项目xirr值'''
        res_xirr = float(xiaoWei.getPro(projectNo)["data"]["projectTotalXirrRate"])
        if res_xirr > xirr :
            Sys_param_config.objects.using(mysql_ifc).filter(config_type="xirr_guidance").update(config_value=res_xirr + 0.1)
        # if res_xirr < xirr:
        #     Sys_param_config.objects.filter(config_type="xirr_guidance").update(config_value=res_xirr - 1)

        # res = xiaoWei.todoListApp()
        # for i in res["content"] :
        #     if i["businessKey"] == projectNo:
        #         taskid = i["id"]
        #         break;

        xiaoWei.opinionSumit(taskid)


    '''区域部负责人登录'''
    if node >= 4 and node_before <4 :

        res_default = Biz_flow_info.objects.using(mysql_ifc).filter(business_key=projectNo).all()
        # assignee = res_default[0].assignee

        if env == 'sit' :
            if custName == 'jxw':
                assignee = "2c92948c892006ed01892a12b9ed0021"
            else :
                assignee = "2c92948c892006ed01892a38ba6f002a"
        else:
            assignee = "2c9283aa897261430189fcdbf26c0022"
        print(res_default[0].assignee)
        print(res_default[0].task_id)
        print(mysql_xiaowei)
        print(assignee)
        res_msdata_uat = Auth_user_sync_record.objects.using(mysql_xiaowei).filter(UC_SYNC_ID=assignee).all()
        print(res_msdata_uat[0].USER_ID)
        user = res_msdata_uat[0].USER_ID

        xiaoWei.updateHeader(user,env)
        res = xiaoWei.todoListApp()
        for i in res["content"]:
            if i["businessKey"] == projectNo:
                taskid = i["id"]
                break;
        exec = ["antiTerrorism"]
        detectorCode = "project_credit:areaManagerApprove"
        for i in exec:
            xiaoWei.detectorExec(i, taskid, detectorCode)
        xiaoWei.opinionSumit(taskid)

    '''风控终审'''
    if node >= 5 and node_before <5:
        time.sleep(60)
        xiaoWei.updateHeader(custName,env)
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
        res_default = Biz_flow_info.objects.using(mysql_ifc).filter(business_key=projectNo).all()
        assignee = res_default[0].assignee
        print(res_default[0].assignee)
        print(res_default[0].task_id)
        res_msdata_uat = Auth_user_sync_record.objects.using(mysql_xiaowei).filter(UC_SYNC_ID=assignee).all()
        print(res_msdata_uat[0].USER_ID)
        user = res_msdata_uat[0].USER_ID

        xiaoWei.updateHeader(user, env)
        taskid = xiaoWei.getPcTask(projectNo)
        exec = ["supplierBlackAndGreyList", "antiTerrorism", "supplierFrozenStatus"]
        detectorCode = "project_credit:auditManagerApprove"
        for i in exec:
            xiaoWei.detectorExec(i, taskid, detectorCode)
        xiaoWei.opinionSumit(taskid)

    '''评审主管登录'''
    if node >= 6 and node_before <6:
        time.sleep(1)
        res_default = Biz_flow_info.objects.using(mysql_ifc).filter(business_key=projectNo).all()
        assignee = res_default[0].assignee
        print(res_default[0].assignee)
        print(res_default[0].task_id)
        res_msdata_uat = Auth_user_sync_record.objects.using(mysql_xiaowei).filter(UC_SYNC_ID=assignee).all()
        print(res_msdata_uat[0].USER_ID)
        user = res_msdata_uat[0].USER_ID
        xiaoWei.updateHeader(user, env)
        taskid = xiaoWei.getPcTask(projectNo)
        exec = ["supplierBlackAndGreyList", "antiTerrorism", "supplierFrozenStatus"]
        detectorCode = "project_credit:auditSupervisorApprove"
        for i in exec:
            xiaoWei.detectorExec(i, taskid, detectorCode)
        xiaoWei.opinionSumit(taskid)

    '''有权人登录'''
    if node >= 7 and node_before <7:
        res_default = Biz_flow_info.objects.using(mysql_ifc).filter(business_key=projectNo).all()
        assignee = res_default[0].assignee
        print(res_default[0].assignee)
        print(res_default[0].task_id)
        res_msdata_uat = Auth_user_sync_record.objects.using(mysql_xiaowei).filter(UC_SYNC_ID=assignee).all()
        print(res_msdata_uat[0].USER_ID)
        user = res_msdata_uat[0].USER_ID
        xiaoWei.updateHeader(user, env)

        taskid = xiaoWei.getPcTask(projectNo)

        xiaoWei.opinionSumit(taskid)

    result = xiaoWei.result_approve(start_time, projectNo)
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    Z500_test.objects.using("local").create(name = custName, projectNo = projectNo, node = node, type = '1',create_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    send_notify_approve(env, custName, projectNo)

    response = JsonResponse(result, json_dumps_params={'ensure_ascii': False})
    # response['Connection'] = 'keep-alive'
    # response['Keep-Alive'] = 'timeout=300,max=1000'
    return response
    # return HttpResponse(result)

'''合同发起'''
def testContractAdd(request):
    start_time = time.time()

    payMainNo = request.GET["payMainNo"].strip()
    print(payMainNo)
    custName = request.GET["custName"]
    # node = int(request.GET["node"][-1])

    env = request.GET["env"]
    print(env)

    if env == 'sit':
        mysql_xiaowei = 'msdata_sit'
        mysql_ifc = 'ifc_dev'
    else:
        mysql_xiaowei = 'msdata_uat'
        mysql_ifc = 'default'

    res_default = Pay_main_info.objects.using(mysql_ifc).filter(pay_main_no=payMainNo).all()
    payInfoNo = res_default[0].pay_info_no
    projectNo = res_default[0].project_no
    print(payInfoNo,projectNo)

    '''登录'''
    res = login(custName, env)
    headers_cust = {"AccessToken": res["access_token"]}
    xiaoWei = xiaoWeiNew(headers_cust, env)


    res_apply_list = xiaoWei.payApplyListNo(payInfoNo)
    taskid = jsonpath.jsonpath(res_apply_list,'$..taskId')[0]
    print("taskid:"+taskid)


    '''客户信息'''
    xiaoWei.payCustEnterpriseSave(payInfoNo,projectNo)
    xiaoWei.payCustGuarantorSave(payInfoNo,projectNo)
    '''交易结构'''
    xiaoWei.payTradesSupplierSave(payInfoNo,projectNo)
    xiaoWei.payTradesLeaseholdSave(payInfoNo,projectNo)
    '''电签信息'''
    xiaoWei.paySupplementSave(payInfoNo,projectNo)

    exec = ["antiTerrorism", "relatedPartyQueries", "supplierBlackAndGreyList","invoiceExistCheck","supplierFrozenStatus"]
    detectorCode = "contract_payment:contractApply"
    for i in exec:
        xiaoWei.detectorExec(i, taskid, detectorCode)

    xiaoWei.opinionSumit(taskid)


    print("合同文件生成中")
    time.sleep(90)
    while True:
        time.sleep(1)
        count = 0
        res = xiaoWei.payApplyList(projectNo)
        for i in res["data"]["records"]:
            if i["payMainNo"] == payMainNo:
                if i["statusName"] == "待签约发起":
                    count = 1
                    break;
        if count == 1:
            break;


    res_apply_list = xiaoWei.payApplyListNo(payInfoNo)
    taskid = jsonpath.jsonpath(res_apply_list, '$..taskId')[0]
    print("taskid:"+taskid)
    xiaoWei.opinionSumit(taskid)

    result = xiaoWei.result_contract(start_time, payMainNo)

    return JsonResponse(result, json_dumps_params={'ensure_ascii': False})

'''待付款申请'''
def testPaymentAdd(request):
    start_time = time.time()


    payMainNo = request.GET["payMainNo"].strip()
    print(payMainNo)
    custName = request.GET["custName"]
    node = int(request.GET["node"][-1])

    env = request.GET["env"]
    print(env)

    if env == 'sit':
        mysql_xiaowei = 'msdata_sit'
        mysql_ifc = 'ifc_dev'
    else:
        mysql_xiaowei = 'msdata_uat'
        mysql_ifc = 'default'

    res_default = Pay_main_info.objects.using(mysql_ifc).filter(pay_main_no=payMainNo).all()
    payInfoNo = res_default[0].pay_info_no
    projectNo = res_default[0].project_no
    print(payInfoNo, projectNo)

    res_pay = Pay_main_info.objects.using(mysql_ifc).filter(pay_main_no=payMainNo).all()
    proj_trades_id = res_pay[0].proj_trades_id
    print(proj_trades_id)
    res_settle = Proj_trades_supplier.objects.using(mysql_ifc).filter(proj_trades_id=proj_trades_id).all()
    settle_mode = res_settle[0].settle_mode
    print(settle_mode)



    '''登录'''
    res = login(custName, env)
    headers_cust = {"AccessToken": res["access_token"]}
    xiaoWei = xiaoWeiNew(headers_cust, env)



    '''风险信息'''
    xiaoWei.riskInformationSave(payInfoNo, projectNo)

    '''付款信息'''
    xiaoWei.requestFundsSave(payInfoNo, projectNo)

    '''寄送信息'''
    xiaoWei.requestFundsSendSave(payInfoNo, projectNo)

    '''影像信息'''
    templateCode = "paymentRequest"
    xiaoWei.attachmentNextStep(payInfoNo, templateCode)

    res_apply_list = xiaoWei.payApplyListNo(payInfoNo)
    taskid = jsonpath.jsonpath(res_apply_list, '$..taskId')[0]
    print("taskid:" + taskid)

    xiaoWei.opinionSumit(taskid)




    '''评审经理登录'''
    if node >= 9:
        print("信用审查中")
        time.sleep(60)
        xiaoWei.headers = headers_cust
        while True:
            count = 0
            res = xiaoWei.payApplyList(projectNo)
            for i in res["data"]["records"]:
                if i["projectNo"] == projectNo:
                    if i["statusName"] == "信用审批中":
                        count = 1
                        break;
            if count == 1:
                break;
        time.sleep(1)
        res_default = Biz_flow_info.objects.using(mysql_ifc).filter(business_key=payInfoNo).all()
        assignee = res_default[0].assignee
        print(res_default[0].assignee)
        print(res_default[0].task_id)
        res_msdata_uat = Auth_user_sync_record.objects.using(mysql_xiaowei).filter(UC_SYNC_ID=assignee).all()
        print(res_msdata_uat[0].USER_ID)
        user = res_msdata_uat[0].USER_ID
        xiaoWei.updateHeader(user, env)
        taskid = xiaoWei.getPcTask(payInfoNo)
        exec = ["supplierBlackAndGreyList", "antiTerrorism", "supplierFrozenStatus", "supplierTicketTakeStatus"]
        detectorCode = "contract_payment:auditManagerApprove"
        for i in exec:
            xiaoWei.detectorExec(i, taskid, detectorCode)
        xiaoWei.opinionSumit(taskid)

    '''金融市场部审批'''
    if node >=10 and settle_mode != "TelegraphicTransfer":
        time.sleep(1)
        res_default = Biz_flow_info.objects.using(mysql_ifc).filter(business_key=payInfoNo).all()
        assignee = res_default[0].assignee
        print(res_default[0].assignee)
        print(res_default[0].task_id)
        res_msdata_uat = Auth_user_sync_record.objects.using(mysql_xiaowei).filter(UC_SYNC_ID=assignee).all()
        print(res_msdata_uat[0].USER_ID)
        user = res_msdata_uat[0].USER_ID
        xiaoWei.updateHeader(user, env)
        taskid = xiaoWei.getAppTask(projectNo)

        '''金融市场部审批页面-保存'''
        xiaoWei.departmentSave(payInfoNo)

        xiaoWei.opinionSumit(taskid)


    result = xiaoWei.result_payment(start_time, payMainNo)


    return JsonResponse(result, json_dumps_params={'ensure_ascii': False})


'''付款审批'''
def testPaymentApproveFlow(request):

    start_time = time.time()


    '''获取合同编号'''
    payMainNo = request.GET["payMainNo"].strip()
    print(payMainNo)
    custName = request.GET["custName"]
    node = int(request.GET["node"][-2:])
    env = request.GET["env"]
    print(env)

    if env == 'sit':
        mysql_xiaowei = 'msdata_sit'
        mysql_ifc = 'ifc_dev'
    else:
        mysql_xiaowei = 'msdata_uat'
        mysql_ifc = 'default'

    res_default = Pay_main_info.objects.using(mysql_ifc).filter(pay_main_no=payMainNo).all()
    payInfoNo = res_default[0].pay_info_no
    projectNo = res_default[0].project_no
    print(payInfoNo, projectNo)



    res_default = Biz_flow_info.objects.using(mysql_ifc).filter(business_key=payInfoNo).all()
    task_name = res_default[0].task_name
    print(task_name)

    '''获取付款方式'''
    res_pay = Pay_main_info.objects.using(mysql_ifc).filter(pay_main_no=payMainNo).all()
    proj_trades_id = res_pay[0].proj_trades_id
    print(proj_trades_id)
    res_settle = Proj_trades_supplier.objects.using(mysql_ifc).filter(proj_trades_id=proj_trades_id).all()
    settle_mode = res_settle[0].settle_mode
    print(settle_mode)

    if task_name == "信用审查中":
        node_before = 8
    if task_name == "评审经理审批":
        node_before = 8
    if task_name == "金融市场部审批" :
        node_before = 9
    if task_name == "放款管理岗审批":
        node_before = 10


    '''登录'''
    res = login(custName, env)
    print(res)
    headers_cust = {"AccessToken": res["access_token"]}
    xiaoWei = xiaoWeiNew(headers_cust, env)



    '''评审经理审批'''
    if node >= 9 and node_before < 9:
        print("信用审查中")
        time.sleep(60)
        xiaoWei.headers = headers_cust
        while True:
            count = 0
            res = xiaoWei.payApplyList(projectNo)
            for i in res["data"]["records"]:
                if i["projectNo"] == projectNo:
                    if i["statusName"] == "信用审批中":
                        count = 1
                        break;
            if count == 1:
                break;
        time.sleep(1)
        res_default = Biz_flow_info.objects.using(mysql_ifc).filter(business_key=payInfoNo).all()
        assignee = res_default[0].assignee
        print(res_default[0].assignee)
        print(res_default[0].task_id)
        res_msdata_uat = Auth_user_sync_record.objects.using(mysql_xiaowei).filter(UC_SYNC_ID=assignee).all()
        print(res_msdata_uat[0].USER_ID)
        user = res_msdata_uat[0].USER_ID
        xiaoWei.updateHeader(user, env)
        taskid = xiaoWei.getPcTask(payInfoNo)
        exec = ["supplierBlackAndGreyList", "antiTerrorism", "supplierFrozenStatus", "supplierTicketTakeStatus"]
        detectorCode = "contract_payment:auditManagerApprove"
        for i in exec:
            xiaoWei.detectorExec(i, taskid, detectorCode)
        xiaoWei.opinionSumit(taskid)

    print(node,node_before)

    '''金融市场部审批'''
    if node >= 10 and node_before < 10 and settle_mode != "TelegraphicTransfer":
        time.sleep(1)
        res_default = Biz_flow_info.objects.using(mysql_ifc).filter(business_key=payInfoNo).all()
        assignee = res_default[0].assignee
        print(res_default[0].assignee)
        print(res_default[0].task_id)
        res_msdata_uat = Auth_user_sync_record.objects.using(mysql_xiaowei).filter(UC_SYNC_ID=assignee).all()
        print(res_msdata_uat[0].USER_ID)
        user = res_msdata_uat[0].USER_ID
        xiaoWei.updateHeader(user, env)
        taskid = xiaoWei.getAppTask(payInfoNo)

        '''金融市场部审批页面-保存'''
        xiaoWei.departmentSave(payInfoNo)

        xiaoWei.opinionSumit(taskid)

    result = xiaoWei.resultPaymentApprove(start_time, payMainNo)

    return JsonResponse(result, json_dumps_params={'ensure_ascii': False})



'''中征码查询'''
def testMiddleCodeQuery(request):
    list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    PCC_wi = [1, 3, 5, 7, 11, 2, 13, 1, 1, 17, 19, 97, 23, 29];
    d = random.randint(1, 99)
    while True:
        res = 0
        sum = 0
        code = []
        for i in range(14):
            # print(i)
            a = choice(list)
            code.append(a)
            c = list.index(a)
            b = PCC_wi[i]
            sum += b * c
        res = sum % 97 + 1
        if res == d:
            # print(code)
            break;
    if d < 10:
        result = {
            # "code": 0,
            "data": "中征码："+''.join(code) + '0' + str(d)
        }
        print(''.join(code) + '0' + str(d))
        return JsonResponse(result, json_dumps_params={'ensure_ascii': False})
    else:
        result = {
            # "code": 0,
            "data": "中征码："+''.join(code) + str(d)
        }
        print(''.join(code) + str(d))
        return JsonResponse(result, json_dumps_params={'ensure_ascii': False})

'''中征码校验'''
def testMiddleCodeCheck(request):
    print("11111")
    code = request.GET["code"].strip()
    if len(code) != 16:
        return False
    wi = [1,3,5,7,11,2,13,1,1,17,19,97,23,29]
    ci_position = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sum = 0
    for i in range(14):
        tmp = ci_position.index(code[i])
        if tmp == -1:
            return False
        sum += tmp*wi[i]
    cb2 = sum%97 +1
    try :
        sl2 = int(code[14:16])
    except:
        return False
    rst = cb2==sl2
    if rst :
        result = {
            "message": "中征码格式正确",
        }
        return JsonResponse(result)
    else:
        result = {
            "message": "中征码格式错误",
        }
        return JsonResponse(result)
# def testApproveFlow(request):
#     test =Z500_test.objects.using("local").create(name='jxw',count="1")
#     test.save()
#     result = {
#         "code": 20000,
#         "status": True,
#         "message": "success",
#     }
#     return JsonResponse(result)


# def test_add_pr(request):
#     # 生成一个以当前文件名为名字的logger实例
#     print("11111111111111111111")
#     logger = logging.getLogger(__name__)
#
#     # 生成一个名为collect的logger实例
#     collect_logger = logging.getLogger("collect")
#
#     def index(request):
#         logger.debug("一个萌萌的请求过来了。。。。")
#
#     logger.info("一个更萌的请求过来了。。。。")
#     logger.debug("这是app01里面的index视图函数")
#     collect_logger.info("用户1:河南")
#
#     return HttpResponse("OK")


