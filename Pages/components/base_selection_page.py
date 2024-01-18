
from selenium.webdriver.common.by import By

class Selectionbase:

    def __init__(self, driver):
        self.driver = driver

    no_base = (By.XPATH, "(//*[contains(text(),'No Base')])")
    salata_mix = (By.XPATH, "(//*[contains(text(),' Salata Mix ')])")
    romaine_hearts = (By.XPATH, "//*[contains(text(),' Romaine Hearts ')]")
    next_button = (By.XPATH, "(//*[contains(text(),'Next')])")

    def get_no_base(self):
        return self.driver.find_element(*Selectionbase.no_base)
    def get_salata_mix(self):
        return self.driver.find_element(*Selectionbase.salata_mix)
    def get_romaine_hearts(self):
        return self.driver.find_element(*Selectionbase.romaine_hearts)
    def get_next_button(self):
        return self.driver.find_element(*Selectionbase.next_button)





