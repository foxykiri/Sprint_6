from selenium.webdriver.common.by import By

class DzenLocators:
    dzen_find_btn = (By.XPATH, './/button[@type="submit" and text() = "Найти"]')