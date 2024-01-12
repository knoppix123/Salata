
from selenium.webdriver.common.by import By

class Toppicsselection:

    def __init__(self, driver):
        self.driver = driver

    no_toppings = (By.XPATH, "(//*[contains(text(),'No toppings')])")
    tomato = (By.XPATH, "(//*[contains(text(),' Tomato ')])")
    cucumber = (By.XPATH, "//*[contains(text(),'Cucumber')]")
    next_button = (By.XPATH, "(//*[contains(text(),'Next')])")

    def get_no_toppings(self):
        return self.driver.find_element(*Toppicsselection.no_base)
    def get_tomato(self):
        return self.driver.find_element(*Toppicsselection.tomato)
    def get_cucumber(self):
        return self.driver.find_element(*Toppicsselection.cucumber)
    def get_next_button(self):
        return self.driver.find_element(*Toppicsselection.next_button)





