
from selenium.webdriver.common.by import By

class Proteinselection:

    def __init__(self, driver):
        self.driver = driver

    grilled_chicken = (By.XPATH, "(//*[contains(text(),' Grilled Chicken ')])")
    pesto_chicken = (By.XPATH, "(//*[contains(text(),' Pesto Chicken ')])")
    arrow_right1 = (By.XPATH, "(//*[@name='md-arrow-dropright'])[1]")
    arrow_left1 = (By.XPATH, "(//*[@name='md-arrow-dropleft'])[1]")
    arrow_right2 = (By.XPATH, "(//*[@name='md-arrow-dropright'])[2]")
    amount = (By.XPATH, "(//*[contains(text(),'$48.30')])[2]")
    next_button = (By.XPATH, "(//*[contains(text(),'Next')])")


    def get_grilled_chicken(self):
        return self.driver.find_element(*Proteinselection.grilled_chicken)
    def get_pesto_chicken(self):
        return self.driver.find_element(*Proteinselection.pesto_chicken)

    def get_arrow_right1(self):
        return self.driver.find_element(*Proteinselection.arrow_right1)
    def get_arrow_right2(self):
        return self.driver.find_element(*Proteinselection.arrow_right2)
    def get_amount(self):
        return self.driver.find_element(*Proteinselection.amount)
    def get_next_button(self):
        return self.driver.find_element(*Proteinselection.next_button)
