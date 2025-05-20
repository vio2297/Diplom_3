import allure

from pages.base_page import BasePage
from locators.passwod_recovery_page_locators import PasswordRecoveryLocators

class PasswordRecoveryPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.locators = PasswordRecoveryLocators()

    @allure.step('Нажатие на кнопку Войти в аккаунт')
    def click_on_login_button(self):
        self.wait_visibility_of_element(self.locators.LOGIN_BUTTON_MAIN_PAGE)
        self.click_on_element(self.locators.LOGIN_BUTTON_MAIN_PAGE)
        self.wait_visibility_of_element(self.locators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Нажатие на кнопку "Восстановить пароль"')
    def click_on_password_recovery_button(self):
        self.click_on_element(self.locators.PASSWORD_RECOVERY_BUTTON)
        self.wait_visibility_of_element(self.locators.RECOVERY_BUTTON)

    @allure.step('Заполнить поле Email')
    def set_email(self, email):
        self.set_text_in_element(self.locators.EMAIL_RECOVERY_INPUT, email)
        self.click_on_element(self.locators.RECOVERY_BUTTON)
        self.wait_visibility_of_element(self.locators.SAVE_DETAILS_BUTTON)

    @allure.step('Проверить что кнопка отображается')
    def check_save_details_button_displayed(self):
        return self.check_displaying_of_element(self.locators.SAVE_DETAILS_BUTTON)

    @allure.step('Нажатие на глаз показать/скрыть пароль')
    def click_on_eye(self):
        self.wait_visibility_of_element(self.locators.EYE_HIDE_SHOW_PASSWORD_BUTTON)
        self.click_on_element(self.locators.EYE_HIDE_SHOW_PASSWORD_BUTTON)
        self.wait_visibility_of_element(self.locators.HIGHLIGHTED_FIELD)

    @allure.step('Проверка отображения элемента')
    def check_displaying_element(self):
        return self.check_displaying_of_element(self.locators.HIGHLIGHTED_FIELD)





