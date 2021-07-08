class OwnPage(object):
    def __init__(self, driver):
        self.driver = driver

    def get_new_year(self):
        return self.driver.find_element_by_xpath("//*[contains(text(),'Детские новогодние костюмы')]")
