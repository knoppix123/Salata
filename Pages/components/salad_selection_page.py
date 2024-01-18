
from selenium.webdriver.common.by import By

class Saladselection:

    def __init__(self, driver):
        self.driver = driver

    ceasar_salad = (By.XPATH, "//*[contains(text(),'Caesar Salad')]")
    spicy_shrimp_salad = (By.XPATH, "//*[contains(text(),'Spicy Shrimp Salad ')]")
    wrap = (By.XPATH,"(//app-item-box//*[contains(text(),'Wrap ')])[1]" )


    next_button = (By.XPATH, "(//*[contains(text(),'NEXT')])[2]")
    check_out_button_first = (By.XPATH, "(//span[contains(text(),'Checkout')])[4]")

    def get_ceasar_salad(self):
        return self.driver.find_element(*Saladselection.ceasar_salad)
    def get_spicy_shrimp_salad(self):
        return self.driver.find_element(*Saladselection.spicy_shrimp_salad)
    def get_wrap(self):
        return self.driver.find_element(*Saladselection.wrap)
    def get_next_button(self):
        return self.driver.find_element(*Saladselection.next_button)
    def get_check_out_button_first(self):
        return self.driver.find_element(*Saladselection.check_out_button_first)