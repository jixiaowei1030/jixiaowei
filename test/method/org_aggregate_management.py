from demo_pytest_new.common.base import Base
import time
import os
from datetime import datetime

class Org_aggregate_management(Base):

    '''调用量任务管理查询'''
    def call_volume_task_management_select(self):
        self.logger.info("------------调用量任务管理查询----------")
        self.search_for_directory("调用量任务管理")
        self.click("xpath", "//div/ul[2]/li[contains(text(),'调用量任务管理')]")
        time.sleep(0.5)
        self.click("xpath","//div[@items='服务接口调用量任务管理']/../div[2]/div/button[1]")
        time.sleep(1)
        self.click("xpath","//div[text()='查询服务接口调用量任务']/../../div[2]/form/div[2]/div/div/div/div/input")
        self.click("xpath","//div[text()='查询服务接口调用量任务']/../../div[2]/form/div[2]/div/div/div[2]/ul[2]/li[1]")
        self.click("xpath","//div[@class='ivu-modal-wrap']/div/div/div[3]/*[2]")

    '''日切账单错误信息管理查询'''
    def error_information_of_daily_cutting_bill_select(self):
        self.logger.info("------------日切账单错误信息管理查询----------")
        self.search_for_directory("日切账单错误信息管理")
        self.click("xpath", "//div/ul[2]/li[contains(text(),'日切账单错误信息管理')]")
        self.click("xpath", "//div[@items='日切账单错误信息管理']/../div[2]/div/button[1]")
        time.sleep(1)
        self.click("xpath","//div[text()='查询日切账单错误信息']/../../div[2]/form/div[2]/div/div/div/div/input")
        self.click("xpath","//div[text()='查询日切账单错误信息']/../../div[2]/form/div[2]/div/div/div[2]/ul[2]/li[1]")
        self.click("xpath","//div[@class='ivu-modal-wrap']/div/div/div[3]/*[2]")

    '''日切账单管理查询'''
    def daily_cutting_bill_select(self):
        self.logger.info("------------日切账单管理查询----------")
        self.search_for_directory("日切账单管理")
        self.click("xpath", "//div/ul[2]/li[contains(text(),'日切账单管理')]")
        self.click("xpath", "//div[@items='日切账单信息管理']/../div[2]/div/button[1]")
        time.sleep(2)
        self.click("xpath","//div[text()='查询日切账单信息']/../../div[2]/form/div[1]/div/div/div/div/input")
        self.click("xpath","//div[text()='查询日切账单信息']/../../div[2]/form/div[1]/div/div/div[2]/ul[2]/li[1]")
        time.sleep(0.5)
        self.click("xpath","//div[@class='ivu-modal-wrap']/div/div/div[3]/*[2]")


    '''日切账单管理下载'''
    def daily_cutting_bill_download(self,start_date,end_date):
        #转换日期格式
        data1 = datetime.strptime(start_date, "%Y-%m-%d").strftime("%Y.%m.%d")
        data2 = datetime.strptime(end_date, "%Y-%m-%d").strftime("%Y.%m.%d")
        self.logger.info("------------日切账单管理下载----------")
        self.click("xpath", "//div[@items='日切账单信息管理']/../div[2]/div/button[2]")
        time.sleep(1)
        self.click("xpath","//div[text()='下载']/../../div[2]/form/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div/input")
        self.sendkeys(start_date,"xpath","//div[text()='下载']/../../div[2]/form/div[1]/div/div/div[1]/div/div/div[1]/div[1]/div/input")
        self.click("xpath","//div[text()='下载']/../../div[2]/form/div[1]/div/div/div[3]/div/div/div[1]/div[1]/div/input")
        self.click("xpath","//div[text()='下载']/../../div[2]/form/div[1]/div/div/div[3]/div/div/div[1]/div[1]/div/input")
        self.sendkeys(end_date,"xpath","//div[text()='下载']/../../div[2]/form/div[1]/div/div/div[3]/div/div/div[1]/div[1]/div/input")
        self.click("xpath","//div[text()='下载']")
        self.click("xpath","//div[@class='ivu-modal-wrap']/div/div/div[3]/*[2]")
        result=os.path.exists(("C:\\Users\\Administrator\\Downloads\\日收入报表%s-%s.xls")%(data1,data2))
        return result
