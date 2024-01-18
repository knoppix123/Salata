
from selenium.webdriver.common.by import By

class Dressing:

    def __init__(self, driver):
        self.driver = driver

    fresh_herb_vinagrette = (By.XPATH, "//*[contains(text(),' Fresh Herb Vinaigrette ')]")
    lemon_vinagrette = (By.XPATH, "//*[contains(text(),'Lemon Vinaigrette ')]")
    jalapeno_avocado = (By.XPATH, "//*[contains(text(),' Jalapeño Avocado ')]")
    buttermilk_ranch = (By.XPATH, "//*[contains(text(),' Buttermilk Ranch ')]")
    fat_free_tomato = (By.XPATH, "//*[contains(text(),' Fat-Free Sun-Dried Tomato')]")
    honey_mustard = (By.XPATH, "//*[contains(text(),' Honey Mustard ')]")
    ginger_lime = (By.XPATH, "//*[contains(text(),' Ginger Lime ')]")
    chipotle_ranch = (By.XPATH, "//*[contains(text(),' Chipotle Ranch')]")
    balsamic_vinagrette = (By.XPATH, "//*[contains(text(),' Balsamic Vinaigrette')]")
    lemon_juice = (By.XPATH, "//*[contains(text(),' Lemon Juice ')]")
    fat_free_mango = (By.XPATH, "//*[contains(text(),' Fat-Free Mango')]")
    classic_caesar = (By.XPATH, "//*[contains(text(),'Classic Caesar' )]")
    olive_oil = (By.XPATH, "//*[contains(text(),' Olive Oil ' )]")
    balsamic_vinegar = (By.XPATH, "//*[contains(text(),' Balsamic Vinegar ' )]")
    oil_and_vinegar = (By.XPATH, "//*[contains(text(),' Oil & Vinegar ' )]")
    next_button = (By.XPATH, "(//*[contains(text(),'Next')])")


    def get_fresh_herb_vinagrette(self):
        return self.driver.find_element(*Dressing.fresh_herb_vinagrette)
    def get_lemon_vinagrette(self):
        return self.driver.find_element(*Dressing.lemon_vinagrette)
    def get_jalapeno_avocado(self):
        return self.driver.find_element(*Dressing.jalapeno_avocado)
    def get_buttermilk_ranch(self):
        return self.driver.find_element(*Dressing.buttermilk_ranch)
    def get_fat_free_tomato(self):
        return self.driver.find_element(*Dressing.fat_free_tomato)
    def get_honey_mustard(self):
        return self.driver.find_element(*Dressing.honey_mustard)
    def get_ginger_lime(self):
        return self.driver.find_element(*Dressing.ginger_lime)
    def get_chipotle_ranch(self):
        return self.driver.find_element(*Dressing.chipotle_ranch)
    def get_balsamic_vinagrette(self):
        return self.driver.find_element(*Dressing.balsamic_vinagrette)
    def get_lemon_juice(self):
        return self.driver.find_element(*Dressing.lemon_juice)
    def get_fat_free_mango(self):
        return self.driver.find_element(*Dressing.fat_free_mango)
    def get_classic_caesar(self):
        return self.driver.find_element(*Dressing.classic_caesar)
    def get_olive_oil(self):
        return self.driver.find_element(*Dressing.olive_oil)
    def get_balsamic_vinegar(self):
        return self.driver.find_element(*Dressing.balsamic_vinegar)
    def get_oil_and_vinegar(self):
        return self.driver.find_element(*Dressing.oil_and_vinegar)
    def get_next_button(self):
        return self.driver.find_element(*Dressing.next_button)




