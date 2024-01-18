
from selenium.webdriver.common.by import By


class Thirdpartydelivery:

    def __init__(self, driver):
        self.driver = driver

    third_party_delivery_title = (By.XPATH, "(//*[@class='login'])[1]")
    calendarselection = (By.XPATH, "//*[@class='input-group-append']")


    def get_third_party_delivery_title(self):
        return self.driver.find_element(*Thirdpartydelivery.third_party_delivery_title)
    def get_calendarselection(self):
        return self.driver.find_element(*Thirdpartydelivery.calendarselection)

