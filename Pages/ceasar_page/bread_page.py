
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Breadselection:

    def __init__(self, driver):
        self.driver = driver

    croissant = (By.XPATH, "//*[contains(text(),' Croissant ')]")
    next_button = (By.XPATH, "(//*[contains(text(),'Next')])")




    def get_croissant(self):
        return self.driver.find_element(*Breadselection.croissant)
    def get_next_button(self):
        return self.driver.find_element(*Breadselection.next_button)