import allure
from data import Login, Urls
from helpers import navigation_to_personal_account


class TestPersonalAccount:


    @allure.title("Переход по клику на 'Личный кабинет'")
    @allure.description("Авторизуемся и при нажатии на кнопку 'Личный кабинет' переходим в него")
    def test_transfer_to_personal_account(self, driver, personal_account_page):
        navigation_to_personal_account(personal_account_page)
        assert personal_account_page.get_current_url() == Urls.PERSONAL_ACCOUNT_URL

    @allure.title("Переход в раздел История заказов")
    @allure.description("Авторизация и переход в раздел История заказов")
    def test_navigation_to_order_history(self, driver, personal_account_page):
        navigation_to_personal_account(personal_account_page)
        personal_account_page.navigation_to_order_history()
        assert personal_account_page.get_current_url() == Urls.ORDER_HISTORY_URL

    @allure.title("Выход из аккаунта")
    @allure.title("Авторизация, переход в личный кабинет и выход из аккаунта")
    def test_logout_from_account(self, driver, personal_account_page):
        navigation_to_personal_account(personal_account_page)
        personal_account_page.logout_from_account()
        assert personal_account_page.get_current_url() == Urls.LOGIN_PAGE_URL






