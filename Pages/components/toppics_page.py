
from selenium.webdriver.common.by import By

class Toppicsselection:

    def __init__(self, driver):
        self.driver = driver

    no_toppings = (By.XPATH, "(//*[contains(text(),'No toppings')])")
    tomato = (By.XPATH, "(//*[contains(text(),' Tomato ')])")
    cucumber = (By.XPATH, "//*[contains(text(),'Cucumber')]")
    carrots = (By.XPATH, "//*[contains(text(),'Carrots')]")
    bell_peppers = (By.XPATH, "//*[contains(text(),'Bell Peppers')]")
    mushroom = (By.XPATH, "//*[contains(text(),'Mushroom')]")
    broccoli = (By.XPATH, "//*[contains(text(),'Broccoli')]")
    radish = (By.XPATH, "//*[contains(text(),'Radish')]")
    bean_sprouts  = (By.XPATH, "//*[contains(text(),'Bean Sprouts ')]")
    red_onion = (By.XPATH, "//*[contains(text(),'Red Onion')]")
    edamame = (By.XPATH, "//*[contains(text(),'Edamame')]")
    sun_dried_tomatoes = (By.XPATH, "//*[contains(text(),'Sun-Dried Tomatoes')]")
    olives_black = (By.XPATH, "//*[contains(text(),'Olives - Black')]")
    corn = (By.XPATH, "//*[contains(text(),'Corn')]")
    cilantro = (By.XPATH, "//*[contains(text(),'Cilantro')]")
    olives_green = (By.XPATH, "//*[contains(text(),'Olives - Green')]")
    green_peas = (By.XPATH, "//*[contains(text(),'Green Peas')]")
    jalapeno = (By.XPATH, "//*[contains(text(),'Jalapeno')]")
    beets= (By.XPATH, "//*[contains(text(),'Beets')]")
    chick_peas = (By.XPATH, "//*[contains(text(),'Chick Peas')]")
    black_beans = (By.XPATH, "//*[contains(text(),'Black Beans')]")
    next_button = (By.XPATH, "(//*[contains(text(),'Next')])")


    def get_no_toppings(self):
        return self.driver.find_element(*Toppicsselection.no_toppings)
    def get_tomato(self):
        return self.driver.find_element(*Toppicsselection.tomato)
    def get_cucumber(self):
        return self.driver.find_element(*Toppicsselection.cucumber)
    def get_carrots(self):
        return self.driver.find_element(*Toppicsselection.carrots)
    def get_bell_peppers(self):
        return self.driver.find_element(*Toppicsselection.bell_peppers)
    def get_mushroom(self):
        return self.driver.find_element(*Toppicsselection.mushroom)
    def get_broccoli(self):
        return self.driver.find_element(*Toppicsselection.broccoli)
    def get_radish(self):
        return self.driver.find_element(*Toppicsselection.radish)
    def get_bean_sprouts(self):
        return self.driver.find_element(*Toppicsselection.bean_sprouts)
    def get_red_onion(self):
        return self.driver.find_element(*Toppicsselection.red_onion)
    def get_edamame(self):
        return self.driver.find_element(*Toppicsselection.edamame)
    def get_sun_dried_tomatoes(self):
        return self.driver.find_element(*Toppicsselection.sun_dried_tomatoes)
    def get_olives_green(self):
        return self.driver.find_element(*Toppicsselection.olives_green)
    def get_green_peas(self):
        return self.driver.find_element(*Toppicsselection.green_peas)
    def get_jalapeno(self):
        return self.driver.find_element(*Toppicsselection.jalapeno)
    def get_beets(self):
        return self.driver.find_element(*Toppicsselection.beets)
    def get_chick_peas(self):
        return self.driver.find_element(*Toppicsselection.chick_peas)
    def get_black_beans(self):
        return self.driver.find_element(*Toppicsselection.black_beans)

    def get_next_button(self):
        return self.driver.find_element(*Toppicsselection.next_button)





