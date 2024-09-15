from locators.dzen_locators import DzenLocators
from pages.base_page import BasePage
import allure

class DzenPage(BasePage):
    @allure.step("Check for ""Main"" button being displayed at Yandex. Dzen")
    def check_element_main_btn(self):
        self.wait_about_element_located(DzenLocators.dzen_main_page_btn)
        self.check_element_displayed(DzenLocators.dzen_main_page_btn)