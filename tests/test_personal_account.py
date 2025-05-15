import allure
from data import Login, Urls


class TestPersonalAccount:

    def navigation_to_personal_account(self, personal_account_page):
        personal_account_page.navigation_to_auth_acc()
        personal_account_page.login(Login.EMAIL, Login.PASSWORD)
        personal_account_page.navigation_to_personal_account()
        assert personal_account_page.get_current_url() == Urls.PERSONAL_ACCOUNT_URL


    @allure.title("Переход по клику на 'Личный кабинет'")
    @allure.description("Авторизуемся и при нажатии на кнопку 'Личный кабинет' переходим в него")
    def test_transfer_to_personal_account(self, driver, personal_account_page):
        self.navigation_to_personal_account(personal_account_page)

    @allure.title("Переход в раздел История заказов")
    @allure.description("Авторизация и переход в раздел История заказов")
    def test_navigation_to_order_history(self, driver, personal_account_page):
        self.navigation_to_personal_account(personal_account_page)
        personal_account_page.navigation_to_order_history()
        assert personal_account_page.get_current_url() == Urls.ORDER_HISTORY_URL

    @allure.title("Выход из аккаунта")
    @allure.title("Авторизация, переход в личный кабинет и выход из аккаунта")
    def test_logout_from_account(self, driver, personal_account_page):
        self.navigation_to_personal_account(personal_account_page)
        personal_account_page.logout_from_account()
        assert personal_account_page.get_current_url() == Urls.LOGIN_PAGE_URL






