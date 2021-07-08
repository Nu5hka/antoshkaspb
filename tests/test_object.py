from pages.base_page import BasePage
from pages.own_page import OwnPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_visit(driver):
    base_page = BasePage(driver)
    base_page.visit()
    assert base_page.get_catalog().is_displayed


def test_catalog(driver):
    base_page = BasePage(driver)
    base_page.visit()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "toTop")))
    base_page.get_catalog().click()
    own_page = OwnPage(driver)
    assert own_page.get_new_year().is_displayed


def test_visit_log(driver_with_cookeis):
    driver_with_cookeis.get('https://antoshkaspb.ru/my/orders/')
    assert driver_with_cookeis.title == 'Заказы'

# pytest -v -s -k "_"
