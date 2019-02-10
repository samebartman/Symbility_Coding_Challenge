from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("/Users/samanthabartman/Desktop/chromedriver")

driver.get("https://www.amazon.ca") #driver opens Amazon.ca website
assert "Amazon" in driver.title 
driver.close() #user will see "Hello, Sign In" in the top right corner 
#Amazon.ca page will then close