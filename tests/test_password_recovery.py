import allure

from data import Urls, Login


class TestPasswordRecovery:

    @allure.description("Заготовка для входа на страницу восстановления пароля")
    def transfer_to_recovery_test(self, password_recovery_page):
        password_recovery_page.click_on_login_button()
        password_recovery_page.click_on_password_recovery_button()
        assert password_recovery_page.get_current_url() == Urls.PASSWORD_RECOVERY_URL

    @allure.title("Проверка на успешны переход на страницу восстановления пароля ")
    @allure.description("Проверка на переход на страницу восстановления пароля при нажатии на кнопку 'Восстановить пароль'")
    def test_transfer_to_recovery_page(self, driver, password_recovery_page):
        self.transfer_to_recovery_test(password_recovery_page)

    @allure.title("Ввод email в поле и переход в страницу для восстановления пароля ")
    @allure.description("Вводим email в поле и переходим на страницу для восстановления пароля")
    def test_recovery_email(self, driver, password_recovery_page):
        self.transfer_to_recovery_test(password_recovery_page)
        password_recovery_page.set_email(Login.EMAIL)
        assert password_recovery_page.check_save_details_button_displayed()

    @allure.title("При клике на глаз показать/скрыть пароль поле для ввода пароля становится активным")
    @allure.description("Поле становится активным и подсвечивается синим поле Пароль")
    def test_click_on_eye_highlights_the_field(self, driver, password_recovery_page):
        self.transfer_to_recovery_test(password_recovery_page)
        password_recovery_page.set_email(Login.EMAIL)
        password_recovery_page.click_on_eye()
        assert password_recovery_page.check_displaying_element()







