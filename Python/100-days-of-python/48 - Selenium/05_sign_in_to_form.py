from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys

URL = "http://secure-retreat-92358.herokuapp.com/"
CHROME_DRIVER_PATH="C:/Users/sss/Documents/_dev/chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get(URL)
fname = driver.find_element(by="name", value="fName")
lName = driver.find_element(by="name", value="lName")
email = driver.find_element(by="name", value="email")
submit = driver.find_element(by="css selector", value=".btn.btn-lg")

fname.send_keys("Reg")
lName.send_keys("En")
email.send_keys("Bar@email.com")
submit.click()

driver.close()
driver.quit()

