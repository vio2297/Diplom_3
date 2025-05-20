from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")
    RECOVERY_BUTTON = (By.XPATH, "//button[text() = 'Восстановить']")
    EMAIL_RECOVERY_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    SAVE_DETAILS_BUTTON = (By.XPATH, "//button[text() = 'Сохранить']")
    PASSWORD_RECOVERY_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input ")
    EYE_HIDE_SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class,'input__icon input__icon-action')]")
    HIGHLIGHTED_FIELD = (By.XPATH, "//div[contains(@class, 'input_status_active') and contains(@class, 'input_type_text')]")


