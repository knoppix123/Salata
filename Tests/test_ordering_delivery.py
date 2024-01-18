from Data.imported_list import *
from selenium.webdriver.common.action_chains import ActionChains


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
    IP = Individual(se)
    TPD = Thirdpartydelivery(se)

    accept_cookies = MP.get_accept_cookies_button()
    accept_cookies.click()
    return MP, LP, MPG, CS, PS, BP,ES, PK, CO, GCO, SSH, SP, TP,DR, IP, TPD



def test_order_delivery_individual(mainpage_instance):
    MP, LP, MPG, CS, PS, BP, ES, PK, CO, GCO, SSH, SP, TP, DR, IP, TPD = mainpage_instance

    order_button = MP.get_order_now_button()
    actions = ActionChains(MP.driver)
    actions.move_to_element(order_button).perform()
    time.sleep(1)
    MP.get_individual_order_button().click()
    time.sleep(2)
    accept_cookies = MP.get_accept_cookies_button2()
    accept_cookies.click()
    IP.get_delivery_title()
    functions.Fillout_delivery_information(IP,MP)

    title = TPD.get_third_party_delivery_title().text
    assert title == "third party delivery"
    TPD.get_calendarselection().click()
    order_date = functions.print_today_date()
    LP.get_order_date(order_date).click()
    LP.get_arrow_time_selection_button().click()
    LP.get_select_12_00_time().click()
    LP.get_order_now_button().click()












