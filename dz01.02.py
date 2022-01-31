#1
a = int(input("Enter number : "))
if a > 100 or a < 0:
    print("Error")
elif 100 > a and a > 0 and a % 3 == 0 and a % 5 == 0:
    print("Fizz Buzz")
elif 100 > a > 0 and a % 3 == 0:
    print("Fizz")
elif 100 > a > 0 and a % 5 == 0:
    print("Buzz")
else:
    print(a)

#2
a = int(input("Введите число : "))
b = int(input("Введите степень (до 7) : "))
if b == 1:
    print(a ** 1)
elif b == 2:
    print(a ** 2)
elif b == 3:
    print(a ** 3)
elif b == 4:
    print(a ** 4)
elif b == 5:
    print(a ** 5)
elif b == 6:
    print(a ** 6)
elif b == 7:
    print(a ** 7)
#3
# Life - life = 1grn
# Life - kiev = 2grn
# life - mts = 3grn
# Kiev - kiev = 1grn
# Kiev - life = 2grn
# Kiev - mts = 3 grn
# Mts - mts = 1 grn
# Mts - kiev = 3 grn
# mts - life = 3 grn
dl = int(input("Введите длительность разговора в минутах : "))
opera = int(input("Выберете своего оператора \n Life = 1\n Kievstar = 2\n Mts = 3 : "))
opera2 = int(input("Выберете своего оператора \n Life = 1\n Kievstar = 2\n Mts = 3 : "))
if opera == 1 and opera2 == 1:
    print(dl * 1,'грн за звонок')
elif opera == 1 and opera2 == 2:
    print(dl * 2,'грн за звонок')
elif opera == 1 and opera2 == 3:
    print(dl * 3,'грн за звонок')
elif opera == 2 and opera2 == 1:
    print(dl * 2,'грн за звонок')
elif opera == 2 and opera2 == 2:
    print(dl * 1,'грн за звонок')
elif opera == 2 and opera2 == 3:
    print(dl * 3,'грн за звонок')
elif opera == 3 and opera2 == 1:
    print(dl * 3,'грн за звонок')
elif opera == 3 and opera2 == 2:
    print(dl * 3,'грн за звонок')
elif opera == 3 and opera2 == 3:
    print(dl * 1,'грн за звонок')

# 4
mag1 = int(input("Введите уровень продажи : "))
mag2 = int(input("Введите уровень продажи : "))
mag3 = int(input("Введите уровень продажи : "))
if mag1 < 500:
    m1 = mag1 * 3 / 100 + 200
    print('Зарплата первого продавца =', m1)
elif 500 < mag1 < 1000:
    m1 = mag1 * 5 / 100 + 200
    print('Зарплата первого продавца =', m1)
elif mag1 > 1000:
    m1 = mag1 * 8 / 100 + 200
    print('Зарплата первого продавца =', m1)
if  mag2 < 500:
    m2 = mag2 * 3 / 100 + 200
    print('Зарплата второго продавца =', m2)
elif 500 < mag2 < 1000:
    m2 = mag2 * 5 / 100 + 200
    print('Зарплата второго продавца =', m2)
elif mag2 > 1000:
    m2 = mag2 * 8 / 100 + 200
    print('Зарплата второго продавца =', m2)
if  mag3 < 500:
    m3 = mag3 * 3 / 100 + 200
    print('Зарплата третьего продавца =', m3)
elif 500 < mag3 < 1000:
    m3 = mag3 * 5 / 100 + 200
    print('Зарплата третьего продавца =', m3)
elif mag3 > 1000:
    m3 = mag3 * 8 / 100 + 200
    print('Зарплата третьего продавца =', m3)
if m2 < m1 > m3:
    print(f'Лучший продавец №1!!!!Поздравляем с начислением премии в 200$!Его зарплата = ', m1 + 200)
elif m1 < m2 > m3:
    print(f'Лучший продавец №2!!!!Поздравляем с начислением премии в 200$!Его зарплата = ', m2 + 200)
elif m1 < m3 > m2:
    print(f'Лучший продавец №3!!!!Поздравляем с начислением премии в 200$!Его зарплата = ', m3 + 200)