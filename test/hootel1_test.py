
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
        self.browser = webdriver.Chrome(options=options)

        self.browser.get(URL)
        self.browser.maximize_window()

    def teardown_method(self):
        self.browser.quit()

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

    def test_navigation(self):
        lista = self.browser.find_element(By.CLASS_NAME, "btn-outline-primary")
        assert lista.is_enabled()
        lista.click()
        time.sleep(1)

        nav = self.browser.find_element(By.XPATH, '//a[text()="2"]')
        assert nav.is_displayed()
        nav.click()

       
