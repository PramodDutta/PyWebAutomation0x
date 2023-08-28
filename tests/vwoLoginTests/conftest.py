import allure
import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os

load_dotenv()
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver

    # Get username and password from environment variables
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    base_url = os.getenv("BASE_URL")
    request.cls.username = username
    request.cls.password = password
    request.cls.base_url = base_url


    yield driver
    driver.quit()
