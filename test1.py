from selenium import webdriver
from time import sleep

import unittest
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://managetest.tycredit.com/index.html#/")

    def test_01(self):
        self.driver.find_element_by_class_name("ivu-input").send_keys("yuting")
        self.driver.find_elements_by_class_name("ivu-input")[1].send_keys("Yting123!!!#")
        self.driver.find_elements_by_class_name("ivu-input")[2].send_keys("123456")
        self.driver.find_element_by_css_selector("button.submit_btn.ivu-btn.ivu-btn-primary").click()
        sleep(2)
        t=self.driver.find_element_by_xpath("//ul[@class='ivu-menu ivu-menu-dark ivu-menu-vertical']/li[3]").text
        print(t)
        self.driver.find_elements_by_xpath("//input[@placeholder='菜单搜索']")
        js = "window.scrollTo(document.body.scrollWidth,document.body.scrollHeight)"
        self.driver.execute_script(js)

if __name__=="__main__":
    unittest.main()
