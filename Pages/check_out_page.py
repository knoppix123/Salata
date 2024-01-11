
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Checkout:

    def __init__(self, driver):
        self.driver = driver

    check_out_button = (By.XPATH, "(//*[contains(text(),'checkout as a guest')])[2]")


    def get_check_out_button(self):
        return self.driver.find_element(*Checkout.check_out_button)


