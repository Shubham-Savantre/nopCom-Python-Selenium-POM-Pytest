from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    email_field = (By.ID, "Email")
    password_field = (By.ID, "Password")
    login_btn = (By.XPATH, '//*[@id="main"]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button')

    def enter_email(self, email):
        self.send_keys(*self.email_field, email)

    def enter_password(self, password):
        self.send_keys(*self.password_field, password)

    def click_login(self):
        self.click(*self.login_btn)