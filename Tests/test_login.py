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
    # password = password_list()

    accept_cookies = MP.get_accept_cookies_button()
    accept_cookies.click()
    return MP, LP, MPG, CS, PS, BP,ES, PK, CO, GCO, SSH, SP, TP,DR

def test_login_success(mainpage_instance):
    MP, LP, MPG, CS, PS, BP, ES, PK, CO, GCO, SSH, SP, TP, DR = mainpage_instance
    MP.get_find_my_salata_button().click()
    LP.get_signin_button().click()
    LP.get_username_field().send_keys(login_list("login1"))

    LP.get_password_field().send_keys(password_list("password1"))
    LP.get_login_button().click()
    account_name = LP.get_account_name().text
    print(account_name)
    assert account_name == "Hello Oleg"

def test_login_invalid(mainpage_instance):
    MP, LP, MPG, CS, PS, BP, ES, PK, CO, GCO, SSH, SP, TP, DR = mainpage_instance
    MP.get_find_my_salata_button().click()
    LP.get_signin_button().click()
    LP.get_username_field().send_keys(login_list("login2"))

    LP.get_password_field().send_keys(password_list("password2"))
    LP.get_login_button().click()
    LP.get_invalid_ogin_message()