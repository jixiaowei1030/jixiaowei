

import pytest
import os
import time

from uiautotest.pagetest.addshipment import add_shipment
from uiautotest.common.login import login
from selenium.webdriver.common.by import By

class Testadd:

    def test_SaveShipment(self,browser):
        test = login(browser)
        test.login()
        test1 = add_shipment(browser)
        test1.add_shipment()
        element = test.isexit(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[3]/div/div/div[1]/div/table/tbody/tr[1]/td[2]/div/span')
        assert element , "元素未找到"



# if __name__ == "__main__":
#     pytest.main(["-v", "--html=report.html", "--alluredir=allure-report"])
#     os.system("allure serve allure-report")

