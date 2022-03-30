URL = "https://www.python.org/"

from selenium import webdriver

events = {}
CHROME_DRIVER_PATH="C:/Users/sss/Documents/_dev/chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(URL)

parent = driver.find_element_by_css_selector(".event-widget .shrubbery .menu")
LIs = parent.find_elements_by_tag_name("li")
for index, li in enumerate(LIs):
    time = li.find_element_by_tag_name("time")
    a = li.find_element_by_tag_name("a")
    events[index] = {
        "time" : time.text,
        "title" : a.text
    }
    print(time.text, a.text, index)
print(events)

for n in range(len(LIs)):
    elem = LIs[n]
    print(elem)

driver.close()
driver.quit()
