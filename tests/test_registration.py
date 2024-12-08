import pytest
from utils.driver_factory import create_driver
from pages.registeration_page import RegistrationPage


class TestRegistration:

    @pytest.fixture(scope="function")
    def setup(self):
        driver = create_driver()
        driver.get("https://demo.nopcommerce.com/register")
        yield driver
        driver.quit()

    def test_registration_valid(self, setup):
        reg_page = RegistrationPage(setup)  # Pass the driver correctly
        reg_page.enter_first_name("abc")
        reg_page.enter_last_name("abc")
        reg_page.set_date_DOB("10")
        reg_page.set_month_DOB("May")
        reg_page.set_year_DOB("1990")
        reg_page.enter_email("abc@abc.com")
        reg_page.enter_company("abc")
        reg_page.unselect_newsletter()
        reg_page.set_new_password("abc123@")
        reg_page.set_confirm_password("abc123@")
        reg_page.click_register()

        # Assert the URL to confirm registration success
        assert setup.current_url == "https://demo.nopcommerce.com/", "Registration failed"
