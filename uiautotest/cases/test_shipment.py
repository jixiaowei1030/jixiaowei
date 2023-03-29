

import pytest
import os
import time

from uiautotest.pagetest.shipment import Shipment
from uiautotest.common.login import login
from selenium.webdriver.common.by import By

class Test_Shipment:

    '''
    shipment
    '''


    def test_AddShipment(self,browser,login):
        AddShipment = Shipment(browser)
        AddShipment.move_shipment()
        AddShipment.click_shipment()
        AddShipment.add_Shipment()
        AddShipment.input_content()
        result = AddShipment.is_element_exit(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[3]/div/div/div[1]/div/table/tbody/tr[1]/td[2]/div/span')
        assert result , "元素未找到"




