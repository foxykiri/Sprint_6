from pages.home_page import HomePage
from pages.order_page import OrderPage
from helps.data import Users
import allure

class TestOrderPage:
    @allure.title('Test "Order by header button"')
    @allure.description('''1)Clicking on header "Order" button;
                        2)Filling first part of an order form;
                        3)Filling second part of an order form;
                        4)Confirming order;
                        5)Waiting for order confirmation popup being displayed''')
    def test_order_by_header_btn(self, driver):
        main_page = HomePage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookie()
        main_page.click_order_btn()
        order_page.full_flow_to_order(Users.first_user)
        assert order_page.order_completed_popup()

    @allure.title('Test "Order by page button"')
    @allure.description('''1)Clicking on page "Order" button;
                           2)Filling first part of an order form;
                           3)Filling second part of an order form;
                           4)Confirming order;
                           5)Waiting for order confirmation popup being displayed''')
    def test_order_by_page_btn(self,driver):
        main_page = HomePage(driver)
        order_page = OrderPage(driver)
        main_page.accept_cookie()
        main_page.order_from_another_btn()
        order_page.full_flow_to_order(Users.second_user)
        assert order_page.order_completed_popup()