# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class InputForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.set_window_size(1920, 1080)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_input_form(self):
        driver = self.driver
        self.open_input_page(driver)
        self.fill_first_name(driver, user_name="AlexTest")
        self.fill_last_name(driver, user_last_name="Soroka")
        self.fill_email(driver, user_email="Test@gmail.com")
        self.fill_phoneNumber(driver, user_phone_number="(123)123-3333")
        self.fill_address(driver)
        self.fill_city(driver)
        self.chosse_state(driver)
        self.fill_zipCode(driver)
        self.fill_website(driver)
        self.choose_hosting(driver)
        self.click_on_send_button(driver)

    def click_on_send_button(self, driver):
        driver.find_element_by_xpath("//form[@id='contact_form']/fieldset/div[13]/div/button/span").click()

    def choose_hosting(self, driver):
        driver.find_element_by_xpath("(//input[@name='hosting'])[2]").click()
        driver.find_element_by_name("comment").click()
        driver.find_element_by_name("comment").clear()
        driver.find_element_by_name("comment").send_keys("Selenium test project")

    def fill_website(self, driver):
        driver.find_element_by_name("website").click()
        driver.find_element_by_name("website").clear()
        driver.find_element_by_name("website").send_keys("www.test.com")

    def fill_zipCode(self, driver):
        driver.find_element_by_name("zip").click()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Input form with validations'])[1]/following::fieldset[1]").click()
        driver.find_element_by_name("zip").clear()
        driver.find_element_by_name("zip").send_keys("6789")

    def chosse_state(self, driver):
        driver.find_element_by_name("state").click()
        Select(driver.find_element_by_name("state")).select_by_visible_text("New York")
        driver.find_element_by_name("state").click()

    def fill_city(self, driver):
        driver.find_element_by_name("city").click()
        driver.find_element_by_name("city").clear()
        driver.find_element_by_name("city").send_keys("New York")

    def fill_address(self, driver):
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").send_keys("USA")

    def fill_phoneNumber(self, driver, user_phone_number):
        driver.find_element_by_name("phone").click()
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys("%s" % user_phone_number)

    def fill_email(self, driver, user_email):
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("%s" % user_email)

    def fill_last_name(self, driver, user_last_name):
        driver.find_element_by_name("last_name").click()
        driver.find_element_by_name("last_name").clear()
        driver.find_element_by_name("last_name").send_keys("%s" % user_last_name)

    def fill_first_name(self, driver, user_name):
        driver.find_element_by_name("first_name").click()
        driver.find_element_by_name("first_name").clear()
        driver.find_element_by_name("first_name").send_keys("%s" % user_name)

    def open_input_page(self, driver):
        driver.get("https://www.seleniumeasy.com/test/input-form-demo.html")
        # fill first name

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
