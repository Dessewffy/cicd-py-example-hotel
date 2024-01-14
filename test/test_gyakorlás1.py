import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestHootel(object):
    def setup_method(self):
        URL = 'http://hotel-v3.progmasters.hu/'
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(URL)
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_guest_number_input(self):
        guest_numb = self.driver.find_element(By.NAME, "numberOfGuests")
        guest_numb.clear()
        guest_numb.send_keys("3")

    def test_user_inputs(self):

        user_inputs = self.driver.find_elements(By.TAG_NAME, 'input')
        user_inputs[0].clear()
        user_inputs[0].send_keys('8')

    def test_login_and_logout(self):
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
        time.sleep(1)

        logout_btn = self.browser.find_element(By.ID, 'logout-link')

        assert logout_btn.text == "Kilépés"

    def test_list_task(self):
        lista = self.driver.find_element(By.XPATH,
                                         '/html/body/app-root/div/app-home/div/div/div[2]/div/form/div[3]/button[2]')
        lista.click()
        time.sleep(2)

        nav = self.driver.find_element(By.XPATH, '//a[text()="3"]')
        nav.click()

        time.sleep(1)

        west_city = self.driver.find_element(By.XPATH, '//h4[text()="NAPFÉNY APARTMAN - apartman"]')
        west_city.click()

        time.sleep(2)

        check = self.driver.find_elements(By.TAG_NAME, "ul")[1]
        print(check.text)

        features = ["Parkolási lehetőség (Fizetős)", "Azonnali visszaigazolás", "Ingyenes WIFI", "Légkondícionálás",
                    "Ingyenes WIFI"]

        if all(feature in check.text for feature in features):
            print("Minden elem megtalálható.")
        else:
            print("Nem található meg az összes elem.")

