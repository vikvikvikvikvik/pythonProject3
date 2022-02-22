# Два списка целых заполняются случайными числами.
# Необходимо:
# ■ Сформировать третий список, содержащий элементы
# обоих списков;1
# ■ Сформировать третий список, содержащий элементы
# обоих списков без повторений;1
# ■ Сформировать третий список, содержащий элементы
# общие для двух списков;1
# ■ Сформировать третий список, содержащий только
# уникальные элементы каждого из списков;
# ■ Сформировать третий список, содержащий только
# минимальное и максимальное значение каждого из
# списков
numbers1 = [1, 2, 3, 4, 56, 15, 112, 33, 6, 46, 73]
numbers2 = [1, 2, 3, 35, 556, 15, 112, 25, 626, 21]
numbersall = []
numbersonly = []
numbersrepit = []
numbersuni = []
numbersminmax = []
numbersall =[numbers1]+[numbers2]
print(numbersall)
numbersonly = list(set(numbersall[0]))
print(numbersonly)
numbersrepit = list(set(numbers1) & set(numbers2))
print(numbersrepit)
numbersuni = list(set(numbersall[0]))
print(numbersuni)
numbersminmax.append(min(numbers1))
numbersminmax.append(min(numbers2))
numbersminmax.append(max(numbers1))
numbersminmax.append(max(numbers2))
print(numbersminmax)