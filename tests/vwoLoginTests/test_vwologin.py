import time
import pytest
import selenium
from selenium import webdriver
from tests.pageObjects.loginPage import LoginPage


class TestVWOLogin:

    @pytest.fixture()
    def driver(self):
        driver = webdriver.Chrome()
        driver.get("https://app.vwo.com")
        driver.maximize_window()
        yield driver
        driver.quit()

    @pytest.mark.positive
    def test_vwologin(self, driver):
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo("contact+augg@thetestingacademy.com", "Wingify@123")
        time.sleep(5)
        assert "Dashboard" in driver.title
        time.sleep(2)
