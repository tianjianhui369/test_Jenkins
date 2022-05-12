from selenium.webdriver.support.wait import WebDriverWait



class Base:
    def __init__(self,driver):
        self.driver = driver
    def base_find_element(self,location):
        location_By,location_action = location
        return WebDriverWait(self.driver,timeout=20,poll_frequency=0.5).until(lambda x:x.find_element(location_By,location_action))
    def base_click(self,location):
        self.base_find_element(location).click()
    def base_input(self,location,value):
        self.base_find_element(location).send_keys(value)