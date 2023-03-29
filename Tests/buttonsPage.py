from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import unittest
from SeleniumTest_python_version.Pages.btnsPage import ButtonPage


class BtnPage(unittest.TestCase):

    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.maximize_window()

    def test_buttons_page(self):
        driver = self.driver
        driver.get("https://formy-project.herokuapp.com/buttons")

        buttons = ButtonPage(driver)

        buttons.click_primary()
        buttons.click_success()
        buttons.click_info()
        buttons.click_warning()
        buttons.click_danger()
        buttons.click_link()
        buttons.click_left()
        buttons.click_middle()
        buttons.click_right()
        buttons.click_first()
        buttons.click_second()
        buttons.click_dropdown()
        buttons.click_link1()

        # time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()
