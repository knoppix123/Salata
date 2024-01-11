
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Plastickit:

    def __init__(self, driver):
        self.driver = driver

    plastic_kits = (By.XPATH, "(//*[contains(text(),'No Plasticware Kit ')])[2]")
    add_to_bag = (By.XPATH, "(//*[contains(text(),' Add To Bag ')])[1]")

    def get_plastic_kits(self):
        return self.driver.find_element(*Plastickit.plastic_kits)
    def get_add_to_bag(self):
        return self.driver.find_element(*Plastickit.add_to_bag)
