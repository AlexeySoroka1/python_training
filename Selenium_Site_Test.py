# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1920, 1080)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Menu List'])[1]/following::li[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Menu List'])[1]/following::a[3]").click()
        driver.find_element_by_id("user-message").click()
        driver.find_element_by_id("user-message").clear()
        driver.find_element_by_id("user-message").send_keys("Alex")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Enter message'])[1]/following::button[1]").click()
        driver.find_element_by_id("sum1").click()
        driver.find_element_by_id("sum1").clear()
        driver.find_element_by_id("sum1").send_keys("5")
        driver.find_element_by_id("sum2").click()
        driver.find_element_by_id("sum2").clear()
        driver.find_element_by_id("sum2").send_keys("7")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Enter b'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='File Download'])[2]/following::a[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Bootstrap List Box'])[2]/following::a[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | xpath=(.//*[normalize-space(text()) and normalize-space(.)='Pick List'])[1]/following::select[1] | label=Sophia]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Pick List'])[1]/following::option[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Pick List'])[1]/following::button[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [addSelection | xpath=(.//*[normalize-space(text()) and normalize-space(.)='Pick List'])[1]/following::select[1] | label=Alice]]
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Pick List'])[1]/following::option[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Pick List'])[1]/following::button[1]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
