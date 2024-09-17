from selenium.webdriver.common.by import By

class OrderPageLocators:
    name_field = (By.XPATH, "//input[@placeholder = '* Имя']") #поле ввода Имени
    last_name_field = (By.XPATH, "//input[@placeholder = '* Фамилия']") #поле ввода Фамилиии
    address_field = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']") #поле ввода Адреса
    metro_station_field = (By.XPATH, "//input[@placeholder = '* Станция метро']") #поле ввода Станции метро
    metro = (By.XPATH, ".//div[text() = 'Черкизовская']") #локатор выбраной станции
    telephone_field = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']") #поле ввода Телефона
    next_btn = (By.XPATH, "//button[text() = 'Далее']") #кнопка Далее

    time_deliver_field = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']") #поле ввода Даты доставки
    rent_time_field = (By.XPATH, ".//span[@class='Dropdown-arrow']") #выплывающий список срока аренды
    rent_period_three_days = (By.XPATH, ".//div[text() = 'трое суток']") #локатор с выбраным временем срока аренды
    black_color_scooter_check = (By.ID, 'black') #выбор цвета "чёрный жемчуг"
    gray_color_scooter_check = (By.ID, 'grey') #выбор цвета "серая безысходность"
    comment_field = (By.XPATH, ".//input[@placeholder= 'Комментарий для курьера']") #поле ввода Комментарий
    back_btn = (By.XPATH, ".//button[text() = 'Назад']") #кнопка Назад
    order_btn = (By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']") #кнопка Заказать


    no_btn = (By.XPATH, ".//button[text() = 'Нет']") #кнопка Нет
    yes_btn = (By.XPATH, ".//button[text() = 'Да']") #кнопка Да


    order_placed_text = (By.XPATH, ".//div[text() = 'Заказ оформлен']") #текст Заказ оформлен
    view_status_btn = (By.XPATH, ".//button[text() = 'Посмотреть статус']") #кнопка Посмотреть статус
