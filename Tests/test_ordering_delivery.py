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
    GO = Grouporder(se)

    accept_cookies = MP.get_accept_cookies_button()
    accept_cookies.click()
    return MP, LP, MPG, CS, PS, BP,ES, PK, CO, GCO, SSH, SP, TP,DR, IP, TPD, GO



def test_order_delivery_individual(mainpage_instance):
    MP, LP, MPG, CS, PS, BP, ES, PK, CO, GCO, SSH, SP, TP, DR, IP, TPD, GO = mainpage_instance

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



def test_order_delivery_group(mainpage_instance):
    MP, LP, MPG, CS, PS, BP, ES, PK, CO, GCO, SSH, SP, TP, DR, IP, TPD, GO = mainpage_instance
    time.sleep(2)
    order_button = MP.get_order_now_button()
    actions = ActionChains(MP.driver)
    actions.move_to_element(order_button).perform()
    time.sleep(1)
    MP.get_group_order().click()
    time.sleep(2)

    LP.get_username_field().send_keys(login_list("login1"))
    LP.get_password_field().send_keys(password_list("password1"))
    LP.get_login_button().click()
    time.sleep(2)
    title = GO.get_group_order_title().text
    assert title == "Start your group order:"
    time.sleep(3)

#
# def test_order_delivery_group(mainpage_instance):
#     MP, LP, MPG, CS, PS, BP, ES, PK, CO, GCO, SSH, SP, TP, DR, IP, TPD, GO = mainpage_instance
















