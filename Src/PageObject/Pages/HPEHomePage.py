import sys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Locator


class HPEHomePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.search_form_field = driver.find_element(By.XPATH, Locator.search_form_field)

    def fillSearchFormField(self, search_phrase):
        self.search_form_field.send_keys(search_phrase)

    def printResultsInConsole(self, search_phrase):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, Locator.search_form_field_results)))
        self.search_form_field_results = self.driver.find_elements(By.XPATH, Locator.search_form_field_results)

        results = [x for x in self.search_form_field_results]
        print("All results: "+str([x.text for x in results]))
        print("Num of results: "+str(len(results)))
        print("If all starts with \""+search_phrase+"\" :" + str(all([x.text.lower().startswith(search_phrase) for x in results])))