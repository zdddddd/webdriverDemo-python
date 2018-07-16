# coding:utf-8

import time,os
from selenium import webdriver
import unittest

class TestCase(unittest.TestCase):
    def case1(self):
        chromedriver = "C:\selenium\drivers\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver = webdriver.Chrome(chromedriver);
        driver.get("http://www.baidu.com")
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()
        time.sleep(5)
        driver.quit()


