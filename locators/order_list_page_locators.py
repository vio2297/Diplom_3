from selenium.webdriver.common.by import By


class OrderListPageLocators:

    # Authorization/Login
    LOGIN_INTO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    # Navigation
    ORDER_LIST_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    ORDER_HISTORY_BUTTON = (By.XPATH, '//a[text()="История заказов"]')

    # Order List
    ORDER_ITEM_LIST = (By.XPATH, '(//li[contains(@class, "OrderHistory_listItem__2x95r")])[1]')
    ORDER_ITEM_DETAILS = (By.XPATH, '//div[contains(@class, "Modal_orderBox__1xWdi")]')

    #Order History
    USER_ORDER_NUMBER_HISTORY = (By.XPATH, "//div[starts-with(@class, 'OrderHistory_textBox')]")
    USER_ORDER_IN_HISTORY = (By.XPATH, "//a[starts-with(@href, '/account/order-history/')]")

    # Counters
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_TOTAL_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    # In progress
    ORDER_IN_PROGRESS = (By.XPATH, "//p[text()='В работе:']/following-sibling::ul/li")


