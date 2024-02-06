

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
from Pages.components.salad_selection_page import Saladselection
from Pages.components.Ceasar_type_page import Ceasarselection
from Pages.components.protein_page import Proteinselection
from Pages.components.bread_page import Breadselection
from Pages.components.extras_page import Extrasselection
from Pages.components.plastic_kits import Plastickit
from Pages.deliveries_pages.group_order_page import Grouporder
from Pages.components.base_selection_page import Selectionbase
from Pages.components.toppics_page import Toppicsselection
from Pages.check_out_page import Checkout
from Pages.deliveries_pages.individual_order_page import Individual
from Pages.deliveries_pages.third_party_delivery_page import Thirdpartydelivery
from Pages.guest_checkout_page import Guestcheckout
from Pages.components.spicy_shrimp_salad_type_page import  Spicyshrimsalad
from Pages.components.dressing_selection_page import Dressing
from Data import functions
from Data.customer_info import login_list
from Data.customer_info import password_list



