from selenium.webdriver.common.by import By
from selenium import webdriver


class FormPage():

    def __init__(self, driver):
        self.driver = driver

        self.firstName_Id = "first-name"
        self.lastName_Id = "last-name"
        self.jobTitle_Id = "job-title"
        self.education_highSchool_Id = "radio-button-1"
        self.education_college_Id = "radio-button-2"
        self.education_graduate_Id = "radio-button-3"
        self.gender_male_Id = "checkbox-1"
        self.gender_female_Id = "checkbox-2"
        self.gender_hidden_Id = "checkbox-3"
        self.experience_level1_cssSelector = "option[value='1']"
        self.experience_level2_cssSelector = "option[value='2']"
        self.experience_level3_cssSelector = "option[value='3']"
        self.experience_level4_cssSelector = "option[value='4']"
        self.date_Id = "datepicker"
        self.submit_cssSelector = ".btn.btn-lg.btn-primary"

    def enter_firstName(self, firstname):
        self.driver.find_element(By.ID, self.firstName_Id).send_keys(firstname)

    def enter_lastName(self, lastname):
        self.driver.find_element(By.ID, self.lastName_Id).send_keys(lastname)

    def enter_jobTitle(self, title):
        self.driver.find_element(By.ID, self.jobTitle_Id).send_keys(title)

    def enter_education(self, education):
        if education.lower() == "high school":
            self.driver.find_element(By.ID, self.education_highSchool_Id).click()
        elif education.lower() == "college":
            self.driver.find_element(By.ID, self.education_college_Id).click()
        else:
            self.driver.find_element(By.ID, self.education_graduate_Id).click()

    def enter_gender(self, gender):
        if gender.lower() == "male":
            self.driver.find_element(By.ID, self.gender_male_Id).click()
        elif gender.lower() == "female":
            self.driver.find_element(By.ID, self.gender_female_Id).click()
        else:
            self.driver.find_element(By.ID, self.gender_hidden_Id).click()

    def enter_experience(self, experience):
        if int(experience) < 2:
            self.driver.find_element(By.CSS_SELECTOR, self.experience_level1_cssSelector).click()
        elif int(experience) < 5:
            self.driver.find_element(By.CSS_SELECTOR, self.experience_level2_cssSelector).click()
        elif int(experience) < 10:
            self.driver.find_element(By.CSS_SELECTOR, self.experience_level3_cssSelector).click()
        else:
            self.driver.find_element(By.CSS_SELECTOR, self.experience_level4_cssSelector).click()

    def enter_date(self, date):
        self.driver.find_element(By.ID, self.date_Id).send_keys(date)

    def click_submit_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.submit_cssSelector).click()

    def new_form(self):
        self.driver.find_element(By.LINK_TEXT, "Form").click()
