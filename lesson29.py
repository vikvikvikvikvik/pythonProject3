class WashingMachine:
    model = 'Samsung'
    color = 'White'
    speed = '1000'
    depth = '60'
    height = '90'
    __weight = '60'

    def __init__(self, weight, color):
        self.weight = weight
        self.color = color

    def __add__(self, other):
        self.weight = self.weight + other.weight

    def washing(self, weight_of_clothes):
        if self.weight > weight_of_clothes:
            print('Start wash')
        elif self.weight == weight_of_clothes:
            print('lol')

    def drying(self):
        print('Start wash')

    def spining(self):
        print('Start wash')

    def __int__(self):
        print("not int")

    def __str__(self):
        return f'Weight : {self.weight}\nColor : {self.color}'

    @property
    def weight(self):
        return self.__weight


bosch = WashingMachine(20, 'Red')
noname = WashingMachine(50, 'Red')
print(bosch.weight)
print(noname.weight)
bosch + noname
print(bosch.weight)
bosch + noname
print(bosch.weight)
# print(bosch.count_of_water)
# bosch.count_of_water = 20
# print(bosch.count_of_water)
# print(bosch.color)
a = 5
s = str(bosch)
print(s)
bosch.washing(19)
# bosch.washing(20)
# bosch.washing(21)
# class O:
#     number = 0
#
#     def __init__(self, number):
#         self.number = number
#
#     def __add__(self, other):
#         self.number1 = self.number + other.number + 1
#         return self.number1
#
#     def __eq__(self, other):
#         return 'Lie'
#
#     def __str__(self):
#         return str(self.number)
#
#
# a = O(2)
# b = O(2)
# c = a + b
# print(a == b)
# print(a.number, '+', b, '=', a + b)
