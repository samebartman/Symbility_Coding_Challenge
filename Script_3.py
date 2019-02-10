from lxml import html, etree
import csv,os,json
import requests
from time import sleep
from selenium import webdriver
textsearch = "memory cards"

from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("/Users/samanthabartman/Desktop/chromedriver")

driver.get("https://www.amazon.ca") 
assert "Amazon" in driver.title 
content = driver.page_source

doc = html.fromstring(content)
search = driver.find_element_by_id("twotabsearchtextbox")

search.send_keys(textsearch)

search.submit()