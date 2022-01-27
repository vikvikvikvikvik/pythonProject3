# print("Viktor")
# print("Viktor")
# print("Viktor")
# print("Viktor")
# print("Viktor")
# print("Viktor")
# print("Viktor")
# print("Viktor")
# print("Viktor")
# print("Viktor")
# while True:
#     print("Viktor")

# flag = True
# while flag:
#     print('Something')
#     flag = False

# i = 0
# while i < 10:
#     print("Andrey")
#     i = i + 1 #инкремент i += 1
#     i = i - 1 #деремент i -= 1
#     i = i * 1 # i *= 1
#     i = i / 1 # i /= 1
#     i = (i / i) * i

# i = 0
# word = '' # если нужна \ёлочка\
# while i < 10:
#     # word = '' сли нужно что бы переменные увеличивались
#     i = i + 1
#     word = word + str(i)
#     print(word)
#

# a = 0
# b = 10
# while a =< b:
#     print(a)
#     a = a + 1

# a = 10
# b = 0
# while a >= b:
#     print(a)
#     a = a - 1

# a = 0
# b = 10
# while a <= b:
#     if a%2 != 0:
#         print(a)
#     a = a + 1

# a = 0
# b = 10
# while a <= b:
#     if a % 2 == 0:
#         print(a)
#     a = a + 1


# flake8 > linter > PEP8
# Задание 5
# Пользователь вводит с клавиатуры два числа. Нужно показать все нечетные числа в указанном диапазоне.
# Если границы диапазона указаны неправильно требуется
# произвести нормализацию границ. Например, пользователь ввел 33 и 13, требуется нормализация после которой
# начало диапазона станет равно 13, а конец 33.

# a = 33
# b = 13
# if a > b:
#     c = a
#     a = b
#     b = c
#     while a >= b:
#         if a % 2 == 0:
#             print(a)
#         a = a + 1
# elif b >= a:
#     while b >= a:
#         if b%2 != 0:
#             print(b)
#     b = b + 1

# a = 10
# b = 30
# if a > b:
#     while a >= b:
#         if b % 2 != 0:
#             print(b)
#         b = b + 1
# elif b >= a:
#     while b >= a:
#         if a % 2 != 0:
#             print(a)
#         a = a + 1

# a = 10
# b = 30
# if a > b:
#     while a >= b:
#         if b % 2 != 0:
#             print(b)
#         b = b + 1
# elif b >= a:
#     while b >= a:
#         if a % 2 != 0:
#             print(a)
#         a = a + 1

# a = 0
# b = 36
# s = 0
# while a <= b:
#     s = s + a
#     a = a + 1
# print(s)

# a = 0
# b = 6
# s = 0
# while a <= b:
#     s = s ** a
#     a = a + 1
# print(s)
#
# a = 1
# b = 10
# s = 1
# while a <= b:
#     s = s * a
#     a = a + 1
# print(s)
#
# n = 10
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
# print(factorial)

# Пользователь вводит с клавиатуры длину линии.
# Нужно отобразить на экране горизонтальную линию
# из *, указанной длины.
# Например, если было введено 7, тогда вывод на экран
# будет такой: *******.


# num = int(input("enter number : "))
# print('*' * num)
#
# a = int(input("enter number : "))
# b = 0
# while b < a:
#     print("*", end="")
#     b = b + 1
#
# l = "*"
# inp = int(input("Number"))
# while inp >= 0:
#     print(l)
#     inp = inp-1

# 4

# num = int(input("enter number : "))
# sim = str(input("enter simvol : "))
# print(sim * num)

#
# a = 10
# s = ''
# l = '&'
# while a > 0:
#     s = s + l
#     a = a - 1
# print(s)

# Guess my number
# import random
#
# secret_number = random.randint(1, 20)
# guess_number = 0
# trai = 5
# while secret_number != guess_number and trai > 0:
#     guess_number = int(input("Enter number : "))
#     trai = trai - 1
#     if secret_number < guess_number:
#         print("Your number greater than secret.")
#     elif secret_number > guess_number:
#         print("Your number less than secret.")
#     elif secret_number == guess_number:
#         print("YOU WIN")
#     if trai > 0:
#         print('retry')
#     else:
#         print('YOU LOSE')

import random

game = True
while game:
    secret_number = random.randint(1, 20)
    guess_number = 0
    lifes = 3
    money = 10
    while secret_number != guess_number and lifes > 0:
        guess_number = int(input("Enter number : "))
        lifes = lifes - 1
        print(f'You have {lifes} lifes')
        if secret_number < guess_number:
            print('Твоё число больше, чем загаданное')
            money = money - 1
        elif secret_number > guess_number:
            print('Твоё число меньше, чем загаданное')
            money = money - 1
        elif secret_number == guess_number:
            print("YOU WIN")
    if lifes > 0:
        print(f"Your balance is {lifes}")
    else:
        print('Ты проиграл:(')
        print(f"Your balance is {money}")

# work = True
# while work:
#     number1 = int(input("Enter number1 : "))
#     command = str(input("Enter operation : "))
#     number2 = int(input("Enter number2 : "))
#     if command == '+':
#         print(f'{number1} {command} {number2} = {number1 + number2}')
#     # while command == '+':
#     #     print(f'{number1} {command} {number2} = {number1 + number2}')
#     elif command == '-':
#         print(f'{number1} {command} {number2} = {number1 - number2}')
#     elif command == '*':
#         print(f'{number1} {command} {number2} = {number1 * number2}')
#     elif command == '/':
#         print(f'{number1} {command} {number2} = {number1 / number2}')
#
#     work = str(input("press any key to continue : "))
# Показать
# таблицу
# умножения
# для
# числа, введенного
# пользователем.Например, если
# пользователь
# вводит
# число
# 7, нужно
# показать:
# print(f'{number1} {command} {2} = {number1 * 2}')
# print(f'{number1} {command} {3} = {number1 * 3}')
# print(f'{number1} {command} {4} = {number1 * 4}')
# print(f'{number1} {command} {5} = {number1 * 5}')
# print(f'{number1} {command} {6} = {number1 * 6}')
# print(f'{number1} {command} {7} = {number1 * 7}')
# print(f'{number1} {command} {8} = {number1 * 8}')
# print(f'{number1} {command} {9} = {number1 * 9}')
# print(f'{number1} {command} {10} = {number1 * 10}')
# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21
# work = True
# while work:
#     number1 = int(input("Enter number1 : "))
#     command = str(input("Enter operation : "))
#     if command == '*':
#         print(f'{number1} {command} {1} = {number1 * 1}\n{number1} {command} {2} = {number1 * 2}\n{number1} {command} {3} = {number1 * 3}\n{number1} {command} {4} = {number1 * 4}\n{number1} {command} {5} = {number1 * 5}\n{number1} {command} {6} = {number1 * 6}\n{number1} {command} {7} = {number1 * 7}\n{number1} {command} {8} = {number1 * 8}\n{number1} {command} {9} = {number1 * 9}\n{number1} {command} {10} = {number1 * 10}')
#
#     num = int(input("Enter number1 : "))
#     x = 1
#     if num == 0:
#         print("ZERO")
#     while x <= 10:
#         print(f"{num} * {x} =", num * x)
#         x = x + 1

# num1 = 7
# num2 = 0
# while num1 > 0 and num2 <10:
#     print(f"{num1} * {num2} =  {num1 * num2}" )
#     num2 = num2+1