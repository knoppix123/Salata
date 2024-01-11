import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from test_setup.webdriver_setup import se
from Pages.mainpage import Mainpage
from Pages.locationpage import Localpage
from Pages.salad_selection_page import Saladselection
from Pages.ceasar_page.Ceasar_type_page import Ceasarselection
from Pages.ceasar_page.protein_page import Proteinselection
from Pages.ceasar_page.bread_page import Breadselection
from Pages.ceasar_page.extras_page import Extrasselection
from Pages.ceasar_page.plastic_kits import Plastickit
from Pages.check_out_page import Checkout
from Pages.guest_checkout_page import Guestcheckout

from Data import functions




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
    accept_cookies = MP.get_accept_cookies_button()
    accept_cookies.click()
    time.sleep(4)
    return MP, LP, MPG, CS, PS, BP,ES, PK, CO, GCO



def test_order(mainpage_instance):
    MP, LP, MPG, CS, PS, BP, ES, PK, CO, GCO = mainpage_instance

    body = MP.driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    order_date = functions.print_today_date()
    menu_button = MP.get_find_my_salata_button()
    menu_button.click()
    time.sleep(6)
    LP.get_seachfield().clear()
    LP.get_seachfield().send_keys("30009")
    time.sleep(1)
    LP.get_seach_button().click()
    time.sleep(2)
    LP.get_liberty_store().click()
    time.sleep(3)
    LP.get_arrow_date_selection_button().click()
    time.sleep(3)
    LP.get_order_date(order_date).click()
    time.sleep(1)
    LP.get_arrow_time_selection_button().click()
    time.sleep(2)
    LP.get_select_12_00_time().click()
    time.sleep(2)
    LP.get_google_notification().click()
    time.sleep(1)
    LP.get_order_now_button().click()
    time.sleep(2)
    MPG.get_ceasar_salad().click()
    time.sleep(1)
    MPG.get_next_button().click()
    time.sleep(3)
    CS.get_ceasar_regular_salad().click()
    time.sleep(1)
    CS.get_arrow_right().click()
    CS.get_arrow_left().click()
    quantiny = CS.get_quantiny().text
    assert quantiny == "1"
    CS.get_next_button().click()
    time.sleep(2)
    PS.get_grilled_chicken().click()
    time.sleep(1)
    PS.get_arrow_right1().click()
    time.sleep(1)
    PS.get_next_button().click()
    time.sleep(2)
    BP.get_croissant().click()
    time.sleep(1)
    BP.get_next_button().click()
    time.sleep(2)
    ES.get_avocado().click()
    time.sleep(1)
    ES.get_next_button().click()
    time.sleep(1)
    PK.get_plastic_kits().click()
    PK.get_add_to_bag().click()
    time.sleep(3)
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
    GCO.get_tip_10().click()
    time.sleep(3)
    GCO.get_complete_order_button().click()
    time.sleep(3)


















    # print(current_date)

