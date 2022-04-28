from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://yanigen.com.ua/')
time.sleep(5)
driver.maximize_window()