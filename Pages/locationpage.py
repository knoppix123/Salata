
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys



class Localpage:

    def __init__(self, driver):
        self.driver = driver

    seachfield = (By.CSS_SELECTOR, "[id='searchField']")
    search_button = (By.XPATH, "(//*[contains(text(),'SEARCH')])[2]")
    liberty_store = (By.XPATH, "(//*[@id='restaurant-74767']//*[contains(text(),'PICKUP')])[2]")
    google_notification = (By.CSS_SELECTOR, "[class='dismissButton']")

    # arrow_date_selection_button = (By.CSS_SELECTOR, "[class='input-group-append']")
    arrow_date_selection_button = (By.XPATH, "(//*[@class='button-group'])[1]")
    arrow_time_selection_button = (By.XPATH,"(//*[@class='button-group'])[2]")
    select_12_00_time = (By.CSS_SELECTOR, "[value='12:00']")
    order_now_button = (By.XPATH, "(//*[contains(text(),'ORDER NOW')])[3]")



    def get_seachfield(self):
        return self.driver.find_element(*Localpage.seachfield)
    def get_seach_button(self):
        return self.driver.find_element(*Localpage.search_button)
    def get_liberty_store(self):
        return self.driver.find_element(*Localpage.liberty_store)
    def get_arrow_date_selection_button(self):
        return self.driver.find_element(*Localpage.arrow_date_selection_button)

    def get_order_date(self,order_date):
        return self.driver.find_element(By.XPATH, f"//*[@class='ngb-dp-month ng-star-inserted']//*[contains(text(),'{order_date}')]")
    def get_arrow_time_selection_button(self):
        return self.driver.find_element(*Localpage.arrow_time_selection_button)
    def get_select_12_00_time(self):
        return self.driver.find_element(*Localpage.select_12_00_time)
    def get_order_now_button(self):
        return self.driver.find_element(*Localpage.order_now_button)
    def get_google_notification(self):
        return self.driver.find_element(*Localpage.google_notification)

