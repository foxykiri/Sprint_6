from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import allure

class OrderPage(BasePage):

    @allure.step('Заполнение поля Имя')
    def send_name_to_field(self, text):
        self.send_keys_to_fields(OrderPageLocators.name_field, text)

    @allure.step('Filling in the "Surname" field')
    def send_surname_to_field(self, text):
        self.send_keys_to_fields(OrderPageLocators.last_name_field, text)

    @allure.step('send delivery address to delivery address field')
    def send_address_to_address_input(self, text):
        self.send_keys_to_fields(OrderPageLocators.address_field, text)

    @allure.step('Send subway station to subway station input field')
    def send_metro_to_subway_input(self, text):
        self.click_on_btn(OrderPageLocators.metro_station_field)
        self.send_keys_to_fields(OrderPageLocators.metro_station_field, text)
        self.click_on_btn(OrderPageLocators.metro)

    @allure.step('Send phone number to telephone input field')
    def send_phone_number_to_number_input_field(self, text):
        self.send_keys_to_fields(OrderPageLocators.telephone_field, text)

    @allure.step('Click on "Proceed" button in order form')
    def click_on_next_btn(self):
        self.click_on_btn(OrderPageLocators.next_btn)

    @allure.step('Completely fill first part of order form')
    def fill_order_form_for_who(self, first_user):
        self.send_name_to_field(first_user[1])
        self.send_surname_to_field(first_user[2])
        self.send_address_to_address_input(first_user[3])
        self.send_metro_to_subway_input(first_user[4])
        self.send_phone_number_to_number_input_field(first_user[5])
        self.click_on_next_btn()

    @allure.step('Send scooter delivery date to input field')
    def send_deliver_date_to_delivery_input(self, text):
        self.click_on_btn(OrderPageLocators.time_deliver_field)
        self.send_keys_to_fields(OrderPageLocators.time_deliver_field, text)

    @allure.step('Choose rent time')
    def rent_time_choose(self):
        self.click_on_btn(OrderPageLocators.rent_time_field)
        self.click_on_btn(OrderPageLocators.rent_period_three_days)

    @allure.step('Choose gray scooter colour')
    def scooter_colour_choose(self):
        self.click_on_btn(OrderPageLocators.gray_color_scooter_check)

    @allure.step('Send comment to comment input field')
    def send_comment_to_comment_input(self, text):
        self.send_keys_to_fields(OrderPageLocators.comment_field, text)

    @allure.step('Click on "Order" button to finish order process')
    def finish_order(self):
        self.click_on_btn(OrderPageLocators.order_btn)

    @allure.step('Completely fill second part of order form')
    def complete_filling_of_order_form(self, text):
        self.send_deliver_date_to_delivery_input(text[6])
        self.rent_time_choose()
        self.scooter_colour_choose()
        self.send_comment_to_comment_input(text[7])
        self.finish_order()

    @allure.step('Order confirmation')
    def confirm_order(self):
        self.click_on_btn(OrderPageLocators.yes_btn)

    @allure.step('Complete work-flow of an order')
    def full_flow_to_order(self, first_user):
        self.fill_order_form_for_who(first_user)
        self.complete_filling_of_order_form(first_user)
        self.confirm_order()

    @allure.step('Order checkout popup window')
    def order_completed_popup(self):
        return self.wait_about_element_located(OrderPageLocators.order_placed_text).is_displayed()