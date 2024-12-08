from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class RegistrationPage(BasePage):
    male_radio = (By.ID, "gender-male")
    female_radio = (By.ID, "gender-female")
    first_name = (By.ID, "FirstName")
    last_name = (By.ID, "LastName")
    date_DOB = (By.NAME, "DateOfBirthDay")
    month_DOB = (By.NAME, "DateOfBirthMonth")
    year_DOB = (By.NAME, "DateOfBirthYear")
    email_field = (By.ID, "Email")
    company_field = (By.ID, "Company")
    newsletter_check = (By.ID, "Newsletter")
    new_password = (By.ID, "Password")
    confirm_pass = (By.ID, "ConfirmPassword")
    register_btn = (By.ID, "register-button")
    continue_btn = (By.CLASS_NAME, "button-1 register-continue-button")

    def select_male(self):
        self.click(*self.male_radio)  # Unpack tuple

    def select_female(self):
        self.click(*self.female_radio)

    def enter_first_name(self, first_name):
        self.send_keys(*self.first_name, first_name)  # Unpack tuple

    def enter_last_name(self, last_name):
        self.send_keys(*self.last_name, last_name)

    def set_date_DOB(self, date_DOB):
        self.select_dropdown_element(*self.date_DOB, date_DOB)

    def set_month_DOB(self, month_DOB):
        self.select_dropdown_element(*self.month_DOB, month_DOB)

    def set_year_DOB(self, year_DOB):
        self.select_dropdown_element(*self.year_DOB, year_DOB)

    def enter_email(self, email):
        self.send_keys(*self.email_field, email)

    def enter_company(self, company_name):
        self.send_keys(*self.company_field, company_name)

    def unselect_newsletter(self):
        self.click(*self.newsletter_check)

    def set_new_password(self, new_password):
        self.send_keys(*self.new_password, new_password)

    def set_confirm_password(self, confirm_password):
        self.send_keys(*self.confirm_pass, confirm_password)

    def click_register(self):
        self.click(*self.register_btn)

    def click_continue(self):
        self.click(*self.continue_btn)
