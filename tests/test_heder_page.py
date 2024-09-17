from helps.data import Urls, QuestionsList
from locators.home_page_locators import HomePageLocators
from locators.dzen_locators import DzenLocators
from pages.home_page import HomePage
from pages.dzen_page import DzenPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure
import pytest

class TestMainPage:
    @allure.title('Test "Click on Scooter logo lead to Scooter main page"')
    @allure.description('''1)Click on "Order" button
                        2)Click on "Scooter" logo
                        3)Compare the expected and current URLs and confirm that the text "Training Simulator" appears''')
    def test_click_on_scooter_logo(self, driver):
        main_page = HomePage(driver)
        main_page.click_order_btn()
        main_page.click_scooter_logo()
        current_url = main_page.get_current_url()
        title_displayed = main_page.check_main_title()
        assert current_url == Urls.BASE_SCOOTER_URL and title_displayed

    @allure.title('Test "Click on Yandex logo lead to Yandex Dzen main page"')
    @allure.description('''1)Click on "Yandex" logo
                            2)Switch to new browser tab
                            3)Comparing expected and current URL's and confirm "Main" button appears''')
    def test_click_on_yandex_logo(self, driver):
        main_page = HomePage(driver)
        dzen_page = DzenPage(driver)
        main_page.click_yandex_logo()
        main_page.switch_to_the_new_tab()
        dzen_page.wait_about_element_located(DzenLocators.dzen_find_btn)
        current_url = main_page.get_current_url()
        assert current_url == Urls.DZEN_URL and dzen_page.check_element_main_btn

    @allure.title('Test "Answers to FAQ compares to expected answers text"')
    @allure.description('''1)Scroll to FAQ;
                            2)Click on question;
                            3)Get the text of the answers;
                            4)Comparing expected and actual text''')
    @pytest.mark.parametrize('questions, answers, expected_question_text',
                             zip(HomePageLocators.questions, HomePageLocators.answers,
                                 QuestionsList.expected_question_text))
    def test_questions_accordeon(self, driver, questions, answers,
                                 expected_question_text):
        main_page = HomePage(driver)
        main_page.accept_cookie()
        main_page.scroll_to_questions()
        text = main_page.get_text_of_questions(questions,answers)
        assert text == expected_question_text