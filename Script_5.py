from lxml import html, etree
import csv,os,json
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
textsearch = "memory cards"
user = "hi"
pwd = "hi ;)"

from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("/Users/samanthabartman/Desktop/chromedriver")

driver.get("https://www.amazon.ca") 
assert "Amazon" in driver.title 
content = driver.page_source

doc = html.fromstring(content)
search = driver.find_element_by_id("twotabsearchtextbox")

search.send_keys(textsearch)

search.submit()
time.sleep(5)
elem = driver.find_element_by_css_selector('[data-attribute="Sandisk Ultra 32GB Class 10 SDHC UHS-I Memory Card Up to 80MB, Grey/Black (SDSDUNC-032G-GN6IN)"]')

ActionChains(driver).click(elem).perform()
elem = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
ActionChains(driver).click(elem).perform()
time.sleep(5)
elem = driver.find_element_by_xpath('//*[@id="hlb-ptc-btn-native"]')
ActionChains(driver).click(elem).perform()
time.sleep(5)
email = driver.find_element_by_name("email")
elem.send_keys(user)
password = driver.find_element_by_name("password")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()