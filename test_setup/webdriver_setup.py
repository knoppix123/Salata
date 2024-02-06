from selenium.webdriver.common.by import By
import time
import os

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def se(request):


    driver = webdriver.Chrome()
    # options = webdriver.ChromeOptions()
    # options.add_argument("--enable-javascript")
    # driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    baseurl = "https://salata.com/"
    # baseurl = "https://www.guidestar.org/"

    driver.get(baseurl)
    driver.implicitly_wait(10)

    yield driver
    driver.quit()


