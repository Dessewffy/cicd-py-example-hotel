import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class TestHootel(object):
   
    def setup_method(self):
        URL = 'http://hotel-v3.progmasters.hu/'
        options = Options()
        options.add_experimental_option("detach", True)
       # options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(URL)
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()


    def test_checkbox_and_navigation(self):
        time.sleep(2)
        lista = self.driver.find_element(By.CLASS_NAME, "btn-outline-primary")
        lista.click()
        time.sleep(2)
    
        checks = self.driver.find_elements(By.CLASS_NAME, "form-check-input")
        for check in checks:
            check.click()
    
        delete = self.driver.find_element(By.CLASS_NAME, "badge-secondary")
        delete.click()
    
        for i, check in enumerate(checks):
            if not check.is_selected():
                print(f"Checkbox #{i + 1} nincs kiválasztva!")
    
        nav = self.driver.find_element(By.XPATH, '//a[text()="2"]')
        nav.click()
    
    
    def test_hotel_description(self):
        time.sleep(1)
        Party_szallo = self.driver.find_element(By.XPATH, '//h4[text()="Party szálló - szálloda"]')
        Party_szallo.click()
    
        time.sleep(1)
        description = self.driver.find_elements(By.TAG_NAME, "p")[1]
        print(description.text)
        length = description.text
    
        if len(length) > 500:
            print("Megfelelő hoszú!")
        else:
            print("Nem elég hosszú")
    
        features = self.driver.find_element(By.XPATH, '//ul[@class="card-text"]')
        assert features.is_displayed()
        print(features.text)
    
        time.sleep(1)
        room = self.driver.find_element(By.XPATH, '//h5[@class="card-title"]')
        assert room.text == "Project X - több ágyas szoba"
        print(room.text)
    
        time.sleep(1)
        button_warn = self.driver.find_element(By.XPATH, '//button[@class="btn btn-warning mr-4"]')
        assert button_warn.is_displayed()
        assert not button_warn.is_enabled()
        print(button_warn.text)
    
        btn_return = self.driver.find_element(By.XPATH, '//button[@class="btn btn-outline-primary"]')
        assert btn_return.is_enabled()
        print(btn_return.text)
