from tests.config import url


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get(url)

    def get_catalog(self):
        return self.driver.find_element_by_xpath("//*[contains(text(),'Собственное производство')]")
