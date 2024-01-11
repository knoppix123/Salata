
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Ceasarselection:

    def __init__(self, driver):
        self.driver = driver

    ceasar_regular_salad = (By.XPATH, "(//*[contains(text(),' Regular Salad ')])[2]")
    arrow_right = (By.CSS_SELECTOR,"[name='md-arrow-dropright']")
    arrow_left = (By.CSS_SELECTOR, "[name='md-arrow-dropleft']")
    quantiny = (By.CSS_SELECTOR, "[class='quantity']")
    next_button = (By.XPATH, "(//*[contains(text(),'Next')])")


    def get_ceasar_regular_salad(self):
        return self.driver.find_element(*Ceasarselection.ceasar_regular_salad)
    def get_arrow_right(self):
        return self.driver.find_element(*Ceasarselection.arrow_right)
    def get_arrow_left(self):
        return self.driver.find_element(*Ceasarselection.arrow_left)
    def get_quantiny(self):
        return self.driver.find_element(*Ceasarselection.quantiny)
    def get_next_button(self):
        return self.driver.find_element(*Ceasarselection.next_button)



