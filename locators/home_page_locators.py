from selenium.webdriver.common.by import By

class HomePageLocators:
    yandex_logo_btn = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    scooter_logo_btn = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    scooter_logo_txt = (By.CLASS_NAME, 'Header_Disclaimer__3VEni')
    accept_cookie_btn = (By.ID, 'rcc-confirm-button')  #
    order_btn_from_header = (By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']")
    order_btn_from_page = (By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']")
    question_li = (By.CSS_SELECTOR, '.accordion')  # Список FAQ

    questions = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7")
    ]

    answers = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7")
    ]
