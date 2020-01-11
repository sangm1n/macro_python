# simple macro practice in python by sangmin
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# window open using webdriver
driver = webdriver.Chrome()
url = "https://google.com"
driver.get(url)

# search the data
driver.find_element_by_css_selector(".gLFyf.gsfi").send_keys("python")
driver.find_element_by_css_selector(".gLFyf.gsfi").send_keys(Keys.ENTER)

# click the first data
driver.find_elements_by_css_selector(".LC20lb")[3].click()