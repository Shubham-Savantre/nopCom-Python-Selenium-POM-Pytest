from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def click(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def send_keys(self, by, value, text):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def select_dropdown_element(self, by, value, DOB):
        element = self.find_element(by, value)
        select = Select(element)
        select.select_by_visible_text(DOB)

    def wait_for_element(self, by, value):
        self.wait.until(EC.presence_of_element_located((by, value)))

    def is_element_present(self, by, value):
        try:
            self.find_element(by, value)
            return True
        except:
            return False