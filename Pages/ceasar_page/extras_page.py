
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Extrasselection:

    def __init__(self, driver):
        self.driver = driver

    avocado = (By.XPATH, "(//*[contains(text(),' Avocado')])[2]")
    next_button = (By.XPATH, "(//*[contains(text(),'Next')])")


    def get_avocado(self):
        return self.driver.find_element(*Extrasselection.avocado)
    def get_next_button(self):
        return self.driver.find_element(*Extrasselection.next_button)