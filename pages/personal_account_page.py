import time

import allure

from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    @allure.title('Авторизация')
    def login(self, email, password):
        self.set_text_in_element(PersonalAccountPageLocators.EMAIL_FIELD, email)
        self.set_text_in_element(PersonalAccountPageLocators.PASSWORD_FIELD, password)
        self.click_on_element(PersonalAccountPageLocators.LOGIN_BUTTON)
        time.sleep(2)
        self.wait_visibility_of_element(PersonalAccountPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.title('Переход на страницу авторизации')
    def navigation_to_auth_acc(self):
        self.click_on_element(PersonalAccountPageLocators.LOGIN_INTO_ACCOUNT_BUTTON)
        self.wait_visibility_of_element(PersonalAccountPageLocators.LOGIN_BUTTON)

    @allure.title('Переход в личный кабинет')
    def navigation_to_personal_account(self):
        self.click_on_element(PersonalAccountPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_visibility_of_element(PersonalAccountPageLocators.LOGOUT_BUTTON)

    @allure.title('Переход в Историю заказов')
    def navigation_to_order_history(self):
        self.click_on_element(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)
        self.wait_visibility_of_element(PersonalAccountPageLocators.ORDER_HISTORY_BUTTON)
        time.sleep(1)

    @allure.title('Выход из аккаунта')
    def logout_from_account(self):
        self.click_on_element(PersonalAccountPageLocators.LOGOUT_BUTTON)
        self.wait_visibility_of_element(PersonalAccountPageLocators.LOGIN_BUTTON)

