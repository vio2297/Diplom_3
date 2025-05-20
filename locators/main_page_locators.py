from selenium.webdriver.common.by import By


class MainPageLocators:
    # Authorization/Login
    LOGIN_INTO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Navigation
    ORDER_LIST_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Order List
    ORDER_ITEM_LIST = (By.XPATH, '(//li[contains(@class, "OrderHistory_listItem__2x95r")])[1]')

    # Constructor
    INGREDIENT_BUTTON = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    INGREDIENT_DETAILS = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]")
    CLOSE_WINDOW = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    INGREDIENT_COUNTER = (By.XPATH,"//div[contains(@class, 'counter_counter__ZNLkj')][../img[@alt='Флюоресцентная булка R2-D3']]//p")
    CART = (By.XPATH, "//span[contains(@class, 'constructor-element__text') and contains(text(), 'Перетяните булочку сюда')]")

    ORDER_CONFIRM_MESSAGE = (By.XPATH,"//div[contains(@class, 'Modal_modal__contentBox')]")
    SAUCE = (By.XPATH, "//img[@alt='Соус Spicy-X']")

