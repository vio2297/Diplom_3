import pytest
from selenium import webdriver

from api_client import ApiClient
from data import Urls, Login
from pages.main_page import MainPage
from pages.order_list_page import OrderListPage
from pages.password_recovery_page import PasswordRecoveryPage
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pages.personal_account_page import PersonalAccountPage


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    elif request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)


    driver.maximize_window()
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def password_recovery_page(driver):
    return PasswordRecoveryPage(driver)

@pytest.fixture
def personal_account_page(driver):
    return PersonalAccountPage(driver)

@pytest.fixture
def order_list_page(driver):
    return OrderListPage(driver)

@pytest.fixture
def create_and_login_user():
    api = ApiClient().login(Login.EMAIL, Login.PASSWORD)
    return api

@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def auth_and_navigate_constructor(main_page):
    main_page.login(Login.EMAIL, Login.PASSWORD)
    main_page.navigation_to_constructor()
    assert main_page.check_element_displayed()

