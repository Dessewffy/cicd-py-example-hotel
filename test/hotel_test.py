'''
http://hotel-v3.progmasters.hu/

5) Ellenőrizzük le a foglalás teljes folyamatát.
'''

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestHotel(object):
    def setup_method(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument('--headless')
        self.browser = webdriver.Chrome(options=options)
        URL = "http://hotel-v3.progmasters.hu"
        self.browser.get(URL)

    def teardown_method(self):
        pass
         self.browser.quit()

    def login(self):
        menu_toggle = WebDriverWait(self.browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@class="navbar-toggler collapsed"]')))
        menu_toggle.click()

        login_btn = WebDriverWait(self.browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@class="nav-link"]')))
        login_btn.click()

        email_input = self.browser.find_element(By.ID, 'email')
        email_input.send_keys("hogap65094@zamaneta.com")

        password_input = self.browser.find_element(By.ID, 'password')
        password_input.send_keys("1234")

        submit_btn = self.browser.find_element(By.NAME, 'submit')
        submit_btn.click()

    def test_booking(self):
        self.login()
        first_hotel = self.browser.find_element(By.XPATH, "//*[@class='card-img-top']")
        first_hotel.click()

        nrofguests = self.browser.find_element(By.ID, "numberOfGuests")
        nrofguests.send_keys(2)

        date_choose = self.browser.find_element(By.XPATH, "//input[@placeholder='Válasz időpontot!']")
        date_choose.click()

        # start_date = self.browser.find_elements(By.XPATH, "//span[@aria-label='December 22, 2023']")[1]  # Ez így nem működik, nem kattintható az elem
        # start_date.click()

        # start_date = self.browser.find_elements(By.XPATH, "//span[@aria-label='December 22, 2023']")[1]  # Adorján megoldása: tömb második eleme már kattintható
        # start_date.click()

        date_choose.send_keys(Keys.ARROW_DOWN, Keys.ENTER, Keys.ARROW_RIGHT, Keys.ENTER)


