'''cписок масивов *д'''

'''list список(масив) * двусвязанный список (тип хранения в памяти)
итерируемый тип данных\изменяемый тип данных\ индексируемый'''

# l = [1,2,3.3,True,False,'FFF']
# l = []
# l = list()
# fruits = ['Apple','Pear','Peach','Mellon','Pineapple','Grape']#SPISOK
# print(fruits[0])#Apple
# print(fruits[-1])#Grape
# print(fruits[3])#Mellon
# print(fruits[0:3])#Apple,PEar,Peach
# print(fruits)
# fruits[0]= 'Pineapple'
# print(fruits)
# print(fruits[0])
# fruits[4]='Apple'
# fruits[5]='Tomato'
# fruits[2]='Avokado'
# print(fruits)
# colors = ['Red','Green','Blue']
# print(colors)
# colors.append('Orange')#add to the end of list
# print(colors)
# colors = colors[::-1]
# print(colors)
# colors.append('Yellow')
# print(colors)
# colors = colors[::-1]
# print(colors)


# colors = ['Red','Green','Blue']
# print(colors)
# colors.append('Orange')#add to the end of list
# print(colors)
# colors.insert(2,'Yellow')# добавить в конкретное место. номер места,аргумент.
# print(colors)
# colors.pop(0)# удалить по индексу.
# print(colors.pop(0))
# print(colors)
# #del colors# удалить обсалютно всё.
# #print(colors)
# colors.remove('Yellow')
# print(colors)
# print('Purple'in colors)#False
# print(len(colors))
# new_colors = colors
# print(colors)
# print(new_colors)
# colors.append('Pink')
# print(colors)
# print(new_colors)
# new_colors.append('Cyan')
# print(colors)
# print(new_colors)
# real_colors = colors[:]
# print(colors)
# print(real_colors)
# real_colors.pop(0)
# colors.pop()
# print(colors)
# print(real_colors)
# '''[19:35] Буйлук Андрей
# Задание 1
# В списке целых, заполненном случайными числами
# вычислить:
# ■ Сумму отрицательных чисел;
# ■ Сумму четных чисел;
# ■ Сумму нечетных чисел;
# ■ Произведение элементов с индексами кратными 3;
# ■ Произведение элементов между минимальным и
# максимальным элементом;
# ■ Сумму элементов, находящихся между первым и последним положительными элементами.
#
# '''
# numbers = [1, 2, 3, 4, 5, -1, -1, 9, 3, 22, 22, 31]
# sum_neg = 0
# sum_even = 0
# sum_odd = 0
# for number in numbers:
#     if number < 0:
#         sum_neg = sum_neg + number
#     if number % 2 == 0 and number != 0:
#         sum_even = sum_even + number
#     elif number % 2 == 0 and number != 0:
#         sum_odd = sum_odd + number
# print(sum_neg,sum_odd,sum_even)
# print(0%2)
# mult_3 = 1
# mult_min_max  = 1
# minimum = numbers[0]
# maximum = numbers[0]
# for index in range(len(numbers)):
#     if index % 3 == 0 and index != 0:
#         mult_3 = mult_3 * numbers[index]
#     if minimum > numbers[index]:
#         minimum = numbers[index]
#         minimum_index = index
#     if maximum < numbers[index]:
#         maximum = numbers[index]
#         maximum_index = index
# mult_numbers = []
# if maximum_index < minimum_index:
#     mult_numbers = numbers[maximum_index:minimum_index+1]
# else:
#     mult_numbers = numbers[minimum_index:maximum_index+1]
# for number in mult_numbers:
#         mult_min_max = mult_min_max * number
# print(mult_min_max)

'''LESSON 16'''

# tuple/dict
# list = []
# tuple = (,)
# dict = {}
# tuple кортеж (массив)
# итерируемый тип данных \ не изменяемый тип данных \ индексируемый.
# не изменяемый список:
bucket = ('Tomato', 'Bread', 'Butter')
# a = 2
# b = 3
# a,b = b,a
# print(a,b)
a = [1]
b = [2]
c = [3]
trio = (a, b, c)
print(trio)
a[0] = 10
b[0] = 22
c[0] = 0
print(trio)

# dict словарь (массив)
# итерируемый тип данных \  изменяемый тип данных \ключ значение
countries = {'Ukraine': 'Kiev', 'Poland': 'Warshava'}
d = {0: 'Viktor', True: 'Forever', 'k': 3}
#'''список не может быть ключём.
# Ключ - любой не изменяемый тип данных:значение - любой тип данных'''
print(d)
# print(d['a'])
# d['a'] = 'Never'
# print(d['a'])
# d['a'] = ['Never','Forever']
# print(d)
d['b'] = 'abc'#add
print(d)
d.pop('k')#delete
print(d)
#d.popitem()
print(d.keys())
print(d.values())
