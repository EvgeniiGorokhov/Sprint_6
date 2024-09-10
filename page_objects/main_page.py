from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage
import allure



class MainPage(BasePage):


    @allure.step('Ждем загрузки части лого "Яндекса"')
    def waiting_for_download_part_of_the_Yandex_logo(self):
        self.wait_visibility_of_element(MainPageLocators.LOGO_YANDEX)

    @allure.step('Ждем загрузки части лого "Самокат"')
    def waiting_for_download_parts_of_scooter_logo(self):
        self.wait_visibility_of_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step('Клик по части лого "Яндекса"')
    def click_on_part_of_the_Yandex_logo(self):
        self.click_on_element(MainPageLocators.LOGO_YANDEX)

    @allure.step('Клик по части лого "Самокат"')
    def click_on_parts_of_the_logo_scooter(self):
        self.click_on_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step('Подождать прогрузки отображения заголовка главной страницы')
    def wait_visibility_of_main_header(self):
        self.wait_visibility_of_element(MainPageLocators.MAIN_HEADER)

    @allure.step('Проверить отображение заголовка главной страницы')
    def check_displaying_of_main_header(self):
        return self.check_displaying_of_element(MainPageLocators.MAIN_HEADER)

    @allure.step('Проскроллить до секции "Вопросы о важном"')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.FAQ_SECTION)

    @allure.step('Подождать прогрузки нужного номера вопроса в аккордеоне "Вопросы о важнoм"')
    def wait_visibility_of_faq_items(self, data):
        self.wait_visibility_of_element(MainPageLocators.FAQ_QUESTIONS_ITEMS[data])

    @allure.step('Кликнуть на нужный номер вопроса в аккордеоне "Вопросы о важнoм"')
    def click_on_faq_items(self, data):
        self.click_on_element(MainPageLocators.FAQ_QUESTIONS_ITEMS[data])

    @allure.step('Подождать прогрузки нужного номера ответа в аккордеоне "Вопросы о важнoм"')
    def wait_visibility_of_faq_answer(self, data):
        self.wait_visibility_of_element(MainPageLocators.FAQ_ANSWERS_BY_ITEM[data])

    @allure.step('Получить текст нужного номера ответа в аккордеоне "Вопросы о важнoм"')
    def get_displayed_text_from_faq_answer(self, data):
        return self.get_text_on_element(MainPageLocators.FAQ_ANSWERS_BY_ITEM[data])




