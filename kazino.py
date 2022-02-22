import random
money = 10
game = True
while game:
    secret_number = random.randint(1, 20)
    guess_number = 0
    lifes = 4
    while secret_number != guess_number and lifes > 0:
        guess_number = int(input("Что бы победить одгадай число от 1 до 20... Пробуй : "))
        lifes = lifes - 1
        print(f'У тебя есть ещё {lifes} жизни')
        if secret_number < guess_number:
            print('Твоё число больше, чем загаданное')
            money = money - 1
        elif secret_number > guess_number:
            print('Твоё число меньше, чем загаданное')
            money = money - 1
        elif secret_number == guess_number:
            money = money + 10
            print(f"Это Победа! ВЫ потратили", 4 - lifes , "жизни")
    if lifes > 0 :
        print(f"у тебя осталось {lifes}$")
    elif lifes == 0 and secret_number != guess_number :
        print('Ты проиграл:(')
        print(f"у тебя осталось {lifes}$")
    elif  money == 0 and secret_number != guess_number:
        print('Ты проиграл:(')
        print(f"у тебя осталось {money}$")
    game = str(input("Ты победил,ещё раз? 'y' или 'n' : "))
    if game == 'n':
        game = 0
        print("Спасибо за игру!")
        end = input('Нажмите enter что бы выйти')