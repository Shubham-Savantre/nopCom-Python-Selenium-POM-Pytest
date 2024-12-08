import pytest

from pages.login_page import LoginPage
from utils.driver_factory import create_driver


class TestLogin:
    @pytest.fixture(scope="function")
    def setup(self):
        driver = create_driver()
        driver.get("https://demo.nopcommerce.com/login")
        yield driver
        driver.quit()

    def test_login_valid(self,setup):
        log_page = LoginPage(setup)
        setup.implicitly_wait(2)
        log_page.enter_email("abc@abc.com")
        setup.implicitly_wait(2)
        log_page.enter_password("abc123@")
        setup.implicitly_wait(2)

        log_page.click_login()
        setup.implicitly_wait(5)
        setup.save_screenshot("before_login_test.png")


        assert setup.current_url=="https://demo.nopcommerce.com/"
