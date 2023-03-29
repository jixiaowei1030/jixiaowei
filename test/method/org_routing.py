# coding=utf-8
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from demo_pytest_new.common.base import Base

class Org_routing(Base):

    def is_login_sucess(self):
        try:
            t = self.driver.find_element_by_xpath("//ul[@class='ivu-menu ivu-menu-dark ivu-menu-vertical']/li[3]").text
            # print(t)
            return t
        except:
            return ""

    def is_login_failure(self):
        try:
            t = self.driver.switch_to.alert
            print(t.text)
            t.accept()
        except:
            return "登录失败"

    def is_title(self, _title):
        try:
            result=WebDriverWait(self.driver, self.timeout,self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_text_in_element(self,text):
        try:
            loca1=("xpath","//div[@class='layout-logo']/span")
            result=WebDriverWait(self.driver, self.timeout,self.t).until(EC.text_to_be_present_in_element(loca1,text))
            return result
        except :
            return False

    '''路由策略信息管理定位'''
    def routing_policy(self):
        sleep(2)
        self.click("xpath","//ul[@class='ivu-menu ivu-menu-dark ivu-menu-vertical']/li[4]/ul/li[1]")

        '''路由映射定位'''
    def routing_mapping(self):
        sleep(2)
        self.click("xpath", "//ul[@class='ivu-menu ivu-menu-dark ivu-menu-vertical']/li[4]/ul/li[2]")

        '''标准化接口定位'''
    def Standardized_interface(self):
        sleep(4)
        self.click("xpath", "//ul[@class='ivu-menu ivu-menu-dark ivu-menu-vertical']/li[4]/ul/li[3]")

        '''商户调用策略管理定位'''
    def call_policy(self):
        sleep(4)
        self.click("xpath", "//ul[@class='ivu-menu ivu-menu-dark ivu-menu-vertical']/li[4]/ul/li[4]")

        '''路由策略信息管理增加'''
    def routing_policy_information_management_add(self,name,code):
        self.logger.info("------------路由策略信息管理增加----------")
        self.search_for_directory("路由策略信息管理")
        self.click("xpath", "//div/ul[2]/li[contains(text(),'路由策略信息管理')]")
        sleep(1)
        self.click("xpath","//div[@items='路由策略信息管理']/../div[2]/div/button[2]")
        self.driver.find_elements_by_xpath('//*[text()="策略名称"]/../div/div/input')[0].send_keys(name)
        self.driver.find_elements_by_xpath('//*[text()="策略代码"]/../div/div/input')[0].send_keys(code)
        self.driver.find_elements_by_xpath('//*[text()="确定"]/..')[1].click()


    '''断言：路由策略信息管理增加，元素在当前界面上'''
    def is_dom_element_add2(self,name):
        try:
            loca2=("xpath","//tr/td[@class='ivu-table-column-center'][1]/div/span[text()=%a]" %name )
            WebDriverWait(self.driver, self.timeout,self.t).until(EC.presence_of_element_located(loca2))
            return True
        except:
            print("元素没有添加成功")
            return False

    '''断言：路由策略信息管理增加，实际结果与预期结果文本是否一致'''
    def is_equal_add(self,name):
        try:
            result=self.findElement("xpath","//tr/td[@class='ivu-table-column-center'][1]/div/span[text()=%a]" %name).text
            assert(name==self.findElement("xpath","//tr/td[@class='ivu-table-column-center'][1]/div/span[text()=%a]" %name).text)
            return True
        except:
            return False

    '''路由策略信息管理查询'''
    def routing_policy_information_management_select(self,name="",code=""):
        self.logger.info("------------路由策略信息管理查询----------")
        sleep(1)
        self.click("xpath","//*[text()='查询']/../..")
        sleep(1)
        self.driver.find_elements_by_xpath('//*[text()="策略名称"]/../div/div/input')[2].clear()
        self.driver.find_elements_by_xpath('//*[text()="策略名称"]/../div/div/input')[2].send_keys(name)
        self.driver.find_elements_by_xpath('//*[text()="策略代码"]/../div/div/input')[2].clear()
        self.driver.find_elements_by_xpath('//*[text()="策略代码"]/../div/div/input')[2].send_keys(code)
        self.click("xpath","//div[text()='查询路由策略信息']/../../div[3]/button[2]")



    '''路由策略信息管理删除'''
    def routing_policy_information_management_delete(self):
        self.logger.info("------------路由策略信息管理删除----------")
        sleep(1)
        self.click("xpath","//*[@items='路由策略信息管理']/../div[3]/*[1]/div/*[4]/*[2]/table/tbody/tr/td[1]/div[1]/label/span/input")
        # t=self.driver.find_element_by_xpath('//*[@items="路由策略信息管理"]/../div[3]/*[1]/div/*[4]/*[2]/table/tbody/tr/td[1]/div[1]/label/span/input').tag_name
        # print(t)
        self.driver.find_element_by_xpath('//*[text()="删除"]/../..').click()
        sleep(0.5)
        self.click("xpath","//div[text()='删除路由策略信息']/../../div[3]/div/div/div[1]")


    '''断言：路由策略信息管理删除，元素不在当前界面上'''
    def is_dom_element_delete2(self, name):
        try:
            loca2 = ("xpath", "//tr/td[@class='ivu-table-column-center'][1]/div/span[text()=%a]" % name)
            WebDriverWait(self.driver, 5, self.t).until(EC.presence_of_element_located(loca2))
            print("元素没有删除成功")
            return False
        except:
            return True


    '''路由策略信息管理修改'''
    def routing_policy_information_management_update(self,name,code):
        self.logger.info("------------路由策略信息管理修改----------")
        sleep(1)
        self.click("xpath","//*[@items='路由策略信息管理']/../div[3]/*[1]/div/*[4]/*[2]/table/tbody/tr/td[1]/div[1]/label/span/input")
        self.driver.find_element_by_xpath('//*[text()="修改"]/../..').click()
        self.driver.find_elements_by_xpath('//*[text()="策略名称"]/../div/div/input')[1].clear()
        self.driver.find_elements_by_xpath('//*[text()="策略代码"]/../div/div/input')[1].clear()
        self.driver.find_elements_by_xpath('//*[text()="策略名称"]/../div/div/input')[1].send_keys(name)
        self.driver.find_elements_by_xpath('//*[text()="策略代码"]/../div/div/input')[1].send_keys(code)
        self.click("xpath","//div[text()='修改路由策略信息']/../../div[3]/button[2]")
        # self.driver.find_element_by_xpath('//i[@class="ivu-icon ivu-icon-ios-close-empty rgb(255, 255, 255)"]').click()

    '''断言：路由策略信息管理修改，元素在当前界面上'''
    def is_dom_element_update2(self, name):
        try:
            loca2 = ("xpath", "//tr/td[@class='ivu-table-column-center'][1]/div/span[text()=%a]" % name)
            WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(loca2))
            sleep(2)
            self.driver.find_element_by_xpath('//i[@class="ivu-icon ivu-icon-ios-close-empty rgb(255, 255, 255)"]').click()
            return True
        except:
            self.driver.find_element_by_xpath('//i[@class="ivu-icon ivu-icon-ios-close-empty rgb(255, 255, 255)"]').click()
            return False


    '''标准化接口管理查询'''
    def standardized_interface_select(self,name,code=""):
        self.logger.info("------------标准化接口管理查询----------")
        sleep(1)
        self.click("xpath","//div[@items='标准化接口管理']/../div[2]/div/*[1]")
        self.driver.find_element_by_xpath('//*[text()="接口名称"]/../div/div/input').clear()
        self.driver.find_element_by_xpath('//*[text()="接口标识"]/../div/div/input').clear()
        self.driver.find_element_by_xpath('//*[text()="接口名称"]/../div/div/input').send_keys(name)
        self.driver.find_element_by_xpath('//*[text()="接口标识"]/../div/div/input').send_keys(code)
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]').click()

    '''断言：标准化接口管理查询成功'''
    def standardized_interface_selectsuccess(self,code):
        try:
            loca2 = ("xpath", "//tr/td[@class='ivu-table-column-center'][2]/div/span[text()=%a]" % code)
            WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(loca2))
            return True
        except:
            print("查询失败")
            return False

    '''标准化接口管理增加'''
    def standardized_interface_add(self,name,code,parameter):
        self.logger.info("------------标准化接口管理增加----------")
        self.search_for_directory("标准化接口管理")
        self.click("xpath", "//div/ul[2]/li[contains(text(),'标准化接口管理')]")
        sleep(2)
        self.click("xpath","//div[@items='标准化接口管理']/../div[2]/div/*[2]")
        self.driver.find_elements_by_xpath('//*[text()="标准化接口名称"]/../div/div/input')[0].send_keys(name)
        self.driver.find_elements_by_xpath('//*[text()="标准化接口标识"]/../div/div/input')[0].send_keys(code)
        self.driver.find_elements_by_xpath('//*[text()="接口请求参数"]/../div/div/*')[0].send_keys(parameter)
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]').click()

    '''标准化接口管理删除'''
    def standardized_interface_delete(self):
        sleep(1)
        self.click("xpath","//div[@items='标准化接口管理']/../div[3]/div/div/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/input")  #问题
        self.driver.find_element_by_xpath('//div[@items="标准化接口管理"]/../div[2]/div/*[3]').click()
        sleep(0.5)
        self.click("xpath","//div[text()='删除标准化接口']/../../div[3]/div/div/div[1]")



    '''标准化接口管理修改'''
    def standardized_interface_update(self,name,code,parameter):
        self.logger.info("------------标准化接口管理修改----------")
        sleep(1)
        self.click("xpath","//div[@items='标准化接口管理']/../div[3]/div/div/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/input")
        self.driver.find_element_by_xpath('//div[@items="标准化接口管理"]/../div[2]/div/*[4]').click()
        self.driver.find_elements_by_xpath('//*[text()="标准化接口名称"]/../div/div/input')[1].clear()
        self.driver.find_elements_by_xpath('//*[text()="标准化接口标识"]/../div/div/input')[1].clear()
        self.driver.find_elements_by_xpath('//*[text()="接口请求参数"]/../div/div/*')[1].clear()
        self.driver.find_elements_by_xpath('//*[text()="标准化接口名称"]/../div/div/input')[1].send_keys(name)
        self.driver.find_elements_by_xpath('//*[text()="标准化接口标识"]/../div/div/input')[1].send_keys(code)
        self.driver.find_elements_by_xpath('//*[text()="接口请求参数"]/../div/div/*')[1].send_keys(parameter)
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]').click()



    '''标准化接口管理绑定策略'''
    def bandingcelue(self,name,code,parameter):
        self.logger.info("------------标准化接口管理绑定策略----------")
        self.standardized_interface_add(name,code,parameter)
        sleep(1)
        self.standardized_interface_select(name,code)
        sleep(1)
        self.driver.find_element_by_xpath('//div[@items="标准化接口管理"]/../div[3]/div/div/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/input').click()
        self.driver.find_element_by_xpath('//div[@items="标准化接口管理"]/../div[2]/div/*[5]').click()

        # 增加
        sleep(2)
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[1]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[text()="策略名称"]/../div/div/div/div/div/input').click()
        self.driver.find_element_by_xpath('//*[text()=" 主备模式/master-slave"]').click()
        sleep(0.5)
        self.driver.find_elements_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]')[1].click()


        # 修改
        sleep(2)
        self.driver.find_element_by_xpath('//div[6]/div[2]/div/div/div[2]/div/div[2]/div/div/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/input').click()
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[3]').click()
        self.click("xpath","//*[text()='策略名称']/../div/div/div/div/div/input")
        self.driver.find_element_by_xpath('//*[text()=" 轮询负载/round-robin-balance"]').click()
        sleep(1)
        self.driver.find_elements_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]')[1].click()
        sleep(2)


        # 删除
        self.click("xpath","//div[6]/div[2]/div/div/div[2]/div/div[2]/div/div/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/input")
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[2]').click()
        sleep(0.25)
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/div/*[1]/div[1]').click()
        sleep(1)
        try:
            loca1 = ("xpath", "//span[text()='删除成功']")
            WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(loca1))
            self.click("xpath", "//div[@class='ivu-modal-wrap']/div/div/div[3]/*[2]")
            return True
        except:
            print("没有删除成功提示")
            self.click("xpath", "//div[@class='ivu-modal-wrap']/div/div/div[3]/*[2]")
            return False


    '''标准化接口管理绑定商户策略'''
    def merchant_strategy(self,name,code,parameter):
        self.logger.info("------------标准化接口管理绑定商户策略----------")
        self.standardized_interface_add(name,code,parameter)
        sleep(2)
        self.standardized_interface_select(name,code)
        sleep(2)
        self.driver.find_element_by_xpath('//div[@items="标准化接口管理"]/../div[3]/div/div/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/input').click()
        self.driver.find_element_by_xpath('//div[@items="标准化接口管理"]/../div[2]/div/*[6]').click()


        # 增加
        sleep(2)
        self.click("xpath","//div[@class='ivu-modal-wrap']/div/div/div[2]/div/div[1]/div/*[1]")
        sleep(1)
        self.click("xpath","//*[text()='机构代码']/../div/div/div/div/input")
        self.click("xpath","//div[text()='新增策略']/../../div[2]/form/div[1]/div/div/div[2]/ul[2]/li[1]")
        sleep(1)
        self.click("xpath","//*[text()='策略名称']/../div/div/div/div[1]/div/input")
        self.click("xpath","//*[text()=' 主备模式/master-slave']/../li[1]")
        sleep(1)
        self.driver.find_elements_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]')[1].click()

        # 修改
        sleep(2)
        self.click("xpath","//div[7]/div[2]/div/div/div[2]/div/div[2]/div/div/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/input")
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[3]').click()
        self.click("xpath","//*[text()='策略名称']/../div/div/div/div[1]/div/input")
        self.click("xpath","//*[text()=' 主备模式/master-slave']/../li[2]")
        sleep(1)
        self.driver.find_elements_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]')[1].click()
        sleep(1)


        # 删除
        sleep(2)
        self.driver.find_element_by_xpath('//div[7]/div[2]/div/div/div[2]/div/div[2]/div/div/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/input').click()
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[2]').click()
        sleep(0.5)
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/div/*[1]/div[1]').click()
        sleep(1)
        try:
            loca1 = ("xpath", "//span[text()='删除成功']")
            WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(loca1))
            self.click("xpath", "//div[@class='ivu-modal-wrap']/div/div/div[3]/*[2]")
            return True
        except:
            print("没有删除成功提示")
            self.click("xpath", "//div[@class='ivu-modal-wrap']/div/div/div[3]/*[2]")
            return False

    '''标准化接口管理默认路由'''
    def  default_routing(self,name,code,num):
        self.logger.info("------------标准化接口管理默认路由----------")
        self.search_for_directory("标准化接口管理")
        self.click("xpath", "//div/ul[2]/li[contains(text(),'标准化接口管理')]")
        sleep(2)
        self.standardized_interface_select(name,code)
        sleep(2)
        self.click("xpath",'//div[@items="标准化接口管理"]/../div[3]/div/div/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/input')
        sleep(2)
        self.driver.find_element_by_xpath('//div[@items="标准化接口管理"]/../div[2]/div/*[7]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[1]/button[1]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//label[text()="缓存有效期(小时)"]/../../div[1]/div/div/div[1]/div/input').click()
        self.driver.find_element_by_xpath('//label[text()="缓存有效期(小时)"]/../../div[1]/div/div/div[2]/ul[2]/li[%a]'%num).click()
        sleep(1)
        self.driver.find_elements_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]')[1].click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[text()="刷新"]/../..').click()

        # 上移
        sleep(2)
        self.click("xpath","//div[text()='默认路由']/../../div[2]/div/div[1]/div[3]/div/div/div[2]/table/tbody/tr[1]/td[1]/div/label/span/input")
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[1]/button[4]').click()
        sleep(2)
        self.click("xpath","//div[text()='默认路由']/../../div[2]/div/div[1]/div[3]/div/div/div[2]/table/tbody/tr[2]/td[1]/div/label/span/input")
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[1]/button[3]').click()


        # 删除
        sleep(2)
        self.driver.find_elements_by_xpath('//div[3]/div/div/div[2]/table/tbody/tr[2]/td[1]/div/label/span/input')[0].click()
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[1]/button[2]').click()
        self.driver.find_elements_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]')[1].click()
        try:
            loca1 = ("xpath", "//span[text()='删除成功']")
            WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(loca1))
            sleep(1)
            self.driver.find_element_by_xpath('//*[text()="刷新"]/../..').click()
            sleep(2)
            self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]').click()
            return True
        except:
            print("没有删除成功提示")
            sleep(2)
            self.driver.find_element_by_xpath('//*[text()="刷新"]/../..').click()
            sleep(2)
            self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]').click()
            return False


    '''标准化接口管理明细'''
    def detailed(self,name,code,parameter):
        self.logger.info("------------标准化接口管理明细----------")
        self.standardized_interface_add(name,code,parameter)
        self.standardized_interface_select(name, code)
        sleep(2)
        self.driver.find_element_by_xpath('//div[@items="标准化接口管理"]/../div[3]/div/div/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/input').click()
        self.driver.find_element_by_xpath('//div[@items="标准化接口管理"]/../div[2]/div/*[8]').click()
        sleep(2)
        self.click("xpath","//div[@class='ivu-modal-wrap']/div/div/div[2]/div/div[1]/div/*[1]")
        sleep(1)
        self.driver.find_element_by_xpath('//*[text()="数据源"]/../div/div/div[1]/div/input').click()
        self.driver.find_element_by_xpath('//form/div[1]/div[1]/div/div/div/div[2]/ul[2]/li[1]').click()
        self.driver.find_element_by_xpath('//*[text()="采集接口名"]/../div/div/input').send_keys("测试")
        self.driver.find_element_by_xpath('//*[text()="子接口唯一标识"]/../div/div/input').send_keys("测试")
        self.click("xpath","//*[text()='能力接口']/../div/div/button/i")
        sleep(0.5)
        self.click("xpath","//*[text()='能力接口']/../div/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/div/input")
        self.click("xpath","//*[text()='能力接口']/../div/div/div/div[1]/div/div[1]/div/div/div/div/div[2]/ul[2]/li[1]")
        self.click("xpath","//*[text()='能力接口']/../div/div/div/div[1]/div/div[3]/div/div/div/div[1]/div/input")
        self.click("xpath","//*[text()='能力接口']/../div/div/div/div[1]/div/div[3]/div/div/div/div[2]/ul[2]/li[1]")
        sleep(0.5)
        self.driver.find_elements_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]')[1].click()
        sleep(1)


        # 修改
        self.driver.find_element_by_xpath('//table[@style="width: 53px;"]/tbody/tr/td[1]/div/label/span/input').click()
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[3]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[text()="采集接口名"]/../div/div/input').send_keys("测试")
        self.driver.find_elements_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]')[1].click()
        sleep(1)

        # 默认指标
        self.driver.find_element_by_xpath('//table[@style="width: 53px;"]/tbody/tr/td[1]/div/label/span/input').click()
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[4]').click()

        sleep(1)
        self.driver.find_element_by_xpath('//*[text()="响应时长"]/../div/div/div/div/input').send_keys("250")
        self.driver.find_element_by_xpath('//*[text()="查得率"]/../div/div/div/div/input').send_keys("66")
        self.driver.find_element_by_xpath('//*[text()="准确率"]/../div/div/div/div/input').send_keys("77")
        self.driver.find_element_by_xpath('//*[text()="单价"]/../div/div/div/div/input').send_keys("11")
        self.driver.find_elements_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]')[1].click()



        # 删除
        sleep(1)
        self.driver.find_element_by_xpath('//table[@style="width: 53px;"]/tbody/tr/td[1]/div/label/span/input').click()
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[2]').click()
        self.driver.find_elements_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]')[1].click()
        sleep(1)
        try:
            loca1 = ("xpath", "//span[text()='删除成功']")
            WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(loca1))
            sleep(1)
            self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]').click()
            return True
        except:
            print("明细没有删除成功提示")
            sleep(2)
            self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]').click()
            return False

    '''标准化接口管理配置权重'''
    def  configuration_weight(self,name,code):
        self.logger.info("------------标准化接口管理配置权重----------")
        self.search_for_directory("标准化接口管理")
        self.click("xpath", "//div/ul[2]/li[contains(text(),'标准化接口管理')]")
        sleep(2)
        self.standardized_interface_select(name,code)
        sleep(2)
        self.driver.find_element_by_xpath('//div[@items="标准化接口管理"]/../div[3]/div/div/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/input').click()
        self.driver.find_element_by_xpath('//div[@items="标准化接口管理"]/../div[2]/div/*[9]').click()
        sleep(2)

        # 增加
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[1]').click()
        sleep(2)
        self.click("xpath","//div[text()='新增权重']/../../div[2]/form/div[1]/div/div/div[1]/div/input")
        sleep(0.5)
        self.driver.find_element_by_xpath('//label[text()="权重"]/../../div[1]/div/div/div[2]/ul[2]/li[1]').click()
        sleep(1)
        self.driver.find_elements_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]')[1].click()
        sleep(1)

        # 修改
        self.click("xpath","//div[text()='默认权重']/../../div[2]/div/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/input")
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[3]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//label[@style="width: 100px;"]/../div/div/div[1]/a[1]/span').click()
        self.driver.find_elements_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]')[1].click()
        sleep(1)

        # 删除
        self.click("xpath","//div[text()='默认权重']/../../div[2]/div/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/input")
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[2]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/div/*[1]/div[1]').click()
        sleep(1)
        try:
            loca1 = ("xpath", "//span[text()='删除成功']")
            WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(loca1))
            sleep(1)
            self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]').click()
            return True
        except:
            print("权重没有删除成功")
            sleep(2)
            self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]').click()
            return False

    '''商户调用策略管理增加'''
    def call_policyadd(self,num1,num2):
        self.logger.info("------------商户调用策略管理增加----------")
        self.search_for_directory("商户调用策略管理")
        self.click("xpath", "//div/ul[2]/li[contains(text(),'商户调用策略管理')]")
        sleep(3)
        self.driver.find_element_by_xpath("//div[@items='商户调用策略管理']/../div[2]/div/*[2]").click()
        sleep(1)
        self.click("xpath","//label[text()='商户代码']/../div/div/div[1]/div/input")
        self.driver.find_elements_by_xpath("//div[@style='margin-left: 80px;']/div/div[2]/ul[2]/li[%a]"%num1)[0].click()
        sleep(0.5)
        self.click("xpath","//label[text()='接口路由']/../div/div/div[1]/div/input")
        '''获取接口路由文本'''
        t=self.driver.find_element_by_xpath("//div[@class='ivu-modal-wrap']/*/*/*/*[text()='新增商户调用策略']/../../div[2]/form/div[2]/div/div/div[2]/ul[2]/li[%a]"%num2).text
        self.driver.find_element_by_xpath("//div[@class='ivu-modal-wrap']/*/*/*/*[text()='新增商户调用策略']/../../div[2]/form/div[2]/div/div/div[2]/ul[2]/li[%a]"%num2).click()
        sleep(0.5)
        self.driver.find_element_by_xpath("//div[@class='ivu-modal-wrap']/div/div/div[3]/*[2]").click()
        return t

    '''商户调用策略管理查询'''
    def call_policyselect(self,num1,name=""):
        sleep(1)
        self.driver.find_element_by_xpath("//div[@items='商户调用策略管理']/../div[2]/div/*[1]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//div[@style='margin-left: 80px;']/div/div[1]/div/input").click()
        self.driver.find_elements_by_xpath("//div[@style='margin-left: 80px;']/div/div[2]/ul[2]/li[%a]"%num1)[0].click()
        sleep(0.5)
        self.driver.find_element_by_xpath("//div[@class='ivu-modal-wrap']/div/div/div[2]/form/div[2]/div/div/input").send_keys(name)
        sleep(0.5)
        self.click("xpath","//div[@class='ivu-modal-wrap']/div/div/div[3]/*[2]")


    '''商户调用策略管理查询'''
    def is_dom_element_select_success(self, name):
        try:
            loca2 = ("xpath", "//tr/td[@class='ivu-table-column-center'][3]/div/span[text()='%s']" % name)
            sleep(1)
            WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(loca2))
            return True
        except:
            print("查询失败")
            return False

    '''商户调用策略管理删除'''
    def call_policydelete(self):
        self.logger.info("------------商户调用策略管理删除----------")
        sleep(1)
        self.driver.find_element_by_xpath("//div[@items='商户调用策略管理']/..//div[3]/div/div/div[4]/div[2]/table/tbody/tr/td/div/label/span/input").click()
        self.driver.find_element_by_xpath("//div[@items='商户调用策略管理']/../div[2]/div/*[3]").click()
        sleep(0.5)
        self.driver.find_element_by_xpath("//div[@class='ivu-modal-wrap']/div/div/div[3]/div/div/div[1]").click()

    '''商户调用策略管理商户路由'''
    def merchant_routing(self,num1,name):
        self.logger.info("------------商户调用策略管理商户路由----------")
        self.search_for_directory("商户调用策略管理")
        self.click("xpath", "//div/ul[2]/li[contains(text(),'商户调用策略管理')]")
        self.call_policyselect(num1,name)
        sleep(1)
        self.driver.find_element_by_xpath("//div[@items='商户调用策略管理']/..//div[3]/div/div/div[4]/div[2]/table/tbody/tr/td/div/label/span/input").click()
        self.driver.find_element_by_xpath("//div[@items='商户调用策略管理']/../div[2]/div/*[4]").click()
        sleep(2)
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[1]/button[1]').click()
        sleep(0.5)
        self.click("xpath","//div[@class='ivu-modal-wrap']/div[@style='width: 360px;']/div/div[2]/form/div[1]/div/div/div[1]/div/input")
        self.click("xpath","//div[@class='ivu-modal-wrap']/div[@style='width: 360px;']/div/div[2]/form/div[1]/div/div/div[2]/ul[2]/li[1]")

        # self.driver.find_elements_by_xpath("//div[@style='margin-left: 120px;']/div/div[1]/input[2]")[0].click()
        # self.driver.find_element_by_xpath("//div[@x-placement='bottom']/ul[2]/li[3]").click()
        self.driver.find_elements_by_xpath("//div[@class='ivu-modal-wrap']/div/div/div[3]/*[2]")[1].click()
        sleep(1)
        # 上移
        self.driver.find_element_by_xpath('//div[text()="商户路由"]/../../div[2]/div/div[1]/div[3]/div/div/div[2]/table/tbody/tr[1]/td[1]/div/label/span').click()
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[1]/button[4]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//div[3]/div/div/div[2]/table/tbody/tr[2]/td[1]/div/label/span/input').click()
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[1]/button[3]').click()
        sleep(1)

        # 删除
        self.driver.find_elements_by_xpath('//div[3]/div/div/div[2]/table/tbody/tr[2]/td[1]/div/label/span/input')[0].click()
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[1]/button[2]').click()
        self.driver.find_elements_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]')[1].click()
        sleep(1)
        try:
            loca1=("xpath","//span[text()='删除成功']")
            WebDriverWait(self.driver,self.timeout,3).until(EC.presence_of_element_located(loca1))
            self.driver.find_element_by_xpath('//div[text()="商户路由"]/../../div[2]/div/div[2]/div[2]/div/button').click()
            sleep(1)
            self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//div[@items="商户调用策略管理"]/../div[4]/div[2]/div/div/a/i').click()
            return True
        except:
            print("商户路由未删除成功")
            self.driver.find_element_by_xpath('//div[text()="商户路由"]/../../div[2]/div/div[2]/div[2]/div/button').click()
            sleep(1)
            self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]').click()
            sleep(1)
            self.driver.find_element_by_xpath('//div[@items="商户调用策略管理"]/../div[4]/div[2]/div/div/a/i').click()
            return False

    '''路由映射管理查看映射'''
    def routing_mappingselect(self,name1,name2):
        self.logger.info("------------路由映射管理查看映射----------")
        self.search_for_directory("路由映射管理")
        self.click("xpath", "//div/ul[2]/li[contains(text(),'路由映射管理')]")
        sleep(5)
        self.click("xpath","//div[@class='ivu-col ivu-col-span-24']/div[2]/ul[7]/li/span/i")
        self.click("xpath","//div[1]/div/div[4]/div[2]/table/tbody/tr[8]/td[1]/div/label/span/input")
        self.driver.find_element_by_xpath("//span[text()='查看映射']").click()
        sleep(2)
        self.driver.find_element_by_xpath("//div/div/div[2]/div/div[4]/div[2]/div/div/div[2]/div/div[1]/div/button[1]").click()
        sleep(2)
        self.click("xpath","//div[text()='新增路由映射明细']/../../div[2]/form/div[1]/div/div/div[1]/div/input")
        self.click("xpath","//div[text()='新增路由映射明细']/../../div[2]/form/div[1]/div/div/div[2]/ul[2]/li[1]")
        sleep(0.5)
        self.driver.find_elements_by_xpath("//input[@placeholder='请输入目标字段']")[0].send_keys(name1)
        self.sendkeys(name1,"xpath","//div[text()='新增路由映射明细']/../../div[2]/form/div[3]/div/div/input")
        self.click("xpath","//div[text()='新增路由映射明细']/../../div[2]/form/div[4]/div/div/div[1]/div/input")
        self.click("xpath","//div[text()='新增路由映射明细']/../../div[2]/form/div[4]/div/div/div[2]/ul[2]/li[1]")
        sleep(0.5)
        self.driver.find_elements_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]')[1].click()
        sleep(2)

        # 修改
        self.click("xpath","//div[4]/div[2]/div/div/div[2]/div/div[2]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span/input")
        self.click("xpath","//div/div/div[2]/div/div[4]/div[2]/div/div/div[2]/div/div[1]/div/button[3]")
        sleep(2)
        self.driver.find_elements_by_xpath("//input[@placeholder='请输入目标字段']")[1].clear()
        self.driver.find_elements_by_xpath("//input[@placeholder='请输入目标字段']")[1].send_keys(name2)
        self.driver.find_elements_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]')[1].click()
        sleep(2)

        # 删除
        self.click("xpath","//div[4]/div[2]/div/div/div[2]/div/div[2]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span/input")
        self.click("xpath","//div/div/div[2]/div/div[4]/div[2]/div/div/div[2]/div/div[1]/div/button[2]")
        self.driver.find_elements_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]')[1].click()


        sleep(1)
        try:
            loca1=("xpath","//span[text()='删除成功']")
            WebDriverWait(self.driver, self.timeout,self.t).until(EC.presence_of_element_located(loca1))
            self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]').click()
            self.click("xpath", "//div[@items='路由映射管理']/../div[4]/div[2]/div/div/a/i")
            return True
        except :
            print("没有删除成功")
            self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]').click()
            self.click("xpath", "//div[@items='路由映射管理']/../div[4]/div[2]/div/div/a/i")
            return False


    '''路由映射管理同步映射'''
    def routing_mapping_synchronous(self):
        self.logger.info("------------路由映射管理同步映射----------")
        self.search_for_directory("路由映射管理")
        self.click("xpath", "//div/ul[2]/li[contains(text(),'路由映射管理')]")
        sleep(4)
        self.click("xpath", "//div[@class='ivu-col ivu-col-span-24']/div[2]/ul[2]/li/span/i")
        self.click("xpath", "//div[1]/div/div[4]/div[2]/table/tbody/tr[3]/td[1]/div/label/span/input")
        self.click("xpath","//span[text()='同步映射']")

    '''断言：路由映射管理同步映射，映射成功'''
    def is_dom_element_routing_mapping(self):
        try:
            loca1 = ("xpath", "//span[text()='已映射，无需同步']")
            WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(loca1))
            return True
        except:
            return False

    '''商户调用策略管理商户权重'''
    def merchant_weight(self,num1,name):
        self.logger.info("------------商户调用策略管理商户权重----------")
        self.search_for_directory("商户调用策略管理")
        self.click("xpath", "//div/ul[2]/li[contains(text(),'商户调用策略管理')]")
        self.call_policyselect(num1,name)
        sleep(2)
        self.click("xpath","//div[@items='商户调用策略管理']/..//div[3]/div/div/div[4]/div[2]/table/tbody/tr/td/div/label/span/input")
        self.click("xpath","//div[@items='商户调用策略管理']/../div[2]/div/*[5]")

        # 增加
        sleep(1)
        self.click("xpath","//div[@class='ivu-modal-wrap']/div/div/div[2]/div/div[1]/div/*[1]")
        sleep(2)
        self.click("xpath","//div[text()='新增商户权重']/../../div[2]/form/div[1]/div/div/div[1]/div/input")
        sleep(0.5)
        self.driver.find_element_by_xpath('//div[text()="新增商户权重"]/../../div[2]/form/div[1]/div/div/div[2]/ul[2]/li[1]').click()
        sleep(1)
        self.driver.find_elements_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]')[1].click()
        sleep(1)

        # 修改
        self.click("xpath","//div[text()='商户权重']/../../div[2]/div/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/input")
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[3]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//div[text()="修改商户权重"]/../../div[2]/form/div[2]/div/div/div[1]/a[1]/span').click()
        self.driver.find_elements_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]')[1].click()
        sleep(1)

        # 删除
        self.click("xpath","//div[text()='商户权重']/../../div[2]/div/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/input")
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[2]/div/div[1]/div/*[2]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/div/*[1]/div[1]').click()
        try:
            loca1=("xpath","//span[text()='删除成功']")
            WebDriverWait(self.driver, self.timeout,self.t).until(EC.presence_of_element_located(loca1))
            sleep(1)
            self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]').click()
            self.click("xpath", "//div[@items='商户调用策略管理']/../div[5]/div[2]/div/div/a/i")
            return True
        except :
            print("没有删除成功")
            self.driver.find_element_by_xpath('//div[@class="ivu-modal-wrap"]/div/div/div[3]/*[2]').click()
            self.click("xpath", "//div[@items='商户调用策略管理']/../div[5]/div[2]/div/div/a/i")
            return False

    '''商户调用策略管理智慧路由配置'''
    def  merchant_smart_routing(self,num1,name):
        self.logger.info("------------商户调用策略管理智慧路由配置----------")
        self.search_for_directory("商户调用策略管理")
        self.click("xpath", "//div/ul[2]/li[contains(text(),'商户调用策略管理')]")
        self.call_policyselect(num1, name)
        sleep(2)
        self.click("xpath","//div[@items='商户调用策略管理']/..//div[3]/div/div/div[4]/div[2]/table/tbody/tr/td/div/label/span/input")
        self.click("xpath","//div[@items='商户调用策略管理']/../div[2]/div/*[6]")
        self.clear("xpath","//div[text()='智慧路由配置']/../../div[2]/form/div[2]/div/div/div[1]/div/input")
        self.sendkeys(250,"xpath","//div[text()='智慧路由配置']/../../div[2]/form/div[2]/div/div/div[1]/div/input")
        self.clear("xpath","//div[text()='智慧路由配置']/../../div[2]/form/div[3]/div/div/div[1]/div/input")
        self.sendkeys(66,"xpath","//div[text()='智慧路由配置']/../../div[2]/form/div[3]/div/div/div[1]/div/input")
        self.clear("xpath","//div[text()='智慧路由配置']/../../div[2]/form/div[4]/div/div/div[1]/div/input")
        self.sendkeys(77,"xpath","//div[text()='智慧路由配置']/../../div[2]/form/div[4]/div/div/div[1]/div/input")
        value=self.findElement("xpath","//div[text()='智慧路由配置']/../../div[2]/form/div[5]/div/div/div[1]/div/input").get_attribute("value")
        self.clear("xpath","//div[text()='智慧路由配置']/../../div[2]/form/div[5]/div/div/div[1]/div/input")
        print(type(value))
        if value=="1":
            self.sendkeys(11,"xpath","//div[text()='智慧路由配置']/../../div[2]/form/div[5]/div/div/div[1]/div/input")
        else:
            self.sendkeys(1,"xpath","//div[text()='智慧路由配置']/../../div[2]/form/div[5]/div/div/div[1]/div/input")
        self.click("xpath","//div[@class='ivu-modal-wrap']/div/div/div[3]/*[2]")

    '''商户调用策略管理当前路由查看'''
    def  merchant_current_route(self):
        self.logger.info("------------商户调用策略管理当前路由查看----------")
        sleep(2)
        self.click("xpath", "//div[@items='商户调用策略管理']/..//div[3]/div/div/div[4]/div[2]/table/tbody/tr/td/div/label/span/input")
        self.click("xpath", "//div[@items='商户调用策略管理']/../div[2]/div/*[7]")
        try:
            loca1=("xpath","//div[text()='当前路由查看']")
            WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(loca1))
            self.click("xpath","//div[@class='ivu-modal-wrap']/div/div/div[3]/*[2]")
            return True
        except:
            return False



# if __name__=="__main__":
    # driver = webdriver.Chrome()
    # driver=Org(driver)
    # driver.login("biqing","123123")
    # self.assertTrue(self.org.is_title("天翼征信业务管理"))
    #  self.assertTrue(self.org.is_text_in_element("欢迎使用天翼征信业务管理平台,虞霆,您好"))
    # r1=self.org.is_text_in_element("欢迎使用天翼征信业务管理平台,虞霆,您好")
    # print(r1)
    # loca1 = ("xpath", "//ul[@class='ivu-menu ivu-menu-dark ivu-menu-vertical']/li[3]/ul/li[2]")
    # r1 = driver.is_text_in_element("aa")
    # print(r1)