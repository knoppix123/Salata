
from selenium.webdriver.common.by import By

class Mainpage:

    def __init__(self, driver):
        self.driver = driver

    accept_cookies_button = (By.XPATH, "//*[contains(text(),'Accept')]")
    accept_cookies_button2 = (By.XPATH, "(//*[contains(text(),'ACCEPT')])[2]")


    logo_button = (By.CSS_SELECTOR, "[class='components__SiteLogo-sc-dracue-7 frXYGZ']")

    menu_button = (By.XPATH, "//*[@class='components__NavItem-sc-dracue-4 gyitpF']//*[contains(text(),'Menu')]")
    dressing_button =  (By.XPATH, "//*[@class='components__NavItem-sc-dracue-4 gyitpF']//*[contains(text(),'Dressings')]")
    catering_button =  (By.XPATH, "//*[@class='components__NavItem-sc-dracue-4 gyitpF']//*[contains(text(),'Catering')]")
    loyalty_button =  (By.XPATH, "//*[@class='components__NavItem-sc-dracue-4 gyitpF']//*[contains(text(),'Loyalty')]")
    gift_cards_button =  (By.XPATH, "//*[@class='components__NavItem-sc-dracue-4 gyitpF']//*[contains(text(),'Gift Cards')]")
    grow_with_us_button =  (By.XPATH, "//*[@class='components__NavItem-sc-dracue-4 gyitpF']//*[contains(text(),'Grow With Us')]")
    find_my_salata_button =  (By.CSS_SELECTOR, "[class='FindLocationButton__Anchor-sc-s9xnuw-0 brttVm']")
    order_now_button = (By.CSS_SELECTOR, "[class='Button__Link-sc-1dc0h4n-1 cEABiC']")
    individual_order_button  = (By.XPATH, "//*[@class='components__NestedNavList-sc-dracue-6 imwAga']//*[contains(text(),'Individual Order')]")
    catering_order = (By.XPATH, "//*[@class='components__NestedNavList-sc-dracue-6 imwAga']//*[contains(text(),'Catering Order')]")
    group_order = (By.XPATH, "//*[@class='components__NestedNavList-sc-dracue-6 imwAga']//*[contains(text(),'Group Ordering')]")


    def get_accept_cookies_button(self):
        return self.driver.find_element(*Mainpage.accept_cookies_button)
    def get_accept_cookies_button2(self):
        return self.driver.find_element(*Mainpage.accept_cookies_button2)
    def get_logo(self):
        return self.driver.find_element(*Mainpage.logo_button)

    def get_menu_button(self):
        return self.driver.find_element(*Mainpage.menu_button)
    def get_dressing_button(self):
        return self.driver.find_element(*Mainpage.dressing_button)
    def get_catering_button(self):
        return self.driver.find_element(*Mainpage.catering_button)
    def get_loyalty_button(self):
        return self.driver.find_element(*Mainpage.loyalty_button)
    def get_gift_cards_button(self):
        return self.driver.find_element(*Mainpage.gift_cards_button)
    def get_grow_with_us_button(self):
        return self.driver.find_element(*Mainpage.grow_with_us_button)
    def get_find_my_salata_button(self):
        return self.driver.find_element(*Mainpage.find_my_salata_button)
    def get_order_now_button(self):
        return self.driver.find_element(*Mainpage.order_now_button)
    def get_individual_order_button(self):
        return self.driver.find_element(*Mainpage.individual_order_button)
    def get_catering_order(self):
        return self.driver.find_element(*Mainpage.catering_button)
    def get_group_order(self):
        return self.driver.find_element(*Mainpage.group_order)

