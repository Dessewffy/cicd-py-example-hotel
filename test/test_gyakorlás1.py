import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


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
        login_button = self.driver.find_element(By.LINK_TEXT, 'Bejelentkezés')
        login_button.click()
    
        email_input = self.driver.find_element(By.ID, 'email')
        email_input.send_keys("hogap65094@zamaneta.com")
    
        password_input = self.driver.find_element(By.ID, 'password')
        password_input.send_keys("1234")
    
        submit_button = self.driver.find_element(By.NAME, "submit")
        submit_button.click()
    
        time.sleep(1)
    
        logout_button = self.driver.find_element(By.ID, 'logout-link')
        logout_button.click()
    
    
    def test_list_task(self):
        lista = self.driver.find_element(By.XPATH,
                                         '/html/body/app-root/div/app-home/div/div/div[2]/div/form/div[3]/button[2]')
        lista.click()
        time.sleep(2)
    
        nav = self.driver.find_element(By.XPATH, '//a[text()="3"]')
        nav.click()
    
        time.sleep(1)
    
        west_city = self.driver.find_element(By.XPATH, '//h4[text()="West City Apartments Budapest - hostel"]')
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
