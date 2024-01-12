from selenium.webdriver.common.by import By


class Spicyshrimsalad:

    def __init__(self, driver):
        self.driver = driver

    small_spicy_salad = (By.XPATH, "//*[contains(text(),' Small Spicy Shrimp Salad ')]")
    next_button = (By.XPATH, "(//*[contains(text(),'Next')])")


    def get_small_spicy_salad(self):
        return self.driver.find_element(*Spicyshrimsalad.small_spicy_salad)
    def get_next_button(self):
        return self.driver.find_element(*Spicyshrimsalad.next_button)