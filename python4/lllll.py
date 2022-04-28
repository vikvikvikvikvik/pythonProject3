# my_list =  ['Mary', 'had', 'a', 'little', 'lamb']
#
#
# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'
#
#
# print(my_list(my_list))
#
#
# s = '23+12'
# number1 = ''
# number2 = ''
# symb = ['+', '-', '*', '/']
#
# for i in range(len(s)):
#     n = s[i]
#     for j in symb:
#         if n == j:
#             number1 = s[:i]
#             number2 = s[i + 1:]
#             mark = n
# if mark == '+':
#     print(number1, '+', number2, '=', int(number1) + int(number2))
# elif mark == '-':
#     print(number1, '-', number2, '=', int(number1) - int(number2))
# elif mark == '*':
#     print(number1, '*', number2, '=', int(number1) * int(number2))
# elif mark == '/':
#     print(number1, '/', number2, '=', int(number1) / int(number2))
#
# #Variables
# a = str(input("Input some impression: "))
# operators = ['+', '-', '*', '/']
# operator = 0
# operator_index = 0
# # Cycle for enumerating type of operator
# for i in a:
#     for b in operators:
#         if b == i:
#             operator = b
#             break
# # Enumerating operator's index
# operator_index = a.index(operator)
# # Calculating and printing results
# if operator == "+":
#     print(int(a[:operator_index]) + int(a[operator_index+1:]))
# elif operator == "-":
#     print(int(a[:operator_index]) - int(a[operator_index+1:]))
# elif operator == "*":
#     print(int(a[:operator_index]) * int(a[operator_index+1:]))
# elif operator == "/":
#     print(int(a[:operator_index]) / int(a[operator_index+1:]))
# else:
#     print("You input something wrong! ")

my_tuple[1] = my_tuple[1] + my_tuple[0]

