# '''Задание 4
# Создайте класс «Дробь». Необходимо хранить в полях
# класса: числитель и знаменатель. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к
# отдельным полям через методы класса. Также создайте
# методы класса для выполнения арифметических операций
#  (сложение, вычитание, умножение, деление, и т.д.).'''
#
# class Fraction:
#     numerator = int()
#     denominator = int()
#     def __init__(self,number):
#         self.numerator = int(number[:number.find('/')])
#         self.denominator = int(number[number.find('/')+1:])
#
#     def __str__(self):
#         return f'{self.numerator}/{self.denominator}'
#
#     def __add__(self, other):
#         n1 = self.numerator * other.denominator
#         n2 = self.denominator * other.denominator
#         n3 = other.numerator * self.denominator
#         n4 = other.denominator * self.denominator
#         self.denominator = n2
#         self.numerator = n1 + n3
#         return f'{numerator}/{denominator}'
#
#     def decimation(self):
#         return self.numerator/self.denominator
#
#
#
# d = Fraction('11/24')
# e = Fraction('5/11')
# print(d)
# print(e)
# print(d,'+',e,'=',d+e)
# print(d)
#
#
# h = Fraction(d+e)
# print(h)
# print(h.decimation())
#
#

class Human:
    age = int()#0-135
    gender = str()#male/female
    height = int()#sm
    weight = float()#kg
    prof = str()#child
    name = str()
    surname = str()
    hp = int()
    sp = int()
    streight = int()#
    stamina = int()
    hungry = int()
    graduation = str()#/Child/ School / Colledge / Universe


    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.prof = 'child'
        self.age = 0
        __graduation = 'Child'
    def __str__(self):
        return f'Name : {self.name} Surname : {self.surname} Profession : {self.prof}'


    def change_prof(self,new_prof):
        self.prof = new_prof

    def wait_one_year(self):
        self.age = self.age + 1

    @property
    def graduation(self):
        return self.__graduation

    @graduation.setter
    def graduation(self,new_graduation):
        if self.age >= 0 and self.age <= 6 and 'Child' in new_graduation:
            self.__graduation = new_graduation
        if self.age >= 6 and self.age <= 15 and 'School' in new_graduation:
            self.__graduation = new_graduation
        if self.age >= 15 and self.age <= 20 and 'Colledge' in new_graduation:
            self.__graduation = new_graduation
        if self.age >= 18 and self.age <= 22 and 'Child' in new_graduation:
            self.__graduation = new_graduation

'''Буйлук Андрей19:25Задание 1
Создайте класс Human, который будет содержать
информацию о человеке.
С помощью механизма наследования, реализуйте класс
Builder (содержит информацию о строителе), класс Sailor
(содержит информацию о моряке), класс Pilot (содержит
информацию о летчике).
Каждый из классов должен содержать необходимые
для работы методы'''
import random
class Builder(Human):
    __position = str()#
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.prof = 'Builder'
        self.age = 18
        __graduation = random.choice(['College','Univercity'])

#bender = Builder('Bender','Rodrigez')
#print(bender)

    @property
    def position(self):
        return self.__position

#     @position.setter                  не правильно!!!!!!!!!!!!
#     def position(self,new_position):
#         if self.position = 'College' and 'Junior' in new_position:
#         self.__position = new_position
#         if self.__position = 'College' and 'Middle' in new_position:
#         self.__position = new_position
#         if self.__position = 'Univercity' and 'Middle' in new_position:
#         self.__position = new_position
#         if self.__position = 'Univercity' and 'Hard' in new_position:
#         self.__position = new_position
#
#
# bender = Builder('Bender','Rodrigez')
# print(bender)
# bender.position = 'Foreman'
# print(bender.position)