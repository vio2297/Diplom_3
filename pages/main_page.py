import allure
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.title('Авторизация')
    def login(self, email, password):
        self.wait_visibility_of_element(MainPageLocators.LOGIN_INTO_ACCOUNT_BUTTON)
        self.click_on_element(MainPageLocators.LOGIN_INTO_ACCOUNT_BUTTON)
        self.set_text_in_element(MainPageLocators.EMAIL_FIELD, email)
        self.set_text_in_element(MainPageLocators.PASSWORD_FIELD, password)
        self.click_on_element(MainPageLocators.LOGIN_BUTTON)
        self.wait_visibility_of_element(MainPageLocators.INGREDIENT_BUTTON)

    @allure.step('Переход в раздел Конструктор')
    def navigation_to_constructor(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_visibility_of_element(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Проверка наличия элемента')
    def check_element_displayed(self):
        return self.check_displaying_of_element(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.title('Переход в раздел Лента заказов')
    def navigation_to_order_list(self):
        self.click_on_element(MainPageLocators.ORDER_LIST_BUTTON)
        self.wait_visibility_of_element(MainPageLocators.ORDER_ITEM_LIST)

    @allure.title('При нажатии на ингредиент откроется окно с деталями')
    def click_on_element_opens_details(self):
        self.click_on_element(MainPageLocators.INGREDIENT_BUTTON)
        self.wait_visibility_of_element(MainPageLocators.INGREDIENT_DETAILS)

    @allure.title('Проверка отображения окна с деталями')
    def check_details_displayed(self):
        return self.check_displaying_of_element(MainPageLocators.INGREDIENT_DETAILS)

    @allure.title('Закрытия окна с деталями при нажатии на крестик')
    def close_window_with_details(self):
        self.click_on_element(MainPageLocators.CLOSE_WINDOW)
        self.wait_visibility_of_element(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Получаем значение счетчика ингредиента')
    def get_ingredient_counter(self):
        try:
            text = self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER)
            return int(text)
        except (NoSuchElementException, TimeoutException):
            return 0

    @allure.step('Перетаскиваем ингредиент в корзину')
    def drag_ingredient_to_cart(self):
        ingredient = self.wait_visibility_of_element(MainPageLocators.INGREDIENT_BUTTON)
        cart = self.wait_visibility_of_element(MainPageLocators.CART)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, cart).perform()


    @allure.step('Перетаскиваем ингредиенты в корзину и оформляем заказ')
    def drag_ingredient_to_cart_and_make_order(self):
        bun = self.wait_visibility_of_element(MainPageLocators.INGREDIENT_BUTTON)
        sauce = self.wait_visibility_of_element(MainPageLocators.SAUCE)
        cart = self.wait_visibility_of_element(MainPageLocators.CART)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(bun, cart).perform()
        actions.drag_and_drop(sauce, cart).perform()
        self.click_on_element(MainPageLocators.MAKE_ORDER_BUTTON)


    @allure.step('Получаем сообщение об успешном заказе')
    def displaying_of_order_confirm(self):
        return self.check_displaying_of_element(MainPageLocators.ORDER_CONFIRM_MESSAGE)







