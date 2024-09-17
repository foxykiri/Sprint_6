from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
import allure

class HomePage(BasePage):
    @allure.step('Click on Yandex logo')
    def click_yandex_logo(self):
        self.click_on_btn(HomePageLocators.yandex_logo_btn)

    @allure.step('Click on Scooter logo')
    def click_scooter_logo(self):
        self.click_on_btn(HomePageLocators.scooter_logo_btn)

    @allure.step('Click on "Order" header button')
    def click_order_btn(self):
        self.click_on_btn(HomePageLocators.order_btn_from_header)

    @allure.step('Check for "Training simulator" text on header')
    def check_main_title(self):
        return self.wait_about_element_located(HomePageLocators.scooter_logo_txt).is_displayed()

    @allure.step('Click on "Accept cookies" button')
    def accept_cookie(self):
        self.wait_about_element_located(HomePageLocators.accept_cookie_btn)
        self.click_on_btn(HomePageLocators.accept_cookie_btn)

    @allure.step('Click "Order" button from page')
    def order_from_another_btn(self):
        self.scroll_to_locator(HomePageLocators.order_btn_from_page)
        self.check_element_displayed(HomePageLocators.order_btn_from_page)
        self.click_on_btn(HomePageLocators.order_btn_from_page)

    @allure.step('Scroll to FAQ list')
    def scroll_to_questions(self):
        self.scroll_to_locator(HomePageLocators.question_li)

    @allure.step('Click on questions from FAQ list')
    def click_on_questions(self, question_buts_locators):
        self.wait_about_element_located(question_buts_locators)
        self.click_on_btn(question_buts_locators)

    @allure.step('Get answers text from FAQ list')
    def get_text_of_questions(self, questions,answers):
        self.click_on_questions(questions)
        self.check_element_displayed(answers)
        text_of_questions = self.get_text_from_locator(answers)
        return text_of_questions

