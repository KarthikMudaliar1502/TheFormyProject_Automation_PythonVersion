import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from SeleniumTest_python_version.Pages.formPage import FormPage
import xlrd


class FormFeed(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.maximize_window()

    def test_FillForm(self):
        driver = self.driver
        driver.get("https://formy-project.herokuapp.com/form")

        form = FormPage(driver)
        workbook = xlrd.open_workbook("../Pages/data.xlsx")
        sheet = workbook.sheet_by_name("Sheet1")
        rowcount = sheet.nrows

        for curr_row in range(1, rowcount):
            first_name = sheet.cell_value(curr_row, 0)
            last_name = sheet.cell_value(curr_row, 1)
            job_title = sheet.cell_value(curr_row, 2)
            education = sheet.cell_value(curr_row, 3)
            gender = sheet.cell_value(curr_row, 4)
            experience = sheet.cell_value(curr_row, 5)
            date = sheet.cell_value(curr_row, 6)

            form.enter_firstName(first_name)
            form.enter_lastName(last_name)
            form.enter_jobTitle(job_title)
            form.enter_education(education)
            form.enter_gender(gender)
            form.enter_experience(experience)
            form.enter_date(date)
            form.click_submit_button()
            time.sleep(1)
            form.new_form()
            time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()