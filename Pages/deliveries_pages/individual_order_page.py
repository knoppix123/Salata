from selenium.webdriver.common.by import By

class Individual():
    def __init__(self,driver):
        self.driver = driver

    delivery_title = (By.XPATH, "//*[contains(text(),' Enter your delivery information ')]")
    address_field = (By.CSS_SELECTOR, "[formcontrolname='streetAddress']")
    city_field = (By.CSS_SELECTOR, "[formcontrolname='city']")
    zip_field = (By.CSS_SELECTOR, "[formcontrolname='zipCode']")
    phone_field = (By.CSS_SELECTOR, "[formcontrolname='phonenumber']")
    special_instructions_field = (By.CSS_SELECTOR, "[name='specialInstructions']")
    submit_button = (By.XPATH, "(//*[@class='abstract-button'])[2]")

    def get_delivery_title(self):
        return self.driver.find_element(*Individual.delivery_title)
    def get_address_field(self):
        return self.driver.find_element(*Individual.address_field)
    def get_city_field(self):
        return self.driver.find_element(*Individual.city_field)
    def get_zip_field(self):
        return self.driver.find_element(*Individual.zip_field)
    def get_phone_field(self):
        return self.driver.find_element(*Individual.phone_field)
    def get_special_instructions_field(self):
        return self.driver.find_element(*Individual.special_instructions_field)
    def get_submit_button(self):
        return self.driver.find_element(*Individual.submit_button)




