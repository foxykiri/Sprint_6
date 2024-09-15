from imghdr import tests

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def wait_about_element_located(self,locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))

    def get_text_from_locator(self,locator):
        return self.wait_about_element_located(locator).text

    def check_element_displayed(self, locator):
        return self.wait_about_element_located(locator).is_displayed()

    def check_element_click(self,locator):
        return WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(locator))

    def click_on_btn(self,locator):
        self.check_element_click(locator)
        self.wait_about_element_located(locator).click()

    def send_keys_to_fields(self,locator,text):
        self.wait_about_element_located(locator).send_keys(text)

    def scroll_to_locator(self, locator):
        element = self.wait_about_element_located(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_the_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])