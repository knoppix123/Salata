
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Saladselection:

    def __init__(self, driver):
        self.driver = driver

    ceasar_salad = (By.XPATH, "//*[contains(text(),'Caesar Salad')]")
    next_button = (By.XPATH, "(//*[contains(text(),'NEXT')])[2]")
    check_out_button_first = (By.XPATH, "(//span[contains(text(),'Checkout')])[4]")

    def get_ceasar_salad(self):
        return self.driver.find_element(*Saladselection.ceasar_salad)
    def get_next_button(self):
        return self.driver.find_element(*Saladselection.next_button)
    def get_check_out_button_first(self):
        return self.driver.find_element(*Saladselection.check_out_button_first)