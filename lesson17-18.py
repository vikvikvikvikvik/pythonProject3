l = [1, 2, 3]  # list
t = (1, 2, 3)  # tuple
d = {'a': 1, 'b': 2, 'c': 3}  # dictionary
s = {1, 2, 3, 4, 5}  # set
fs = {1, 2, 3, 4, 5}  # frozenset


#
# for element in l:
#     print(element)
#
# for i in range(len(l)):
#     print(l[i])
#
# a = [i for i in range(10)]  # inline
# print(a)
#
# n1 = 2
# command = '-'
# n2 = 2
# calc = {'+': n1 + n2, '-': n1 - n2}
# print(calc[command])
#
# l2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(l2)
# for i in range(len(l2)):
#     for j in range(len(l2[i])):
#         print(l2[i][j], end=' ')
#     print()
# print(l2[1][1])
# #
# l2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(l2)):
#     print(l2[i][0],l2[i][1],l2[i][2])
#
#
# tictactoe_board = [[1,2,3],[4,5,6],[7,8,9]]
# for y in range(9):
#     turn = int(input("Enter number of cell: "))
#     for i in range(len(tictactoe_board)):
#         for j in range(len(tictactoe_board[i])):
#             if tictactoe_board[i][j] == turn:
#                 tictactoe_board[i][j] = 'X'
#     for i in range(len(tictactoe_board)):
#         for j in range(len(tictactoe_board[i])):
#             print(tictactoe_board[i][j], end=' ')
#         print()

# s = {1, 2, 3, 4, 5}  # set
# fs = {1, 2, 3, 4, 5}  # frozenset
#
# s = set('abbbcd')
# print(s)
# s = set([1,2,3,4,5])
# print(s)
# s = set((1,2,3,4,5))
# print(s)
# s = set({'a':1,'b':2,'c':3})
# print(s)
#
# some_list = [1,3,4,3,6,4,6,3,9,4,8,0,5,3]
# print(some_list)
# some_list = list(set(some_list))
# print(some_list)
#
# some_list = [1,3,4,3,6,4,6,3,9,4,8,0,5,3]
# print(some_list.__sizeof__())
# some_list = list(set(some_list))
# print(some_list.__sizeof__())
# print(some_list)
# users = [('Andrey',12345),)('Vik',54321),('Andrey',12345)]
# users = list(set())
#


# lesson 18
# объявление функции
def hello():
    print('hello world')


# вызов функции
hello()
hello()
hello()
hello()
hello()


def hello_name(name):  # аргументы,а трибуты функции,переменные функции.
    # тело функции
    print(f"hello {name}")


hello_name('Vik')
hello_name('Kiv')
hello_name('bob')

'''Задание 1
Напишите функцию, которая отображает на экран
форматированный текст, указанный ниже:
“Don't let the noise of others' opinions
drown out your own inner voice.”
                                  Steve Jobs'''
# def steve():
#     print(f"“Don\'t let the noise of others\' opinions \ndrown out your own inner voice.” \n\t\t\t\t\t\t\t\tSteve Jobs")
# steve()

'''Задание 2
Напишите функцию, которая принимает два числа
в качестве параметра и отображает все нечетные числа
между ними.'''

# def point(q, w):
#     for i in range(q, w + 1):
#         if i % 2 != 0:
#             print(i)
#
#
# number1 = int(input("enter number : "))
# number2 = int(input("enter number : "))
# point(number1, number2)
# point(1, 11)

'''[20:32] Буйлук Андрей
Задание 4
Напишите функцию, которая возвращает максимальное из четырёх чисел. Числа передаются в качестве
параметров.
'''


def pep(a, b, c, d):
    if a >= b and a >= c and a >= d:
        print(a)
    elif b >= a and b >= c and b >= d:
        print(b)
    elif c >= a and c >= b and c >= d:
        print(c)
    elif d >= a and d >= b and d >= c:
        print(d)


pep(12, 33, 41, 11)

'''Задание 3
Напишите функцию, которая отображает горизонтальную или вертикальную линию из некоторого символа.
Функция принимает в качестве параметра: длину линии,
направление, символ.'''


def line(length, direction, symbol):
    s = ''
    while length > 0:

        if direction == 'horizontal':
            s = s + symbol
        elif direction == 'vertical':
            s = s + '\n' + symbol
        length = length - 1
    # print(s)
    return s


# line(5,'vertical','#')
a = line(24, 'horizontal', '!$')
print(a)


def summa(a, b):
    if a <= b:
        a = a + 1
        return summa
    elif b <= a:
        b = b + 1


summa(1, 5)


def summa(a, b):
    s = 0
    for i in range(a, b + 1):
        s = s + i
    return s


a = summa(1, 3)
print(a)
