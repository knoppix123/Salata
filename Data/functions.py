from datetime import date
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def print_today_date():
    dayselection_list = [1,2,3,4,5,6,7,]
    today = str(date.today())
    last_two_letters = today[-2:]
    last_two_letters = int(last_two_letters)
    order_date = last_two_letters + random.choice(dayselection_list)
    return order_date
        # print(last_two_letters)

def place_order(MP,LP,order_date):
    menu_button = MP.get_find_my_salata_button()
    menu_button.click()
    # time.sleep(6)
    LP.get_seachfield().clear()
    LP.get_seachfield().send_keys("30009")
    time.sleep(1)
    LP.get_seach_button().click()
    time.sleep(1)
    LP.get_liberty_store().click()
    time.sleep(1)
    LP.get_arrow_date_selection_button().click()
    LP.get_arrow_date_selection_button().click()
    time.sleep(1)
    LP.get_arrow_date_selection_button().click()
    time.sleep(1)
    LP.get_order_date(order_date).click()
    time.sleep(1)
    LP.get_arrow_time_selection_button().click()
    # time.sleep(2)
    LP.get_select_12_00_time().click()
    # time.sleep(2)
    LP.get_google_notification().click()
    # time.sleep(1)
    LP.get_order_now_button().click()
    time.sleep(2)

def finish_order(MPG,CO,GCO,MP):
    MPG.get_check_out_button_first().click()
    time.sleep(1)
    CO.get_check_out_button().click()
    time.sleep(1)
    GCO.get_firstname_field().send_keys("Oleg")
    GCO.get_lastname_field().send_keys("Chichetenko")
    GCO.get_email_field().send_keys("knoppix123@gmail.com")
    GCO.get_phone_number_field().send_keys("4077220256")
    GCO.get_next_button().click()
    time.sleep(1)
    GCO.get_next_button3().click()
    GCO.get_cc_number_field().send_keys("379145086162000")
    GCO.get_ccv_number_field().send_keys("1234")
    GCO.get_expiration_cc_field().send_keys("1228")
    GCO.get_zipzode().send_keys("32707")
    GCO.get_next_button5().click()
    time.sleep(5)
    body = MP.driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.END)
    body.send_keys(Keys.END)

    time.sleep(3)
    # GCO.get_tip_10().click()
    GCO.get_complete_order_button().click()
    time.sleep(3)

def Randomtoppinc(TP):
    toppings_selection_list = [TP.get_tomato,TP.get_cucumber, TP.get_carrots,TP.get_bell_peppers, TP.get_mushroom, TP.get_broccoli,TP.get_radish,TP.get_bean_sprouts,
                               TP.get_red_onion,TP.get_edamame,TP.get_sun_dried_tomatoes, TP.get_olives_green,TP.get_green_peas,TP.get_jalapeno,TP.get_beets,
                               TP.get_chick_peas,TP.get_black_beans]
    toppings_selection_choise = random.choice(toppings_selection_list)
    return  toppings_selection_choise()

def Randomdressing(DR):
    dressing_selection_list = [DR.get_fresh_herb_vinagrette, DR.get_lemon_vinagrette, DR.get_jalapeno_avocado,DR.get_buttermilk_ranch, DR.get_fat_free_tomato, DR.get_honey_mustard,DR.get_ginger_lime,DR.get_chipotle_ranch, DR.get_balsamic_vinagrette, DR.get_lemon_juice, DR.get_fat_free_mango, DR.get_classic_caesar,DR.get_olive_oil, DR.get_balsamic_vinegar,DR.get_oil_and_vinegar]
    dressing_selection_choise = random.choice(dressing_selection_list)
    return dressing_selection_choise()

def Fillout_delivery_information(IP,MP):
    IP.get_address_field().send_keys("7333 Avalon BLVD")
    IP.get_city_field().send_keys("Alpharetta")
    IP.get_zip_field().send_keys("30009")
    IP.get_phone_field().send_keys("1231231231")
    MP.driver.execute_script("arguments[0].value = 'your_text_here';", IP.get_special_instructions_field())
    IP.get_submit_button().click()
    MP.driver.execute_script("arguments[0].click();", IP.get_submit_button())
    time.sleep(1)






