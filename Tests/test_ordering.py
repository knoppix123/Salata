from Data.imported_list import *


@pytest.fixture
def mainpage_instance(se):
    MP = Mainpage(se)
    LP = Localpage(se)
    MPG = Saladselection(se)
    CS = Ceasarselection(se)
    PS = Proteinselection(se)
    BP = Breadselection(se)
    ES = Extrasselection(se)
    PK = Plastickit(se)
    CO = Checkout(se)
    GCO = Guestcheckout(se)
    SSH = Spicyshrimsalad(se)
    SP = Selectionbase(se)
    TP = Toppicsselection(se)
    DR = Dressing(se)

    accept_cookies = MP.get_accept_cookies_button()
    accept_cookies.click()
    return MP, LP, MPG, CS, PS, BP,ES, PK, CO, GCO, SSH, SP, TP,DR



def test_order_ceasar_salad(mainpage_instance):
    MP, LP, MPG, CS, PS, BP, ES, PK, CO, GCO, SSH, SP, TP, DR = mainpage_instance

    body = MP.driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.PAGE_DOWN)
    order_date = functions.print_today_date()
    functions.place_order(MP, LP, order_date)
    MPG.get_ceasar_salad().click()
    MPG.get_next_button().click()
    CS.get_ceasar_regular_salad().click()
    CS.get_arrow_right().click()
    CS.get_arrow_left().click()
    quantiny = CS.get_quantiny().text
    assert quantiny == "1"
    CS.get_next_button().click()
    PS.get_grilled_chicken().click()
    PS.get_arrow_right1().click()
    PS.get_next_button().click()
    BP.get_croissant().click()
    BP.get_next_button().click()
    ES.get_avocado().click()
    ES.get_next_button().click()
    PK.get_no_plastic_kits().click()
    PK.get_add_to_bag().click()
    functions.finish_order(MPG, CO, GCO, MP)


def test_order_spicy_shrimp_salad(mainpage_instance):
    MP, LP, MPG, CS, PS, BP, ES, PK, CO, GCO, SSH, SP, TP, DR = mainpage_instance
    order_date = functions.print_today_date()
    functions.place_order(MP,LP, order_date)
    MPG.get_spicy_shrimp_salad().click()
    MPG.get_next_button().click()
    SSH.get_small_spicy_salad().click()
    SSH.get_next_button().click()
    BP.get_croissant().click()
    BP.get_next_button().click()
    ES.get_artichoke().click()
    ES.get_next_button().click()
    PK.get_no_plastic_kits().click()
    PK.get_add_to_bag().click()
    functions.finish_order(MPG,CO,GCO,MP)


def test_order_wrap(mainpage_instance):
    MP, LP, MPG, CS, PS, BP, ES, PK, CO, GCO, SSH, SP, TP, DR = mainpage_instance
    order_date = functions.print_today_date()
    functions.place_order(MP,LP, order_date)
    MPG.get_wrap().click()
    MPG.get_next_button().click()
    SP.get_salata_mix().click()
    SP.get_next_button().click()

    time.sleep(2)
    MP.driver.execute_script("arguments[0].click();", functions.Randomtoppinc(TP))
    MP.driver.execute_script("arguments[0].click();", functions.Randomtoppinc(TP))
    MP.driver.execute_script("arguments[0].click();", functions.Randomtoppinc(TP))
    MP.driver.execute_script("arguments[0].click();", functions.Randomtoppinc(TP))
    time.sleep(2)
    TP.get_next_button().click()
    time.sleep(2)
    MP.driver.execute_script("arguments[0].click();", functions.Randomdressing(DR))
    MP.driver.execute_script("arguments[0].click();", functions.Randomdressing(DR))
    DR.get_next_button().click()
    time.sleep(2)
    MP.driver.execute_script("arguments[0].click();", PS.get_grilled_chicken())
    PS.get_next_button().click()
    BP.get_cool_cucumber().click()
    BP.get_next_button().click()
    BP.get_croissant().click()
    BP.get_next_button().click()
    ES.get_avocado().click()
    ES.get_next_button().click()
    PK.get_no_plastic_kits().click()
    PK.get_add_to_bag().click()

    time.sleep(2)






















