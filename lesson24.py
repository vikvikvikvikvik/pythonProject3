import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as SF
from selenium.webdriver.chrome.service import Service as SC
driver_path_chrome = SC(os.getcwd() + '\drivers\chromedriver.exe')
driver_path_firefox = SF(os.getcwd() + '\drivers\geckodriver.exe')
driver = webdriver.Firefox(service=driver_path_firefox)
url = 'https://www.google.com/'
driver.get(url)
driver.set_window_position(0,0)# для второго монитора расположеного справа.
time.sleep(2)
driver.maximize_window()

#HEADLESS bezgolovii
# driver.get(url)
# print(driver.title)
# button_18_50_xpath = '/html/body/div[2]/main/cach/div[1]/div/div/div[2]/div/button[2]'
# button_51_60_xpath = '/html/body/div[2]/main/cach/div[1]/div/div/div[2]/div/button[3]'
# button_start = driver.find_element('xpath',button_18_50)
# button_start.click()
# print(button_start.text)
url = 'https://test.mensa.no/'
driver.get(url)
print(driver.title)
button_18_50_xpath = '/html/body/div[2]/main/cach/div[1]/div/div/div[2]/div/button[2]'
button_51_60_xpath = '/html/body/div[2]/main/cach/div[1]/div/div/div[2]/div/button[3]'
button_51_60 = driver.find_element('xpath',button_51_60_xpath)
print(button_51_60.text)
button_18_50 = driver.find_element('xpath',button_18_50_xpath)
print(button_18_50.text)
time.sleep(2)
button_18_50.click()
button_start_xpath = '//*[@id="startTest"]'
button_start_xpath_full = '/html/body/div[2]/main/cach/div[2]/div/div/div/div[2]/button'
button_start = driver.find_element('xpath',button_start_xpath_full)
time.sleep(2)
button_start.click()
ex1_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex1 = driver.find_element('xpath',ex1_a_xpath)
button_ex1.click()
ex2_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[2]/div[3]/div[2]/div/img'
button_ex2 = driver.find_element('xpath',ex2_a_xpath)
button_ex2.click()
ex3_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[3]/div[3]/div[3]/div/img'
button_ex3 = driver.find_element('xpath',ex3_a_xpath)
button_ex3.click()
time.sleep(6)
ex4_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[4]/div[3]/div[4]/div/img'
button_ex4 = driver.find_element('xpath',ex4_a_xpath)
button_ex4.click()
time.sleep(6)
ex5_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[5]/div[3]/div[4]/div/img'
button_ex5 = driver.find_element('xpath',ex5_a_xpath)
button_ex5.click()
time.sleep(6)
ex6_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[6]/div[3]/div[4]/div/img'
button_ex6 = driver.find_element('xpath',ex6_a_xpath)
button_ex6.click()
time.sleep(6)
ex7_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[7]/div[3]/div[1]/div/img'
button_ex7 = driver.find_element('xpath',ex7_a_xpath)
button_ex7.click()
time.sleep(6)
ex8_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[8]/div[3]/div[1]/div/img'
button_ex8 = driver.find_element('xpath',ex8_a_xpath)
button_ex8.click()
ex9_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex9 = driver.find_element('xpath',ex9_a_xpath)
button_ex9.click()
ex10_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex10 = driver.find_element('xpath',ex10_a_xpath)
button_ex10.click()
ex11_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex11 = driver.find_element('xpath',ex11_a_xpath)
button_ex11.click()
ex12_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex12 = driver.find_element('xpath',ex12_a_xpath)
button_ex12.click()
ex13_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[3]/div[3]/div[3]/div/img'
button_ex13 = driver.find_element('xpath',ex13_a_xpath)
button_ex13.click()
ex14_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex14 = driver.find_element('xpath',ex14_a_xpath)
button_ex14.click()
ex15_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex15_= driver.find_element('xpath',ex15_a_xpath)
button_ex15_click()
ex16_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[3]/div[3]/div[3]/div/img'
button_ex16 = driver.find_element('xpath',ex16_a_xpath)
button_ex16.click()
ex17_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex17 = driver.find_element('xpath',ex17_a_xpath)
button_ex17.click()
ex18_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex18 = driver.find_element('xpath',ex18_a_xpath)
button_ex18.click()
ex19_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex19 = driver.find_element('xpath',ex19_a_xpath)
button_ex19.click()
ex20_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[3]/div[3]/div[3]/div/img'
button_ex20 = driver.find_element('xpath',ex20_a_xpath)
button_ex20.click()
ex21_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex21 = driver.find_element('xpath',ex21_a_xpath)
button_ex21.click()
ex22_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex22 = driver.find_element('xpath',ex22_a_xpath)
button_ex22.click()
ex23_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex23 = driver.find_element('xpath',ex23_a_xpath)
button_ex23.click()
ex24_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[3]/div[3]/div[3]/div/img'
button_ex24 = driver.find_element('xpath',ex24_a_xpath)
button_ex24.click()
ex25_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex25 = driver.find_element('xpath',ex25_a_xpath)
button_ex25_click()
ex26_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[3]/div[3]/div[3]/div/img'
button_ex26 = driver.find_element('xpath',ex26_a_xpath)
button_ex26_click()
ex27_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex27 = driver.find_element('xpath',ex27_a_xpath)
button_ex27_click()
ex28_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex28 = driver.find_element('xpath',ex28_a_xpath)
button_ex28_click()
ex29_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[3]/div[3]/div[3]/div/img'
button_ex29 = driver.find_element('xpath',ex29_a_xpath)
button_ex29_click()
ex30_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex30 = driver.find_element('xpath',ex30_a_xpath)
button_ex30_click()
ex31_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[3]/div[3]/div[3]/div/img'
button_ex31 = driver.find_element('xpath',ex31_a_xpath)
button_ex31_click()
ex32_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex32 = driver.find_element('xpath',ex32_a_xpath)
button_ex32_click()
ex33_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex33 = driver.find_element('xpath',ex33_a_xpath)
button_ex33_click()
ex34_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex34 = driver.find_element('xpath',ex34_a_xpath)
button_ex34_click()
ex35_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[1]/div[3]/div[1]/div/img'
button_ex35 = driver.find_element('xpath',ex35_a_xpath)
button_ex35_click()
ex36_a_xpath = '/html/body/div[2]/main/cach/div[3]/div[3]/div[3]/div[3]/div/img'
button_ex36 = driver.find_element('xpath',ex36_a_xpath)
button_ex36_click()

#2