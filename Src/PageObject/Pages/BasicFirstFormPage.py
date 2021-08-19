import sys

sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Locator


class BasicFirstFormPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.display_message_input = driver.find_element(By.XPATH, Locator.user_message)
        self.submit_display = driver.find_element(By.XPATH, Locator.get_input_button)
        self.display_result = driver.find_element(By.XPATH, Locator.display)
        self.field_a = driver.find_element(By.XPATH, Locator.sum1)
        self.field_b = driver.find_element(By.XPATH, Locator.sum2)
        self.submit_total = driver.find_element(By.XPATH, Locator.gettotal_button)
        self.field_sum = driver.find_element(By.XPATH, Locator.displayvalue)

    def submitDisplayMessage(self):
        self.submit_display.click()

    def getDisplayResult(self):
        return self.display_result.text

    def fillDisplayMessageInput(self, message):
        self.display_message_input.send_keys(message)

    def fillFieldA(self, message):
        self.field_a.send_keys(message)

    def fillFieldB(self, message):
        self.field_b.send_keys(message)

    def submitSumOfFieldAAndFieldB(self):
        self.submit_total.click()

    def getSumResult(self):
        return self.field_sum.text