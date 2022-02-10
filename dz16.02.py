# '''Задание 1
# Пользователь вводит с клавиатуры два числа. Нужно
# посчитать отдельно сумму четных, нечетных и чисел,
# кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы.'''
# x = int(input("enter number : "))
# y = int(input("enter number : "))
# chetnie = 0
# nechetnie = 0
# num9 = 0
# num1 = 0
# num2 = 0
# num3 = 0
# for i in range(x, y):
#     if i % 2 == 0:
#         chetnie = chetnie + i
#         num1 = num1 + 1
#     if i % 2 != 0:
#         nechetnie = nechetnie + i
#         num2 = num2 + 1
#     if i % 9 == 0:
#         num9 = num9 + i
#         num3 = num3 + 1
# print(chetnie,"чётные", nechetnie, "нечётные", num9, "кратные 9")
# print(chetnie / num1, nechetnie / num2, num9 / num3 )
#
# '''Задание 2
# Пользователь вводит с клавиатуры длину линии и
# символ для заполнения линии. Нужно отобразить на
# экране вертикальную линию из введенного символа,
# указанной длины.
# Например, если было введено 5 и символ %, тогда
# вывод на экран будет такой:
# %
# %
# %
# %
# %'''
# num = int(input("ввелите количество символов : "))
# sym = str(input("выберете символ : "))
# for i in range(num):
#     print (sym)

# '''Задание 3
# Пользователь вводит с клавиатуры числа. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero». Когда пользователь вводит
# число 7 программа прекращает свою работу и выводит
# на экран надпись «Good bye!»
# '''
#
# x = int(input("enter number : "))
# if x == 7:
#     print("«Good bye!»")
# elif x > 0:
#     print('Number is positive')
# elif x < 0:
#     print("Number is negative")
# elif x == 0:
#     print("Number is equal to zero")

# '''Задание 4
# Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум и минимум,
# введенных чисел. Когда пользователь вводит число 7
# программа прекращает свою работу и выводит на экран
# надпись «Good bye!»'''
# x = int(input("Enter number : "))
# y = int(input("Enter number : "))
# num = 0
# for i in range(x,y + 1):
#     if x == 7 or y == 7:
#         print("Good bye!")
#         break
#     if x >= 0 and y > x:
#         num = x + y
# print(num, "сумма")
# if x < y:
#     print(f" {x} Это число меньше число")
# if y > x:
#     print(f" {y} Это число больше большее ")