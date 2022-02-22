# str методы строк
# h = 'Hello World!'
# #    0123456789
# print(h)
# #строка является итерируемым типом данных / не изменяемый тип данных\byltrcbhetvfz
#
# print(h[0])
# h = h + '?'
# print(h)
# print(h[0])
# print(h[1])
# print(h[2])
# print(h[3])
# n = 'Kovalyov Viktor Aleksandrovich'
# #    123456789 10 11 12 13 14 15
# print(n[4],n[1],n[2],n[18])
# print(n[16],n[2],n[1],n[0],n[3],n[23],n[1])
# print(n[20],n[21],n[22],n[23])
# #1
# s = 'Hello World!'
# print(len(s))
# for i in range(len(s)):
#     print(s[i])
#     print(s[i-len(s)])
#     print

# #1
# rs = ''
# for i in range (len(s)):
#     rs = s[i] + rs
# print(rs)
#
# #2
# s = 'Hello World!'
# for i in range(1,len(s)+1):
#     print(s[-i])

# 3
# letters = 'abcdefghijklmnoprstuvxyz'
# number = '0123456789'
# s = 'hello123'
# count_number = 0
# count_letter = 0
# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#     for l in range(len(letters)):
#         if a == letters[l]:
#             count_letter = count_letter + 1
#     for n in range(len(number)):
#         if a == number[n]:
#             count_number = count_number + 1
# print(count_letter, count_number)


# number = '923411253123asf'
# print(number.isnumeric())
# print(number.isalpha())
# GDPR
# v2
#
# s = 'hello123'
# count_numbers = 0
# count_letters = 0
# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#     if a.isalpha():
#         count_letters = count_letters + 1
#     if a.isnumeric():
#         count_numbers = count_numbers + 1
# print(count_numbers,count_letters)


# 3[19:36] Буйлук Андрей
# Задание 3
# Пользователь вводит с клавиатуры строку и символ
# для поиска. Посчитайте сколько раз в строке встречается
# искомый символ. Полученное число выведите на экран.

# s = 'Abrakadabra'
# symbol = 'a'
# count = 0
# for i in range(len(s)):
#     if s[i] == symbol:
#         count = count + 1
# print(count)
# print(s.count(symbol))
# print(s.count(number))


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Задание 4
# Пользователь вводит с клавиатуры строку и слово
# для поиска. Посчитайте сколько раз в строке встречается
# искомое слово. Полученное число выведите на экран.
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# lesson14
# '''Задание 5
# Пользователь вводит с клавиатуры строку, слово для
# поиска, слово для замены. Произведите в строке замену
# одного слова на другое. Полученную строку отобразите
# на экране.
# * Без использования метода replace'''
#
# s = 'Abrakadabra'
# symbol = 'ra'
# new_symbol = 'RA'
# print(s.replace(symbol,new_symbol))
# print(s)

# s = 'hello123'
# print(s.isalnum())


# s = 'AbrAKaDaBRa KaDAbRAAbra'
# s = s.capitalize()
#
# print(s.lower())
# print(s.upper())
# print(s.title())
# print(s.capitalize())


'''Задание 1
Есть некоторый текст. Реализуйте следующую функциональность:
■ Изменить текст таким образом, чтобы каждое предложение начиналось
с большой буквы;
■ Посчитайте сколько раз цифры встречаются в тексте;
■ Посчитайте сколько раз знаки препинания встречаются в тексте;
■ Посчитайте количество восклицательных знаков в
тексте.'''

# symbol = 'abcdefghijklmnoprstuvxyz'
# number = '0123456789'
# spe = '!?,.'
# s = 'some interesting, text and else. what i am doing. how do you do? i am fine! thank you.'
# count_number = 0
# count_symbol = 0
# count_spe = 0
# count_spea = 0
# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#     for l in range(len(symbol)):
#         if a == symbol[l]:
#             count_symbol = count_symbol + 1
#     for n in range(len(number)):
#         if a == number[n]:
#             count_number = count_number + 1
#     for q in range(len(spe)):
#         if a == spe[q]:
#             count_spe = count_spe + 1
#         if a == spe[0]:
#             count_spea = count_spea + 1
# print(count_symbol, count_number, count_spe,count_spea)


# symbol = 'abcdefghijklmnoprstuvxyz'
# number = '0123456789'
# spe = '!?,.'
# s = 'some interesting, text and else. what i am doing. how do you do? i am fine! thank you.'
# count_number = 0
# count_symbol = 0
# count_spe = 0
# count_spea = 0
# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#     for l in range(len(symbol)):
#         if a == symbol[l]:
#             count_symbol = count_symbol + 1
#     for n in range(len(number)):
#         if a == number[n]:
#             count_number = count_number + 1
#     for q in range(len(spe)):
#         if a == spe[q]:
#             count_spe = count_spe + 1
#     if a == spe[0]:
#         count_spea = count_spea + 1
# print(count_symbol, count_number, count_spe, count_spea)
#
#
# number = '0123456789'
# spe = '!?,.'
# s = 'some interesting, text and else! what i am doing. how do you do? i am fine! thank you.'
# count_number = 0
# count_symbol = 0
# count_spe = 0
# count_spea = 0
# for i in range(len(s)):
#     print(s[i])
#     a = s[i]
#
#     if a in number:
#         count_number = count_number + 1
#     if a in spe:
#         count_spe = count_spe + 1
#     if a == spe[0]:
#         count_spea = count_spea + 1
# print(count_symbol, count_number, count_spe,count_spea)
#



# s = 'Hello World!'
# print(s[0:5])  # Hello
# print(s[-6:-1])  # World
# print(s[-6:])  # World
# print(s[:5])  # Hello
# print(s[::-1])  # !dlrow olleh
#
# t = 'some interesting, text and else. what i am doing. how do you do? i am fine! thank you.'
# t = t.capitalize()
# symbols = '!.?'
# for i in range(2, len(t)):
#     for s in range(len(symbols)):
#         print(t[i - 2:i])
#     if t[i - 2:i] == (symbols[s] + ' '):
#         print('y')
#         t = t[:i] + t[i].upper() + t[i + 1:]
#

# word = 'hello world!'
# print(word.find('l'))
# print(word.rfind('l'))
#
# x = input("enter : ")
# y = int(input("enter : "))
#
# print(x / y)