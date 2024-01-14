'''
http://hotel-v3.progmasters.hu/

1) Navigáljunk el a hotelek listájához.
2) Ellenőrozzük le a checkboxok működését: mindet kattintsuk be, majd a "Szoba szolgáltatás szűrések törlése" gombra kattintva távolítsuk el a kiválaszott szolgáltatásokat, és ellenőrizzük is le, hogy megtörtént.
3) Navigáljunk el egy tetszőleges hotel oldalára.
4) Írjuk ki a terminálra a hosszú leírását.
5) Ellenőrizzük le egy elágazással, hogy a hosszú leírás 500 karakternél hosszabb-e (kapjunk róla visszajelzést a terminálon).
6) Jelentkezzünk be az oldalra. Ellenőrizzük le, hogy a bejelentkezés megtörtént.
7) Vizsgáljuk meg, hogy a felhasználónknak van-e korábbi, vagy jelenleg aktuális foglalása.

'''
# setup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

o = Options()
o.add_experimental_option("detach", True)

website_url = 'http://hotel-v3.progmasters.hu/'
driver = webdriver.Chrome(options=o)
driver.get(website_url)
driver.maximize_window()

# script
time.sleep(2)
lista = driver.find_element(By.CLASS_NAME, "btn-outline-primary")
lista.click()
time.sleep(2)

checks = driver.find_elements(By.CLASS_NAME, "form-check-input")
for check in checks:
    check.click()
"""Checkboxok kipipálása és ennek ellenőrzése"""
delete = driver.find_element(By.CLASS_NAME, "badge-secondary")
delete.click()

for i, check in enumerate(checks):
    if not check.is_selected():
        print(f"Checkbox #{i+1} nincs kiválasztva!")

"""Elnavigálás egy hotel oldalához és leírás printelése/ellenőrzése"""
nav = driver.find_element(By.XPATH, '//a[text()="2"]')
nav.click()

time.sleep(1)
Party_szallo = driver.find_element(By.XPATH, '//h4[text()="Party szálló - szálloda"]')
Party_szallo.click()

time.sleep(1)
description = driver.find_elements(By.TAG_NAME, "p")[1]
print(description.text)
length = description.text

if len(length) > 500:
    print("Megfelelő hoszú!")
else:
    print("Nem elég hosszú")


features = driver.find_element(By.XPATH, '//ul[@class="card-text"]')
assert features.is_displayed()
print(features.text)

time.sleep(1)
room = driver.find_element(By.XPATH, '//h5[@class="card-title"]')
assert room.text == "Project X - több ágyas szoba"
print(room.text)

time.sleep(1)
button_warn = driver.find_element(By.XPATH, '//button[@class="btn btn-warning mr-4"]')
assert button_warn.is_displayed()
assert not button_warn.is_enabled()
print(button_warn.text)

btn_return = driver.find_element(By.XPATH, '//button[@class="btn btn-outline-primary"]')
assert btn_return.is_enabled()
print(btn_return.text)



"""

# Belépés 
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

# Sikeres belépés ellenőrzése
time.sleep(1)
loguot = driver.find_element(By.ID, 'logout-link')
text = loguot.text
if text == "Kilépés":
    print("Ki tudnál lépni, tehát be tudtál lépni!")
else:
    print("Valami nem stimmel")

#Foglalás ellenőrzése
ancor = driver.find_element(By.ID, 'user-bookings')
ancor.click()

time.sleep(1)
try:
    div_element = driver.find_element(By.CLASS_NAME, 'no-gutters')

    if div_element.find_elements(By.XPATH, ".//*"):
        print("Már van foglalás.")


except NoSuchElementException:
    print("Nincs foglalásom")
"""
