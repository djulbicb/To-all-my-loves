# install chrome
# https://www.google.com/chrome/
# chromedriver. Version dots>help>about google chrome
# https://chromedriver.chromium.org/downloads
# unzip and move to somewhere

# BeutifulSoup is bad for angular, react. You wait for loading.

from selenium import webdriver
CHROME_DRIVER_PATH="C:/Users/sss/Documents/_dev/chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
# on mac: Settings > Security & Privacy > Allow chromederiver
driver.get("https://www.amazon.com")
element = driver.find_element_by_id("nav-cart-text-container")
driver.find_element_by_name("nave-of-form-field")
print(element.text)
print(element.tag_name) # kog je tipa tag
print(element.get_attribute("placeholder")) # vrednost atributa

logo = driver.find_element_by_class_name("python-logo")
print(logo.size)

driver.find_element_by_css_selector(".documentation .test")
driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# u html konzoli stranice, right click on element copy xpath
driver.close() # closes tab
driver.quit() # closes browser