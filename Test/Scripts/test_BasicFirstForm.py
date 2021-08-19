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

        searched_phrase = "nimble"
        hpehomepage.fillSearchFormField(searched_phrase)
        number_of_results, does_all_starts_with_phrase = hpehomepage.printResultsInConsole(searched_phrase)
        assert number_of_results == 4
        assert does_all_starts_with_phrase

    def test_SearchFieldResults_flashcase(self):
        driver = self.driver
        driver.get("https://www.hpe.com/us/en/home.html")
        driver.set_page_load_timeout(5)
        hpehomepage = HPEHomePage(driver)

        searched_phrase = "flash"
        hpehomepage.fillSearchFormField(searched_phrase)
        number_of_results, does_all_starts_with_phrase = hpehomepage.printResultsInConsole(searched_phrase)
        assert number_of_results == 3
        assert does_all_starts_with_phrase


if __name__ == '__main__':
    unittest.main()
