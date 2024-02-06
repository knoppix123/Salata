
from selenium.webdriver.common.by import By


class Grouporder:

    def __init__(self, driver):
        self.driver = driver
    group_order_title = (By.XPATH, "//*[contains(text(),'Start your group order:')]")

    def get_group_order_title(self):
        return self.driver.find_element(*Grouporder.group_order_title)


