import time

import pytest

from tests.pageObjects.loginPage import LoginPage


# 100 of Test cases - I have to type the 100 Times the Driver code ?

# sample_conftest.py -> You can call the all important functions which are common
# and you want them to execute before class execution / module ?



# qa -
# preprod


import allure
@allure.epic("VWO App Positive ")
@allure.feature("Login Positive Test")
class TestVWOLogin:

    @pytest.mark.usefixtures("setup")
    @pytest.mark.qa
    def test_vwologin(self, setup):
        driver = setup
        driver.get(self.base_url)
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user=self.username, pwd=self.password)
        time.sleep(5)
        assert "Dashboard" in driver.title
        time.sleep(2)
