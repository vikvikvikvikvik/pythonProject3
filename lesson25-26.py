a = int(5)
b = str('Hello')
c = list([1, 2, 3])
# 2 + 2 = 5

class Box:
    v = 5 #аргумент класса.атрибут класса.поле класс.field, переменная класса.
    #параметры класса : что? сколько? какой? существительное
    def open(self):#МЕТОД КЛАССА.method.функция класса.
        print('Open box')#глагол : что сделать?как сделать?

lanch = Box()
print(lanch.v)
lanch.open()


class Box:
    v = 5 #аргумент класса.атрибут класса.поле класс.field, переменная класса.
    #параметры класса : что? сколько? какой? существительное
    def open(self,count):#МЕТОД КЛАССА.method.функция класса.
        print(f'Open {count} box')#глагол : что сделать?как сделать?

lanch = Box()
print(lanch.v)
lanch.open(2)

tools = Box()
tools.open(5)

class Borsch:
    volume = 3
    color = 'red'
    components = ['Beetroot','Tomato','Meat','Potato']
    temperature = 20.5
    vegeterian = False
    create_date = '22/02/2022'
    life_period = 480
    def heating(self):
        self.temperature = self.temperature + 5
    def show_heating(self):
        return self.temperature
    def more_borsch(self):
        self.volume = self.volume + 1
    def show_volume(self):
        return self.volume

andrii_borsch = Borsch()
print(andrii_borsch.show_heating())
andrii_borsch.heating()
andrii_borsch.heating()
print(andrii_borsch.show_heating())
andrii_borsch.more_borsch()
andrii_borsch.more_borsch()
print(andrii_borsch.show_volume())


# Пирамида тестирования
import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as SF

driver_path_firefox = SF(os.getcwd() + '\drivers\geckodriver.exe')
driver = webdriver.Firefox(service=driver_path_firefox)
driver.maximize_window()
url = 'https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html'
driver.get(url)
q1_full_xpath = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[2]/td[3]/input'
q1 = driver.find_element('xpath',q1_full_xpath)
q1.send_keys('some')
q1_xpath = '//input[@name = "q1"]'
q9_a_full_xpath = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[2]/td[2]/input'
q9_a = driver.find_element('xpath',q9_a_full_xpath)
q9_a.click()
q9_xpath = '//input[@name = "q9" and @value = "c"]'
q19_a_full_xpath = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[3]/tbody/tr[2]/td[2]/input'
q19_a = driver.find_element('xpath',q19_a_full_xpath)
q19_a.click()
q19_xpath = '//input[@name = "q19" and value = "c"]'
q2_full_xpath = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[1]/tbody/tr[3]/td[3]/input'
q2 = driver.find_element('xpath',q2_full_xpath)
q2.send_keys('qq')
q3_xpath = '//input[@name = "q3"]'
q3c_xpath = driver.find_element('xpath',q3_xpath)
q3c_xpath.send_keys('qq')
q10_a_full_xpath = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[2]/tbody/tr[4]/td[2]/input'
q10_a = driver.find_element('xpath',q10_a_full_xpath)
q10_a.click()
q11_xpath = '//input[@name = "q11" and @value = "d"]'
q11_a = driver.find_element('xpath',q11_xpath)
q11_a.click()
q20_a_full_xpath = '/html/body/div/div/div/main/div[4]/div[2]/div/form/table[3]/tbody/tr[4]/td[2]/input'
q20_a = driver.find_element('xpath',q20_a_full_xpath)
q20_a.click()
q20_a.click()
time.sleep(3)
q20_a.click()
q21_xpath = '//input[@name = "q21" and @value = "c"]'
q21_c = driver.find_element('xpath',q21_xpath)
q21_c.click()