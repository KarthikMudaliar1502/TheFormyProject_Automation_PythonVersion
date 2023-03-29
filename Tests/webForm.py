import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from SeleniumTest_python_version.Pages.formPage import FormPage


class WebForm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.maximize_window()

    def test_WebForm(self):
        driver = self.driver
        driver.get("https://formy-project.herokuapp.com/form")

        form = FormPage(driver)

        form.enter_firstName("Amitabh")
        form.enter_lastName("Bachchan")
        form.enter_jobTitle("Scientist")
        form.enter_education("High School")
        form.enter_gender("Male")
        form.enter_experience(2)
        form.enter_date("02/07/2022")
        form.click_submit_button()
        form.new_form()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()