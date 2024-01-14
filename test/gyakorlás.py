#setup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

o = Options()
o.add_experimental_option("detach", True)

website_url = 'http://hotel-v3.progmasters.hu'
driver = webdriver.Chrome(options=o)
driver.get(website_url)
driver.maximize_window()
#Options.add_argument('--headless')

#script

guest_numb = driver.find_element(By.NAME,"numberOfGuests")
guest_numb.clear()
guest_numb.send_keys("3")

#Több elem egyszerre, listával lehet hivatkozni: elements[index]
user_inputs = driver.find_elements(By.TAG_NAME, 'input')
user_inputs[0].clear()
user_inputs[0].send_keys('8')

###Link text sszöveges rész alapján a partial_Link_tesxt részletekre is keres
"""login_button = driver.find_element(By.LINK_TEXT, 'Bejelentkezés')
login_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Bejelentkezés')
login_button.click()"""

#class osztály alapján, de itt a regisztrációs gomb ide tartozik, ezétz  lista kell (find_elements, index)
"""login_button1 = driver.find_elements(By.CLASS_NAME, 'nav-link')[1]
login_button1.click()

#CSS szelektorok ilyen szelektor pl.$$('a[class="nav-link"]') a dollár jelek a böngészőbe kellenek
#nekünk ez kell:a[class="nav-link"]
login_button2 = driver.find_element(By.CSS_SELECTOR, 'a[class="nav-link"]')

"""
#Belépés
login_button = driver.find_element(By.LINK_TEXT, 'Bejelentkezés')
login_button.click()


email_input = driver.find_element(By.ID, 'email')
email_input.send_keys("hogap65094@zamaneta.com")
email_input.click()

email_input = driver.find_element(By.ID, 'password')
email_input.send_keys("1234")
email_input.click()

Button = driver.find_element(By.NAME, "submit")
Button.click()

#Legyen idő betölteni a kilépés gombot
time.sleep(1)
loguot = driver.find_element(By.ID, 'logout-link')
loguot.click()


#Lista feladat
lista = driver.find_element(By.XPATH, '/html/body/app-root/div/app-home/div/div/div[2]/div/form/div[3]/button[2]')
lista.click()
time.sleep(2)

nav = driver.find_element(By.XPATH, '//a[text()="3"]')
nav.click()

time.sleep(1)
west_city = driver.find_element(By.XPATH, '//h4[text()="West City Apartments Budapest - hostel"]')
west_city.click()

time.sleep(2)
check = driver.find_elements(By.TAG_NAME, "ul")[1]
print(check.text)

features = ["Parkolási lehetőség (Fizetős)", "Azonnali visszaigazolás", "Ingyenes WIFI", "Légkondícionálás", "Ingyenes WIFI"]

if all(feature in check.text for feature in features):
    print("Minden elem megtalálható.")
    driver.quit()
else:
    print("Nem található meg az összes elem.")






