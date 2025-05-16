import allure

from data import Login, Urls


class TestMainPage:

    @allure.title("Переход по клику на «Конструктор")
    @allure.description("Авторизация и переход в раздел Конструктор")
    def test_navigation_to_constructor(self, driver, main_page, auth_and_navigate_constructor):
        pass


    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    @allure.description("Авторизация, переход в раздел конструктор, проверка, что при клике на ингредиент, появится всплывающее окно с деталями ")
    def test_click_on_ingredient_opens_details(self, driver, main_page, auth_and_navigate_constructor):
        main_page.click_on_element_opens_details()
        assert main_page.check_details_displayed()



    @allure.title("Всплывающее окно закрывается кликом по крестику")
    @allure.description("Авторизация, переход в раздел конструктор,клик на ингредиент, появится всплывающее окно с деталями, проверяем, что его можно закрыть нажав на крестик")
    def test_close_window_with_details_by_click_on_x(self, driver, main_page, auth_and_navigate_constructor):
        main_page.click_on_element_opens_details()
        assert main_page.check_details_displayed()
        main_page.close_window_with_details()
        assert main_page.check_element_displayed()




    @allure.title("При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    @allure.description("Проверяем исходное состояние счетчика, перетягиваем ингредиент в корзину, и проверяем, что счетчик данного ингредиента повысился на одну единицу")
    def test_counter_change_after_ingredient_added(self, driver, main_page):
        main_page.login(Login.EMAIL, Login.PASSWORD)
        start_value = main_page.get_ingredient_counter()
        assert start_value == 0
        main_page.drag_ingredient_to_cart()
        after_value = main_page.get_ingredient_counter()
        assert after_value == start_value + 2



    @allure.title("Авторизированный пользователь может оформить заказ")
    @allure.description("Авторизация, добавление ингредиентов в корзину и оформление заказа. Проверка, что заказ оформлен")
    def test_success_order_with_auth_user(self,driver, main_page):
        main_page.login(Login.EMAIL, Login.PASSWORD)
        main_page.drag_ingredient_to_cart_and_make_order()
        assert main_page.displaying_of_order_confirm()



    @allure.title("Переход по клику на «Лента заказов")
    @allure.description("Авторизация и переход по клику на Ленту заказов")
    def test_navigation_to_order_list(self, driver, main_page):
        main_page.login(Login.EMAIL, Login.PASSWORD)
        main_page.navigation_to_order_list()
        assert main_page.get_current_url() == Urls.ORDER_LIST_URL
