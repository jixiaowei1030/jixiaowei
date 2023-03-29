from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains
from demo.common.logger import Log

class Base():
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver
        self.timeout=10
        self.t=0.5
        self.logger=Log()
        # self.loggerger = loggerging.getloggerger('测试')
        # self.loggerger.setLevel(loggerging.DEBUG)
        # self.fh = loggerging.FileHandler('test.logger')
        # self.fh.setLevel(loggerging.DEBUG)
        # self.ch = loggerging.StreamHandler()
        # self.ch.setLevel(loggerging.DEBUG)
        # self.formatter = loggerging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # self.fh.setFormatter(self.formatter)
        # self.ch.setFormatter(self.formatter)
        # self.loggerger.addHandler(self.fh)
        # self.loggerger.addHandler(self.ch)
        # 这两行代码是为了避免日志输出重复问题
        # self.loggerger.removeHandler(self.ch)
        # self.loggerger.removeHandler(self.fh)

    def findElement(self,*locat):
        locat1=[*locat]
        '''查找元素，找到返回元素，找不到返回false'''
        try:
            ele = WebDriverWait(self.driver, self.timeout,self.t).until(lambda x: x.find_element(*locat))
            # print("正在通过%s定位元素>(%s)"%(locat1[0],locat1[1]))
            # self.loggerger.info("正在通过%s定位元素>(%s)" % (locat1[0], locat1[1]))
            return ele
        except:
            self.logger.info("正在通过%s定位元素>(%s)" % (locat1[0], locat1[1]))
            self.logger.info("没有找到元素")
            # print("没有找到元素")

    # def findElement(self,*locat):
    #     ele = WebDriverWait(self.driver, self.timeout,self.t).until(lambda x: x.find_element(*locat))
    #     return ele

    def findElements(self,*locat):
        locat1 = [*locat]
        '''查找元素，找到返回元素，找不到返回false'''
        try:
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locat))
            # print("正在通过%s定位元素>(%s)"%(locat1[0],locat1[1]))
            # self.loggerger.info("正在通过%s定位元素>(%s)" % (locat1[0], locat1[1]))
            return ele
        except:
            self.logger.info("正在通过%s定位元素>(%s)" % (locat1[0], locat1[1]))
            self.logger.info("没有找到元素")
            # print("没有找到元素")

    '''传值'''
    def sendkeys(self,text,*locat):
        ele=self.findElement(*locat)
        ele.send_keys(text)

    '''点击'''
    def click(self,*locat):
        ele=self.findElement(*locat)
        ele.click()

    def double_click(self, *locat):
        '''双击事件'''
        ele = self.findElement(*locat)
        ActionChains(self.driver).double_click(ele).perform()

    '''清除'''
    def clear(self,*locat):
        ele=self.findElement(*locat)
        ele.clear()



    '''一级菜单定位'''
    def first_level_menu_location(self,locat):
        self.click("xpath", "//ul[@class='ivu-menu ivu-menu-dark ivu-menu-vertical']/li[%s]" %locat)

    '''二级菜单定位'''
    def seconde_level_menu_location(self,locat1,locat2):
        sleep(3)
        self.click("xpath", "//ul[@class='ivu-menu ivu-menu-dark ivu-menu-vertical']/li[%s]/ul/li[%s]"%(locat1,locat2))

    '''页面搜索'''
    def search_for_directory(self, name=""):
        sleep(3)
        self.click("xpath", "//input[@placeholder='菜单搜索']")
        self.sendkeys(name, "xpath", "//input[@placeholder='菜单搜索']")


    '''断言:有信息成功的提示'''
    def is_dom_element(self,message):
        try:
            loca1 = ("xpath", "//span[text()='%s']"%message)
            WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(loca1))
            return True
        except:
            self.logger.info("没有%s提示"%message)
            return False

    # '''断言：路由策略信息管理查询，元素在当前界面上'''
    # def is_dom_element_select(self, name):
    #     try:
    #         loca2 = ("xpath", "//div[@items='%s']/../div[3]/div/div/div[2]/table/tbody/tr/td[3]/div/span" % name)
    #         WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(loca2))
    #         return True
    #     except:
    #         self.loggerger.info("查询失败")
    #         return False

    '''断言：路由策略信息管理查询，元素在当前界面上'''
    def is_dom_element_select(self, name):
        sleep(1)
        try:
            loca2 = ("xpath", "//span[text()='%s']" % name)
            WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(loca2))
            return True
        except:
            self.logger.info("查询失败")
            return False

# if __name__== "__main__":
#     driver=webdriver.Chrome()
#     driver.get("http://172.17.45.29:8030/index.html#/")
#     locat=Base(driver)



