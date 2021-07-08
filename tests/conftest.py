import pytest
import requests
from selenium import webdriver
from tests.config import email, password, url


@pytest.fixture(scope="function")
def driver(request):
    path = str(request.fspath)
    print(request.fspath)
    driver = webdriver.Chrome(f"{path[:path.find('tests')]}tests/chromedriver")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    # driver.close()


@pytest.fixture(scope="function")
def driver_with_cookeis(driver):
    response = requests.post(url=f"{url}/login", data={"email": email, "pass": password})
    assert response.status_code == 200, 'Запрос выполнен успешно'
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ активации'
    print("\ngetting auth_key")
    driver.get(url)
    a = response.request.headers.get('cookie').split(';')
    cookie_list = a[0].split("=")
    print(cookie_list)
    driver.add_cookie({"name": cookie_list[0], "value": cookie_list[1]})
    yield driver
