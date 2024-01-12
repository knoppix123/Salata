import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_setup.webdriver_setup import se
from Pages.mainpage import Mainpage
from Pages.locationpage import Localpage
from Pages.salad_selection_page import Saladselection
from Pages.ceasar_page.Ceasar_type_page import Ceasarselection
from Pages.ceasar_page.protein_page import Proteinselection
from Pages.ceasar_page.bread_page import Breadselection
from Pages.ceasar_page.extras_page import Extrasselection
from Pages.ceasar_page.plastic_kits import Plastickit
from Pages.wrap_page.base_selection_page import Selectionbase
from Pages.wrap_page.toppics_page import Toppicsselection
from Pages.check_out_page import Checkout
from Pages.guest_checkout_page import Guestcheckout
from Pages.spicy_shrimp_salad_page.spicy_shrimp_salad_type_page import  Spicyshrimsalad
from Data.functions import place_order
from Data.functions import print_today_date
from Data.functions import finish_order




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

    accept_cookies = MP.get_accept_cookies_button()
    accept_cookies.click()
    time.sleep(4)
    return MP, LP, MPG, CS, PS, BP,ES, PK, CO, GCO, SSH, SP, TP


def test_order_ceasar_salad(mainpage_instance):
    MP, LP, MPG, CS, PS, BP, ES, PK, CO, GCO, SSH, SP, TP = mainpage_instance

    body = MP.driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.PAGE_DOWN)
    order_date = print_today_date()
    place_order(MP, LP, order_date)
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
    finish_order(MPG, CO, GCO, MP)


def test_order_spicy_shrimp_salad(mainpage_instance):
    MP, LP, MPG, CS, PS, BP, ES, PK, CO, GCO, SSH, SP, TP = mainpage_instance
    order_date = print_today_date()
    place_order(MP,LP, order_date)
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
    finish_order(MPG,CO,GCO)


def test_order_wrap(mainpage_instance):
    MP, LP, MPG, CS, PS, BP, ES, PK, CO, GCO, SSH, SP, TP = mainpage_instance
    order_date = print_today_date()
    place_order(MP,LP, order_date)
    MPG.get_wrap().click()
    MPG.get_next_button().click()
    base_selection_list = [SP.get_no_base,SP.get_salata_mix,SP.get_romaine_hearts]
    base_selection_choise = random.choice(base_selection_list)
    base_selection_choise().click()
    SP.get_next_button().click()
    toppings_selection_list = [TP.get_no_toppings, TP.get_tomato,TP.get_cucumber ]
    toppings_selection_choise = random.choice(toppings_selection_list)
    toppings_selection_choise().click()
    TP.get_next_button().click()













