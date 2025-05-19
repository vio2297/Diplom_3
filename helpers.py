import allure
from api_client import ApiClient
from data import Login, Urls

@allure.title("Создание заказа через Api")
def create_api_order():
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
def auth_navigation_to_order_list(order_list_page):
      # Авторизация, переход на страницу Лента заказов
    order_list_page.login(Login.EMAIL, Login.PASSWORD)
    order_list_page.navigation_to_order_list()
    assert order_list_page.get_current_url() == Urls.ORDER_LIST_URL