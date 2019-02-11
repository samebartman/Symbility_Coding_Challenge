from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
user = "symbilitytestscripts@gmail.com"
pwd = "abc123--"
driver = webdriver.Chrome("/Users/samanthabartman/Desktop/chromedriver")

driver.get("https://www.amazon.ca")
assert "Amazon" in driver.title
time.sleep(5)
elem = driver.find_element_by_xpath('//*[@id="nav-link-yourAccount"]')
ActionChains(driver).click(elem).perform()
time.sleep(5)
email = driver.find_element_by_name("email")
email.send_keys(user)
password = driver.find_element_by_name("password")
password.send_keys(pwd)
password.send_keys(Keys.RETURN)
time.sleep(5)
assert "No results found." not in driver.page_source
driver.close()