import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest
import allure
import random

from selenium.webdriver.support.wait import WebDriverWait as EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestHootel(object):
    def setup_method(self):
        URL = 'http://hotel-v3.progmasters.hu/'
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        options.add_argument('--headless')
        self.driver.get(URL)
        self.driver.maximize_window()

    def teardown_method(self):
         self.driver.quit()
       

    @pytest.mark.parametrize('email, password', [('hogap65094@zamaneta.com', '1234')])
    @allure.title("Hootel Login")
    @allure.description("A belépés tesztelése")
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.tag("login")
    def test_login(self, email, password):
        menu_toggle = WebDriverWait(self.browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@class="navbar-toggler collapsed"]')))
        menu_toggle.click()

        login_btn = WebDriverWait(self.browser, 5).until(
           EC.element_to_be_clickable((By.XPATH, '//a[@class="nav-link"]')))
        login_btn.click()

        email_input = self.browser.find_element(By.ID, 'email')
        email_input.send_keys(email)

        password_input = self.browser.find_element(By.ID, 'password')
        password_input.send_keys(password)

        submit_btn = self.browser.find_element(By.NAME, 'submit')
        submit_btn.click()
        time.sleep(1)

        logout_btn = self.browser.find_element(By.ID, 'logout-link')

        assert logout_btn.text == "Kilépés"

    @pytest.mark.parametrize('email, password', [('hogap65094@zamaneta.com', '1234')])
    def test_booking_one_day(self, email, password):
        # Belépés
        self.test_login(email, password)

        # Hotel lista és hotel random kiválasztása
        hotel_list = self.driver.find_element(By.XPATH, '//button[@class="btn btn-outline-primary btn-block"]')
        hotel_list.is_displayed()
        hotel_list.click()

        time.sleep(1)
        random_numb = random.randint(1, 9)
        hotel = self.driver.find_elements(By.XPATH, '//h4[@style="cursor: pointer"]')[random_numb]
        hotels_list = self.driver.find_elements(By.XPATH, '//h4[@style="cursor: pointer"]')
        assert len(hotels_list) == 10
        hotel.click()

        # Foglalás
        number_of_guest = self.driver.find_element(By.ID, 'numberOfGuests')
        number_of_guest.send_keys("1")

        time.sleep(1)
        datum = self.driver.find_element(By.XPATH, '//*[@id="bookingDateRange"]/div/input')
        datum.click()

        time.sleep(1)
        datum_choose = self.driver.find_elements(By.XPATH, '//span[@aria-label="December 18, 2023"]')[2]
        datum_choose.click()

        datum_choose2 = self.driver.find_elements(By.XPATH, '//span[@aria-label="December 21, 2023"]')[2]
        datum_choose2.click()

        time.sleep(1)
        check_box = self.driver.find_element(By.XPATH, '//label[@class="ng-star-inserted"]')
        check_box.click()

        time.sleep(2)
        booking_btn = self.driver.find_element(By.XPATH, '//button[@class="btn btn-warning mr-4"]')
        booking_btn.click()

        time.sleep(1)
        aszf = self.driver.find_element(By.XPATH, '//input[@formcontrolname="aSZF"]')
        aszf.click()

        payment_btn = self.driver.find_element(By.XPATH, '//button[@class="btn btn-primary mr-4"]')
        payment_btn.click()

        # Sikeres foglalás ellenőrzése
        time.sleep(3)
        check_booking = self.driver.find_element(By.XPATH, '//div[@class="modal-body"]/h5')
        assert check_booking.text == "Gratulálunk! Sikeres foglalás!"
