
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Guestcheckout:

    def __init__(self, driver):
        self.driver = driver

    firstname_field = (By.CSS_SELECTOR, "[id='firstname']")
    lastname_field = (By.CSS_SELECTOR, "[id='lastname']")
    email_field = (By.XPATH, "(//*[@id='username'])[2]")
    phone_number_field = (By.CSS_SELECTOR, "[id='contactnumber']")
    next_button = (By.XPATH, "(//*[contains(text(),'Next')])")
    next_button3 = (By.XPATH,"(//*[contains(text(),'NEXT')])[3]" )
    next_button5 = (By.XPATH,"(//*[contains(text(),'NEXT')])[5]" )


    cc_number_field = (By.CSS_SELECTOR, "[id='ccnumber']")
    ccv_number_field = (By.CSS_SELECTOR, "[id='cardcvv']")
    expiration_cc_field = (By.CSS_SELECTOR, "[id='cardexp']")
    zipzode = (By.CSS_SELECTOR, "[id='cardzip']")
    # tip_10 = (By.XPATH, "//*[@class='col']//*[contains(text(),'10%')]")
    tip_10 = (By.XPATH, "(//*[@class='col']//*[@class='btn-outline-dark btn-sm btn'])[4]")

    complete_order_button =(By.XPATH, "(//*[contains(text(),'COMPLETE ORDER')])[2]")


    def get_firstname_field(self):
        return self.driver.find_element(*Guestcheckout.firstname_field)
    def get_lastname_field(self):
        return self.driver.find_element(*Guestcheckout.lastname_field)
    def get_email_field(self):
        return self.driver.find_element(*Guestcheckout.email_field)
    def get_phone_number_field(self):
        return self.driver.find_element(*Guestcheckout.phone_number_field)
    def get_next_button(self):
        return self.driver.find_element(*Guestcheckout.next_button)
    def get_next_button3(self):
        return self.driver.find_element(*Guestcheckout.next_button3)
    def get_next_button5(self):
        return self.driver.find_element(*Guestcheckout.next_button5)


    def get_cc_number_field(self):
        return self.driver.find_element(*Guestcheckout.cc_number_field)
    def get_ccv_number_field(self):
        return self.driver.find_element(*Guestcheckout.ccv_number_field)
    def get_expiration_cc_field(self):
        return self.driver.find_element(*Guestcheckout.expiration_cc_field)
    def get_zipzode(self):
        return self.driver.find_element(*Guestcheckout.zipzode)
    def get_tip_10(self):
        return self.driver.find_element(*Guestcheckout.tip_10)
    def get_complete_order_button(self):
        return self.driver.find_element(*Guestcheckout.complete_order_button)



