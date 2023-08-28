import time
import pytest
import selenium
from selenium import webdriver
from tests.pageObjects.loginPagePF import LoginPage
import allure
from allure_commons.types import AttachmentType
from dotenv import load_dotenv

@allure.epic("VWO App")
@allure.feature("Login Test")
class TestVWOLogin:
    load_dotenv()
    @pytest.mark.usefixtures("setup")
    def test_vwologin_negative(self, setup):
        driver = setup
        driver.get(self.base_url)
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user=self.username, pwd="123")
        time.sleep(5)
        if "Dashboard2" not in driver.title:
            allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScreen", attachment_type=AttachmentType.PNG)
        assert "Dashboard2" in driver.title
        time.sleep(2)

    @pytest.mark.usefixtures("setup")
    def test_vwologin_pf(self,setup):
        driver = setup
        driver.get(self.base_url)
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user=self.username, pwd=self.password)
        time.sleep(5)
        assert "Dashboard" in driver.title
        time.sleep(2)

