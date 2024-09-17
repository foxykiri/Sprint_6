import allure
import pytest
from  selenium import webdriver
from helps.data import Urls

@allure.step('Open browser / Go to Yandex. Scooter / Close browser')
@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.BASE_SCOOTER_URL)
    yield driver
    driver.quit()