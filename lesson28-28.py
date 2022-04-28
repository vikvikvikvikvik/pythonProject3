import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://yanigen.com.ua')
driver.get_screenshot_as_file('google.png')

home_ru = "//a[contains(text().'ГЛАВНАЯ')]"
home_ua = "//a[contains(text().'ГОЛОВНА')]"
home_en = "//a[contains(text().'HOME')"
product = "//a[contains(text().'HOME')"

a = '//li[@class="bjqs-prev"]/a[@data=direction="previous"]'
button = driver.find_element('xpath',a)
button.click()
time.sleep(5)
