from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
user = "symbilitytestscripts@gmail.com" #username for test amazon account
pwd = "abc123--" #password for test amazon account
driver = webdriver.Chrome("/Users/samanthabartman/Desktop/chromedriver")

driver.get("https://www.amazon.ca")
assert "Amazon" in driver.title
time.sleep(5)
elem = driver.find_element_by_xpath('//*[@id="nav-link-yourAccount"]') #causes mouse to hover over Sign In CTA
ActionChains(driver).click(elem).perform() #causes mouse to click on Sign In CTA
time.sleep(5)
email = driver.find_element_by_name("email") #finds the username textbox
email.send_keys(user) #types username in textbox
password = driver.find_element_by_name("password") #finds the password textbox
password.send_keys(pwd) #types password in textbox
password.send_keys(Keys.RETURN)
time.sleep(5)
assert "No results found." not in driver.page_source
driver.close()
