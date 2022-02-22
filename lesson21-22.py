# import time
# #IDE
# f = open('test.txt','wt')#t -text/ /b - binary
# f.write('My name is Vik\nHow are you?\n now? ')
# #time.sleep(15)
# f.close()
# #random.randint()
# f = open('test.txt','rt')
# print(f.read())
# f.close()
# # w - write открыть файл на запись
# # r - read  открыть файл на чтение,если он есть.если нет - ошибка.
#
# f = open('test.txt','rt')
# print(f.read())# считывет файл целиком. НЕ БЕЗОПАСЕН при больших файлах.
# f.close()
#
# f = open('test.txt','rt')
# print(f.readline())
# print(f.readline())# считывет файл построчно как итерируемый объект.
# f.close()
#
# f = open('test.txt','rt')
# print(f.readlines())#считывает файл целиком как список
# f.close()
#
#
# # w - write открыть файл на запись,если нет файла - создать. если есть, перезаписать.
# f = open('test.txt','wt')#t -text/ /b - binary
# f.write('My name is Vik\nHow are you?\n now? ')#
# s = ''''''
# f.write(s)
# f.close()


# a - add открытие файла на запись,если нет файла - создать.
# если есть файл - дописать в конец


# открыть файл на запись,если файл есть -  ошибка
# f = open('test.txt','xt')
# f.write('I am your Father,Luke')
# f.close()

# + - открытие файла на чтение и запись
# f = open('test2.txt','wt+')
# f.write('I am your Father,Luke')
# f.close()

# import random
# f = open('numbers2.txt','wt')
# for i in range(10):
#     for j in range(10):
#         f.write(str(random.randint(1,9)))
#     f.write('\n')
# f.close()

# n1 = open('numbers1.txt','rt')
# n2 = open('numbers2.txt','rt')
# n3 = open('numbers3.txt','wt')
# ln1 = n1.readline()
# ln2 = n2.readline()
# while ln1 or ln2:
#     print(ln1)
#     print(ln2)
#     n3.write(ln1)
#     n3.write(ln2)
# n3.close()

# n1 = open('numbers1.txt','rt')
# n2 = open('numbers2.txt','rt')
# n3 = open('numbers3.txt','wt')
# ln1 = n1.readline()
# ln2 = n2.readline()
# while ln1 or ln2:
#     n3.write(ln1)
#     n3.write(ln2)
#     ln1 = n1.readline()
#     ln2 = n2.readline()
# n3.close()

# lesson 22. Selenium Webdriver
# https://www.geeksforgeeks.org/web-driver-methods-in-selenium-python/
import os
import time
from selenium import webdriver

# driver = webdriver.Firefox()
# driver.get('https://chromedriver.chromium.org/downloads')
# driver.get('https://www.google.com/')
# driver.get('https://github.com/')
# driver = webdriver.Chrome()
# driver.get('https://chromedriver.chromium.org/downloads')
# driver.get('https://www.google.com/')
# driver.get('https://github.com/')
# from selenium import webdriver
# driver_path_chrome = os.getcwd() + '\chromedriver.exe'
driver_path_firefox = os.getcwd() + '\geckodriver.exe'
# driver = webdriver.Chrome(executable_path=driver_path_chrome)
# driver.get('https://chromedriver.chromium.org/downloads')
driver = webdriver.Firefox(executable_path=driver_path_firefox)
#driver.maximize_window()#окно на весь экран
#driver.set_window_size(300,100) указать размер окна.
driver.get('https://github.com/')
driver.get_screenshot_as_file('downloads.png')
time.sleep(5)
driver.get('https://chromedriver.chromium.org/downloads')
driver.get_screenshot_as_file('chromium.png')
time.sleep(5)
driver.quit()# ЗАКРЫВАЕТ БРАУЗЕР


