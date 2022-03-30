from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
import time

def getLastActiveProduct(products):
    lastActive = None
    for product in products:
        classes = product.get_attribute("class").split(" ")
        if "enabled" in classes:
            lastActive = product
    return lastActive
def getLastActiveUpgrades(upgrades):
    lastActive = None
    for upgrade in upgrades:
        classes = upgrade.get_attribute("class").split(" ")
        if "enabled" in classes:
            lastActive = upgrade
    return lastActive

URL = "https://orteil.dashnet.org/cookieclicker/"
CHROME_DRIVER_PATH="C:/Users/sss/Documents/_dev/chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get(URL)
cookie = driver.find_element_by_id("bigCookie")

timeout = time.time() + 5
SEC_IN_MIN = 60 #60
five_min = time.time() + SEC_IN_MIN*5 # 5minutes

while True:
    cookie.click()

    if time.time() > timeout:
        products = driver.find_elements_by_css_selector("#products .product")
        upgrades = driver.find_elements_by_css_selector("#upgrades .upgrade")
        lastUpgrade = getLastActiveUpgrades(upgrades)
        lastProduct = getLastActiveProduct(products)
        if lastUpgrade is not None:
            lastUpgrade.click()
        if lastProduct is not None:
            lastProduct.click()
        timeout = time.time() + 5
        print("click")

    if time.time() > five_min:
        break
