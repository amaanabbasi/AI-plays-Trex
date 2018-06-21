from selenium import webdriver
import selenium.webdriver.common.keys as Keys 
import time 
import threading 
from capture import capture_feed # <-- user defined

driver = webdriver.Chrome()

driver.get('http://www.trex-game.skipser.com/')
time.sleep(2)

page = driver.find_element_by_id('t')
page.send_keys(u'\ue013')

capture_feed.start()

while True: 
	pass