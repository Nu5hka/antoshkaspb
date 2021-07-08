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


response = requests.post(url=f"{url}/login", data={"email": email, "pass": password})
driver.get(url)
cookie_list = response.requests.headers.get('Cookie').split('=')
print(cookie_list)
driver.add_cookie({"name": cookie_list[0], "value": cookie_list[1]})
