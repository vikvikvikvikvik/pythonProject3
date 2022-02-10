# def simple(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# l = [1, 2, 3]
# print(l.pop())
# print(l.append(4))
#
#
# def pop(somelist):
#     return somelist.pop()
#
#
# def append(somelist, data):
#     somelist.append(data)
#
#
# l = [1, 2, 3]
# pop(l)
# append(l, 4)
# print(l)
#
#
# # Pекурсия
#
# # Return > break
# def somfunction():
#     return 'Something'
#     print("You can't see this in console")
#
#
# def calc(a, b):  # Позиционные аргументы
#     return a + b
#
#
# print(calc(2, 2))
#
#
# def calc1(a, b, c=2):  # Аргументы по умолчанию(всегда стоят после обычных)
#     return a + b + c
#
#
# print(calc1(2, 2))
#
#
#
#
# def custom_range(start,finish=False,step=False):
#     numbers = []
#     if finish:
#         if start < finish:
#             while start != finish:
#                 numbers.append(start)
#                 if step:
#                     start = start + step
#                 else:
#                     start = start + 1
#     else:
#         while 0 < start:
#             numbers.append(start)
#             start = start + 1
#     return numbers
#
# print(range(10))
# print(custom_range(10))


# def lucky(abcdef):
#     n1 = abcdef//100000
#     n2 = (abcdef//10000)%10
#     n3 = (abcdef//1000)%10
#     n4 = (abcdef // 100) % 10
#     n5 = (abcdef // 10) % 10
#     n6 = (abcdef // 1) % 10
#     if n1+n2+n3 == n4+n5+n6:
#         return True
#     else:
#         return False
# print(lucky(124421))

'''Задание 7
Напишите функцию, которая проверяет является
ли шестизначное число «счастливым». Число передаётся в качестве параметра. Если число счастливое нужно
вернуть из функции true, иначе false.
«Счастливое шестизначное число» — это число у которого сумма первых трёх цифр равна сумме трёх вторых
цифр. Например, 123420 – счастливое 1+2+3 = 4+2+0,
а 723422 – несчастливое 7+2+3 != 4+2+2.'''


# def lucky_number(number):
#     if number[0] + number[1] + number[2] == number[3] + number[4] + number[5]:
#         print('lucky')
#         return True
#     else:
#         print("Not lucky")
#         return False
# print(lucky_number('111111'))
# def nl(qwerty):
#     n1 = qwerty//100000
#     n2 = (qwerty//10000)%10
#     n3 = (qwerty//1000)%10
#     n4 = (qwerty // 100) % 10
#     n5 = (qwerty // 10) % 10
#     n6 = (qwerty // 1) % 10
#     if n1+n2+n3 == n4+n5+n6:
#         return True
#     else:
#         return False
# print(nl(123420))

def custom_range(start, finish=False, step=False):
    numbers = []
    if finish:
        if start < finish:
            while start != finish:
                numbers.append(start)
                if step:
                    start = start + step
                else:
                    start = start + 1
        elif start > finish:
            while start != finish:
                numbers.append(start)
                if step:
                    start = start + step
                else:
                    return numbers
    else:
        n = 0
        while n < start:
            numbers.append(n)
            n = n + 1
    return numbers


for i in range(1, 12, 1):
    print(i, end=' ')
print()
for i in custom_range(1, 12, 1):
    print(i, end=' ')


# Lesson 20

def average(*numbers): # название переменной аргумента может быть любой,
    # главное что бы дальше вы ссылались на него.
    count = len(numbers)
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum/count
print(average(1, 2, 3, 1234, 5, 6, 7, 8, 9, 0, 2, 4, 5))

def create_note(**notes):
    return notes
print(create_note(andrey='techer',vik='qa',alex='qc'))

a = 1
b = 14
def some():
    a = 2
    a = a * a
    print(a)
    print(b)
    print('Finish')

print(a)
some()

с = 2
def local_some():
    global c# не безопасно
    c = c + 3

local_some()
print(c)
