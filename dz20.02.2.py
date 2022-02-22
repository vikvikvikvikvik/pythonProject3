# Задание 1:
# Пользователь вводит с клавиатуры арифметическое
# выражение. Например, 23+12.
# Необходимо вывести на экран результат выражения.
# В нашем примере это 35. Арифметическое выражение
# может состоять только из трёх частей: число, операция,
# число. Возможные операции: +, -,*,/
#

#variant1

num = list(input("введите выражение например (1+9).числа должны быть не больше 10 : "))
if num[1] == "+":
    print(int(num[0]) + int(num[2]))
elif num[1] == "-":
    print(int(num[0]) - int(num[2]))
elif num[1] == "*":
    print(int(num[0]) * int(num[2]))
elif num[1] == "/":
    print(int(num[0]) / int(num[2]))


#variant2
example = str(input('enter number : '))
e_list = []
if example[0] == '-':
  if '+' in example[1:]:
    e_list = example[1:].split('+')
    e_list.insert(1,'+')
  elif '-' in example[1:]:
    e_list = example[1:].split('-')
    e_list.insert(1,'-')
  elif '*' in example[1:]:
    e_list = example[1:].split('*')
    e_list.insert(1,'*')
  elif '/' in example[1:]:
    e_list = example[1:].split('/')
    e_list.insert(1,'/')
  e_list[0] = int(e_list[0])
  e_list[2] = int(e_list[2])
  e_list[0] = e_list[0] * (-1)
else:
  if '+' in example:
    e_list = example.split('+')
    e_list.insert(1,'+')
  elif '-' in example:
    e_list = example.split('-')
    e_list.insert(1,'-')
  elif '*' in example:
    e_list = example.split('*')
    e_list.insert(1,'*')
  elif '/' in example:
    e_list = example.split('/')
    e_list.insert(1,'/')
  e_list[0] = int(e_list[0])
  e_list[2] = int(e_list[2])

d = {'+':e_list[0] + e_list[2],'-':e_list[0] - e_list[2],'*':e_list[0] * e_list[2],'/':e_list[0] / e_list[2]}
result = d[e_list[1]]
print(result)

# Задание 2:
# В списке целых, заполненном случайными числами,
# определить минимальный и максимальный элементы,
# посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать
# количество нулей. Результаты вывести на экран.


numbers = [0,124,5,1,5,1,5,-2,15,0,0,-1,-11,66,16]
min = 0
max = 0
neg = 0
pos = 0
zer = 0
for number in numbers:
    if number < min:
        min = number
    elif number > max:
        max = number
    elif number < 0:
        neg = neg + 1
    elif number > 0:
        pos = pos + 1
    elif number == 0:
        zer = zer + 1
print(f"min = {min}, max = {max}, neg = {neg}, pos = {pos}, zer = {zer}")
