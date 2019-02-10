from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
user = "hi"
pwd = "hi ;)"
driver = webdriver.Chrome("/Users/samanthabartman/Desktop/chromedriver")

driver.get("https://www.amazon.ca")
assert "Amazon" in driver.title


elem = driver.find_element_by_xpath('//*[@id="nav-link-yourAccount"]')
ActionChains(driver).click(elem).perform()
time.sleep(5)
elem = driver.find_element_by_name("email")
elem.send_keys(user)
elem = driver.find_element_by_name("password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()