# # 1
# a = int(input("Enter number : "))
# b = int(input("Enter number : "))
# if a > b:
#     while a >= b:
#         if b % 7 == 0:
#             print(b)
#         b = b + 1
# elif b >= a:
#     while b >= a:
#         if a % 7 == 0:
#             print(a)
#         a = a + 1
# a = int(input("Enter number : "))
# b = int(input("Enter number : "))
# c = int(input("Enter number 1 = все числа в диапазоне 2 = все числа по убыванию 3 = все числа в поряд: "))
# for i in range(b, a, -1):
#     print(i)
# for i in range(a, b, -1):
#     print(i)
# for i in range(b, a, +1):
#     print(i)
# for i in range(a, b, +1):
#     print(i)
# if a >= b:
#     while a >= b:
#         if b % 7 == 0 or b % 5 == 0:
#             print(b)
#         b = b + 1
# elif b >= a:
#     while b >= a:
#         if a % 7 == 0 or a % 5 == 0:
#             print(a)
#         a = a + 1
# for i in range(a,b + 1):
#         if (i % 5 == 0):
#             print(i)

# 2
# a = int(input("Enter number : "))
# b = int(input("Enter number : "))
# c = int(input(
#     "введите число что бы выбрать действие \n 1 = показать все числа в диапазоне \n 2 = показать все числа по убыванию \n 3 = показать все числа кратные 7 \n 4 = показать количество цифр кратных 5: "))
# if c == 1:
#     for i in range(b, a, +1):
#         print(i)
#     for i in range(a, b, +1):
#         print(i)
# elif c == 2:
#     for i in range(b, a, -1):
#         print(i)
#     for i in range(a, b, -1):
#         print(i)
# elif c == 3:
#     for i in range(a, b + 1):
#         if i % 7 == 0:
#             print(i)
#     for i in range(b, a + 1):
#         if i % 7 == 0:
#             print(i)
# elif c == 4:
#     for i in range(a, b + 1):
#         if (i % 5 == 0):
#             print(i)
# 3
# a = int(input("Enter number : "))
# b = int(input("Enter number : "))
#
# for x in range(a, b ):
#         if x % 3 == 0 and x % 5 == 0:
#             print("Fizz Buzz")
#         elif x % 3 == 0:
#             print("Fizz")
#         elif x % 5 == 0:
#             print("Buzz")
#         else:
#             print(x)
# for x in range(b, a ):
#         if x % 3 == 0 and x % 5 == 0:
#             print("Fizz Buzz")
#         elif x % 3 == 0:
#             print("Fizz")
#         elif x % 5 == 0:
#             print("Buzz")
#         else:
#             print(x)
