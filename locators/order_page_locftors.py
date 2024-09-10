from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Для кого самокат
    FIELDS_NAME = By.XPATH, "//input[@placeholder='* Имя']"
    FIELDS_SURNAME = By.XPATH, "//input[@placeholder='* Фамилия']"
    FIELDS_ADDRESS = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_STATION = By.XPATH, "//input[@placeholder='* Станция метро']"
    SELECT_ITEM_IN_DROPDOWN_METRO = By.XPATH, ".//li[@class='select-search__row']"
    FIELD_PHONE = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    BUTTON_NEXT = By.XPATH, "//button[text()='Далее']"

    # Про аренду
    FIELDS_DATE = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    CALENDAR = By.XPATH, "//div[@class='react-datepicker-popper']"
    CALENDAR_ITEM = By.XPATH, "//div[contains(@class, 'react-datepicker') and contains(@tabindex, '0')]"
    RENTAL_TERM = By.XPATH, ".//div[text()='* Срок аренды']"
    DROPDOWN_ITEM_RENTAL_PERIOD = By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='трое суток']"
    COLOR_SAMOKATO = By.XPATH, "//input[@id='black']"
    COMMENT = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    BUTTON_ORDER = By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']"

    # Подтверждение заказа
    YES_PLACE_ORDER = By.XPATH, "//button[text()='Да']"
    BUTTON_VIEW_STATUS = By.XPATH, ".//*[text()='Посмотреть статус']"


