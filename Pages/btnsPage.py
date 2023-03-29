from selenium.webdriver.common.by import By
from selenium import webdriver


class ButtonPage():

    def __init__(self, driver):
        self.driver = driver

        self.primary_btn_cssSelector = ".btn.btn-lg.btn-primary"
        self.success_btn_cssSelector = ".btn.btn-lg.btn-success"
        self.info_btn_cssSelector = ".btn.btn-lg.btn-info"
        self.warning_btn_cssSelector = ".btn.btn-lg.btn-warning"
        self.danger_btn_cssSelector = ".btn.btn-lg.btn-danger"
        self.link_btn_cssSelector = ".btn.btn-lg.btn-link"
        self.left_btn_xPath = "/html/body/div/form/div[2]/div/div/div/button[1]"
        self.middle_btn_xPath = "/html/body/div/form/div[2]/div/div/div/button[2]"
        self.right_btn_xPath = "	/html/body/div/form/div[2]/div/div/div/button[3]"
        self.first_btn_xPath = "/html/body/div/form/div[3]/div/div/div/button[1]"
        self.second_btn_xPath = "/html/body/div/form/div[3]/div/div/div/button[2]"
        self.dropDown_btn_Id = "btnGroupDrop1"
        self.dropDown_link_linkTxt = "Dropdown link 1"

    def click_primary(self):
        self.driver.find_element(By.CSS_SELECTOR, self.primary_btn_cssSelector).click()

    def click_success(self):
        self.driver.find_element(By.CSS_SELECTOR, self.success_btn_cssSelector).click()

    def click_info(self):
        self.driver.find_element(By.CSS_SELECTOR, self.info_btn_cssSelector).click()

    def click_warning(self):
        self.driver.find_element(By.CSS_SELECTOR, self.warning_btn_cssSelector).click()

    def click_danger(self):
        self.driver.find_element(By.CSS_SELECTOR, self.danger_btn_cssSelector).click()

    def click_link(self):
        self.driver.find_element(By.CSS_SELECTOR, self.link_btn_cssSelector).click()

    def click_left(self):
        self.driver.find_element(By.XPATH, self.left_btn_xPath).click()

    def click_middle(self):
        self.driver.find_element(By.XPATH, self.middle_btn_xPath).click()

    def click_right(self):
        self.driver.find_element(By.XPATH, self.right_btn_xPath).click()

    def click_first(self):
        self.driver.find_element(By.XPATH, self.first_btn_xPath).click()

    def click_second(self):
        self.driver.find_element(By.XPATH, self.second_btn_xPath).click()

    def click_dropdown(self):
        self.driver.find_element(By.ID, self.dropDown_btn_Id).click()

    def click_link1(self):
        self.driver.find_element(By.LINK_TEXT, self.dropDown_link_linkTxt).click()


