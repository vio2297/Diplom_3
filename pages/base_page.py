import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def wait_visibility_of_element(self,locator):
        return WebDriverWait(self.driver, 25).until(ec.visibility_of_element_located(locator))

    @allure.step('Получаем адрес страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ввести значение в поле ввода')
    def set_text_in_element(self, locator, text):
        element = self.wait_visibility_of_element(locator)
        element.send_keys(text)

    @allure.step('Проверка отображения элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Поиск всех элементов по локатору')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Поиск элементов по Xpath с текстом')
    def is_text_in_element(self, xpath, text):
        elements = self.driver.find_elements(By.XPATH, xpath)
        for element in elements:
            if text in element.text:
                return True
        return False


    @allure.step('Получение цифр элемента')
    def get_numbers_from_element(self, locator):
        element = self.driver.find_element(*locator)
        text = element.text.replace(' ', '').strip()
        return int(text)

    @allure.step('Получение текста элемента')
    def get_text_from_element(self, locator):
        element = self.wait_visibility_of_element(locator)
        return element.text.strip()

    @allure.step('Получение числового значения')
    def get_integer_from_element(self, locator):
        text = self.get_text_from_element(locator)
        return int(text.replace(' ', ''))

    @allure.step('Поиск текста в списке элементов по xpath')
    def search_text_in_element(self, xpath, text):
        elements = self.driver.find_elements(By.XPATH, xpath)
        return any(text in element.text for element in elements)



