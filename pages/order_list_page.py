
import allure
from selenium.webdriver.common.by import By

from locators.order_list_page_locators import OrderListPageLocators
from pages.base_page import BasePage


class OrderListPage(BasePage):
    @allure.title('Авторизация')
    def login(self, email, password):
        self.wait_visibility_of_element(OrderListPageLocators.LOGIN_INTO_ACCOUNT_BUTTON)
        self.click_on_element(OrderListPageLocators.LOGIN_INTO_ACCOUNT_BUTTON)
        self.set_text_in_element(OrderListPageLocators.EMAIL_FIELD, email)
        self.set_text_in_element(OrderListPageLocators.PASSWORD_FIELD, password)
        self.click_on_element(OrderListPageLocators.LOGIN_BUTTON)
        self.wait_visibility_of_element(OrderListPageLocators.MAKE_ORDER_BUTTON)

    @allure.title('Переход в раздел Лента заказов')
    def navigation_to_order_list(self):
        self.click_on_element(OrderListPageLocators.ORDER_LIST_BUTTON)
        self.wait_visibility_of_element(OrderListPageLocators.ORDER_ITEM_LIST)

    @allure.title(' При клике на заказ, открывается окно с деталями')
    def open_order_list_details(self):
        self.wait_visibility_of_element(OrderListPageLocators.ORDER_ITEM_LIST)
        self.click_on_element(OrderListPageLocators.ORDER_ITEM_LIST)
        self.wait_visibility_of_element(OrderListPageLocators.ORDER_ITEM_DETAILS)

    @allure.step('Проверка, что данные о заказе отображаются')
    def is_order_list_details_visible(self):
        return self.check_displaying_of_element(OrderListPageLocators.ORDER_ITEM_DETAILS)

    @allure.step('Переход в личный кабинет, в раздел История заказов')
    def navigation_to_order_history(self):
        self.click_on_element(OrderListPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_visibility_of_element(OrderListPageLocators.ORDER_HISTORY_BUTTON)
        self.click_on_element(OrderListPageLocators.ORDER_HISTORY_BUTTON)
        self.wait_visibility_of_element(OrderListPageLocators.LOGOUT_BUTTON)


    def wait_for_order_in_history(self):
        self.wait_visibility_of_element(OrderListPageLocators.USER_ORDER_IN_HISTORY)

    def wait_for_order_in_feed(self):
        self.wait_visibility_of_element(OrderListPageLocators.ORDER_ITEM_LIST)

    @allure.step('Получаем последний номер заказа пользователя в Истории заказов')
    def get_order_nuber(self):
        element = self.wait_visibility_of_element(OrderListPageLocators.USER_ORDER_NUMBER_HISTORY)
        return element.text.replace('#', '').strip()

    @allure.step('Проверка, что номер заказа есть в Истории заказов')
    def is_order_in_history(self, order_number):
        formatted_number = str(order_number).rjust(7, '0')
        order_number_with_hash = f"#{formatted_number}"
        xpath = f"//p[contains(text(), '{order_number_with_hash}')]"
        return self.is_text_in_element(xpath, order_number_with_hash)

    @allure.step('Проверка, что номер заказа есть в Ленте заказов')
    def is_order_in_order_feed(self, order_number):
        formatted_number = str(order_number).rjust(7, '0')
        order_number_with_hash = f"#{formatted_number}"
        xpath = f"//p[contains(@class, 'text_type_digits-default') and text()='{order_number_with_hash}']"
        elements = self.find_elements(By.XPATH, xpath)
        return len(elements) > 0

    @allure.step('Получение значения счетчика "Выполнено за все время"')
    def get_total_orders_count(self):
        return self.get_numbers_from_element(OrderListPageLocators.TOTAL_ORDERS_COUNT)

    @allure.step('Получение значения счетчика "Выполнено за сегодня"')
    def get_total_orders_count_for_today(self):
        return self.get_numbers_from_element(OrderListPageLocators.TODAY_TOTAL_ORDER_COUNT)

    @allure.step('Проверка, что номер заказа есть в блоке "В работе"')
    def is_order_in_progress(self, order_number):
        formatted_number = str(order_number).rjust(7, '0')
        order_number_with_hash = f"#{formatted_number}"
        elements = self.find_elements(OrderListPageLocators.ORDER_IN_PROGRESS)
        return any(order_number_with_hash in element.text for element in elements)


    @allure.step('Обновили страницу')
    def refresh(self):
        super().refresh()


    @allure.step('Дожидаемся, чтобы число прогрузилось')
    def wait_today_total_order_count_visible(self):
        self.wait_visibility_of_element(OrderListPageLocators.TODAY_TOTAL_ORDER_COUNT)








