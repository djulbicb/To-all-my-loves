from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"
CHROME_DRIVER_PATH="C:/Users/sss/Documents/_dev/chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(URL)

article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)

# Click on element
# link_portals = driver.find_element_by_link_text("All portals")
# link_portals.click()

# Search for something
search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.close()
driver.quit()