import sys

sys.path.append(sys.path[0] + "/...")

from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.BasicFirstFormPage import BasicFirstFormPage
from Src.PageObject.Pages.HPEHomePage import HPEHomePage
import unittest


class EasySelenium_Forms(WebDriverSetup):

    def test_SearchFieldResults(self):
        driver = self.driver
        driver.get("https://www.hpe.com/us/en/home.html")
        driver.set_page_load_timeout(5)
        hpehomepage = HPEHomePage(driver)
        hpehomepage.fillSearchFormField("nimble")
        hpehomepage.printResultsInConsole("nimble")


if __name__ == '__main__':
    unittest.main()
