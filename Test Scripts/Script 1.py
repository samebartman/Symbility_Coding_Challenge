from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user = ""
pwd = ""
driver = webdriver.Chrome("/Users/samanthabartman/Desktop/chromedriver")

driver.get("https://www.amazon.ca")
assert "Amazon" in driver.title
elem = driver.find_element_by_name("email")
elem.send_keys(user)
elem = driver.find_element_by_name("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()



