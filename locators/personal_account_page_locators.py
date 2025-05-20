from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    LOGIN_INTO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    USER_ORDER_IN_HISTORY = (By.XPATH, "//a[contains(@href, '/account/order-history') and contains(text(), 'История заказов')]")
    USER_ORDER_NUMBER_HISTORY = (By.XPATH, "//div[starts-with(@class, 'OrderHistory_textBox')]")