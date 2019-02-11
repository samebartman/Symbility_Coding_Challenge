from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("/Users/samanthabartman/Desktop/chromedriver")

driver.get("https://www.amazon.ca") #driver opens Amazon.ca website
assert "Amazon" in driver.title 
time.sleep(5)
driver.close() #user will see "Hello, Sign In" in the top right corner 
#Amazon.ca page will then close