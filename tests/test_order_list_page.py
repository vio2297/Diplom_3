import allure
from api_client import ApiClient
from data import Login, Urls


class TestOrderListPage:
    @allure.title("Создание заказа через Api")
    def create_api_order(self):
        # Авторизация пользователя и создаем заказ через Api
        api = ApiClient().login(Login.EMAIL, Login.PASSWORD)
        with allure.step("Получение валидных ингредиентов"):
            ingredients = api.get_valid_ingredients()
            assert len(ingredients) >= 2, "Недостаточно ингредиентов для заказа"

        with allure.step("Создание заказа с ингредиентами"):
            result = api.create_order(ingredients[:2])
            assert result["success"] is True, "Создание заказа неудачно"
            return result["order"]["number"]

    @allure.title("Авторизация и переход в Ленту заказов")
    def auth_navigation_to_order_list(self, order_list_page):
        # Авторизация, переход на страницу Лента заказов
        order_list_page.login(Login.EMAIL, Login.PASSWORD)
        order_list_page.navigation_to_order_list()
        assert order_list_page.get_current_url() == Urls.ORDER_LIST_URL



    @allure.title("При клике на заказ, открывается всплывающее окно с деталями")
    @allure.description("Авторизуемся в аккаунт, переходим в раздел Лента заказов, кликаем на заказ и открывается окно с деталями заказа ")
    def test_open_order_history_details(self, driver, order_list_page):
        order_list_page.login(Login.EMAIL, Login.PASSWORD)
        order_list_page.navigation_to_order_list()
        assert order_list_page.get_current_url() == Urls.ORDER_LIST_URL
        order_list_page.open_order_list_details()
        assert order_list_page.is_order_list_details_visible()


    @allure.title("заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    @allure.description("Создаем заказ для пользователя через Api, проверяем, что заказ отображается в Личном кабинете в Истории заказов, проверяем, что этот же заказ отображается на странице Лента заказов")
    def test_user_order_in_order_list(self, driver, order_list_page):
        order_number = self.create_api_order()

        # Переходим в личный кабинет в раздел История заказов и проверяем что в списке есть заказ и получаем его номер
        order_list_page.login(Login.EMAIL, Login.PASSWORD)
        order_list_page.navigation_to_order_history()
        order_list_page.wait_for_order_in_history()
        assert order_list_page.get_current_url() == Urls.ORDER_HISTORY_URL
        assert order_list_page.is_order_in_history(order_number)

        # переходим в раздел Лента заказов и получаем номер последнего заказа
        order_list_page.navigation_to_order_list()
        order_list_page.wait_for_order_in_feed()
        assert order_list_page.get_current_url() == Urls.ORDER_LIST_URL
        assert order_list_page.is_order_in_order_feed(order_number)


    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    @allure.description("Переходим в раздел Лента заказов, проверяем счетчик Выполнено за все время:Создаем заказ через Api, переход в раздел Лента заказов и проверяем, что счетчик Выполнено за все время увеличился")

    def test_order_counter_increase_after_order_creation(self, driver, order_list_page):
        # Авторизация, переход на страницу Лента заказов
        self.auth_navigation_to_order_list(order_list_page)

        # Считывание счетчика До создания заказа
        old_count = order_list_page.get_total_orders_count()

        # Создание заказа через Api
        self.create_api_order()

        # Обновляем старицу
        driver.refresh()
        order_list_page.wait_today_total_order_count_visible()

        # Считываем значения счетчика после создания заказа
        new_count = order_list_page.get_total_orders_count()
        assert new_count > old_count

    @allure.title("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    @allure.description("Переходим в раздел Лента заказов, проверяем счетчик Выполнено за сегодня: Создаем заказ через Api, переход в раздел Лента заказов и проверяем, что счетчик Выполнено за сегодня увеличился")
    def test_order_for_today_increase_after_order_creation(self, driver, order_list_page):
        # Авторизация, переход на страницу Лента заказов
        self.auth_navigation_to_order_list(order_list_page)

        # Считывание счетчика До создания заказа
        old_count = order_list_page.get_total_orders_count_for_today()

        # Создание заказа через Api
        self.create_api_order()

        # Обновляем старицу
        driver.refresh()
        order_list_page.wait_today_total_order_count_visible()

        # Считываем значения счетчика после создания заказа
        new_count = order_list_page.get_total_orders_count_for_today()
        assert new_count > old_count


# этот тест падает, так как В работе сразу же исчезает и не успевает перехватить данные
    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    @allure.description("Авторизация, переход в раздел Лента заказов, создаем заказ через Api, проверяем, что номер заказа появляется в разделе В работе ")
    def test_order_number_appears_in_progress_section(self, driver, order_list_page):
        # Авторизация, переход на страницу Лента заказов
        self.auth_navigation_to_order_list(order_list_page)

        # Создание заказа через Api
        order_number = self.create_api_order()

        # Обновляем старицу
        driver.refresh()
        order_list_page.wait_today_total_order_count_visible()

        # Проверяем, что номер заказа появился в разделе В работе
        assert order_list_page.is_order_in_progress(order_number) , f"Заказ №{order_number} не найден в блоке 'В работе'"




