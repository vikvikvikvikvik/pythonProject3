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


'''Guess
my
number'''
import random

game = True
loose = 0
win = 0
while game:
    secret_number = random.randint(1, 20)
    guess_number = 0
    tries = 1
    while guess_number != secret_number and tries < 15:
        guess_number = int(input("Enter number : "))
        tries = tries + 1
        print(f'It is {tries} attempt')
        if tries > 5 and tries < 10:
            print("Be careful!")
            if secret_number <= 10:
                print("Number is lower then 10 ")
            elif secret_number >= 10:
                print("Number is higher then 10 ")
        if tries > 10:
            print("You almost lost, guess better!")
            if secret_number <= 5:
                print("Number is lower then 5 ")
            elif secret_number >= 5:
                print("Number is higher then 5 ")
            elif secret_number <= 10:
                print("Number is lower then 10 ")
            elif secret_number >= 10:
                print("Number is higher then 10 ")
            elif secret_number <= 15:
                print("Number is lower then 15 ")
            elif secret_number >= 15:
                print("Number is higher then 15 ")
        if secret_number < guess_number:
            print('Your number greater than secret ')
        elif secret_number > guess_number:
            print('Your number less than secret ')

    if tries == 15:
        print(f'You used {tries} attempts, and you loose!!!')
        loose += 1

    else:
        print(f'You used {tries} attempts, not bad, YOU WON!!!')
        win += 1

    print(f"You have {loose} looses, {win} wins ")
    game = str(input("You WON! Do you want to play more? Write '1', or '0' "))
    if game == '0':
        game = 0
        print("Thank you for game!")
        end = input('Please press enter to exit ')
