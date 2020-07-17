import time
import random
from pathlib import Path
import sys
#-----------------------------------------
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class SupremeCheckOut():
##fsfsfsf
    def __init__(self,keys):
        self.keys = keys #dictionary with keys
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def fill_form(self):
        url = 'https://www.supremenewyork.com/checkout'
        self.driver.get(url)
        time.sleep(2)
        element = self.driver.find_element_by_id("nav-store").click()
        time.sleep(2)

    def closeBrowser(self):
        driver = self.driver.close()


keys = {
    'name':'name',
    'email':'email',
    'tel':'tel',
    'address':'address',
    'apt,unit,ect':'apt_num',
    'zip':'zip_code',
    'credit_card':'credit_car',
    'date_m':'date_m',
    'date_y':'date_y',
    'CVV':'cvv',
}

go = SupremeCheckOut(keys)
go.fill_form()
time.sleep(10)
go.closeBrowser()


if __name__ == "__main__":
    pass
