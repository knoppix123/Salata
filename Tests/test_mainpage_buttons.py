import time
import pytest
from test_setup.webdriver_setup import se
from Pages.mainpage import Mainpage



@pytest.fixture
def mainpage_instance(se):
    MP = Mainpage(se)
    accept_cookies = MP.get_accept_cookies_button()
    accept_cookies.click()
    time.sleep(4)

    return MP

def test_accept_logo(mainpage_instance):
    MP =mainpage_instance
    logo = MP.get_logo()
    logo.click()
    time.sleep(5)
    title = MP.driver.title
    print(title)

def test_menu_button(mainpage_instance):
    MP = mainpage_instance
    menu_button = MP.get_menu_button()
    menu_button.click()
    title = MP.driver.title
    assert title == "Salads | Wraps | Soups | Ice Teas & Lemonade | Salata Menu"

def test_dressing_button(mainpage_instance):
    MP = mainpage_instance
    menu_button = MP.get_dressing_button()
    menu_button.click()
    title = MP.driver.title
    assert title == "Home - Salata"

def test_catering_button(mainpage_instance):
    MP = mainpage_instance
    menu_button = MP.get_catering_button()
    menu_button.click()

def test_loyalty_button(mainpage_instance):
    MP = mainpage_instance
    menu_button = MP.get_loyalty_button()
    menu_button.click()

def test_gift_cards_button(mainpage_instance):
    MP = mainpage_instance
    menu_button = MP.get_gift_cards_button()
    menu_button.click()

def test_grow_with_us_button(mainpage_instance):
    MP = mainpage_instance
    menu_button = MP.get_grow_with_us_button()
    menu_button.click()

def test_find_my_salata_button(mainpage_instance):
    MP = mainpage_instance
    menu_button = MP.get_find_my_salata_button()
    menu_button.click()

def test_order_now_button(mainpage_instance):
    MP = mainpage_instance
    menu_button = MP.get_order_now_button()
    menu_button.click()
    time.sleep(2)





