game = True
global_player1_score = 0
global_player2_score = 0
while game:
    #Variables
    player1_choice = ''
    player2_choice = ''
    player1_score = 0
    player2_score = 0
    player1_name = str(input('Введите своё имя : '))
    player2_name = str(input('Введите своё имя : '))
    rounds = 5
    #Start of game
    for i in range(1,rounds+1):
        player1_choice = ''
        player2_choice = ''
        #Enter data
        while player1_choice != 'r' and  player1_choice != 'p' and player1_choice != 'sc' and player1_choice != 'sp' and player1_choice != 'l':
            player1_choice = str(input(f'Enter your choice {player1_name}: [r],[p],[sc],[sp],[l] : '))
        while player2_choice != 'r' and player2_choice != 'p' and player2_choice != 'sc' and player2_choice != 'sp' and player2_choice != 'l':
            player2_choice = str(input(f'Enter your choice {player2_name}: [r],[p],[sc],[sp],[l] : '))
        #Compare data
        # if player1_choice == 'r':
        #     if player2_choice == 's':
        #         print('Player 1 win the round!')
        #         player1_score = player1_score + 1
        #     elif player2_choice == 'p':
        #         print('Player 2 win the round!')
        #         player2_score = player2_score + 1
        #     else:
        #         print('Draw round')
        if player1_choice == player2_choice:
            print('Draw round')
        elif player1_choice == 'r':
            if player2_choice == 'sc':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            elif player2_choice == 'l':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            elif player1_choice == 'p':
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
            else:
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
        elif player1_choice == 'p':
            if player2_choice == 'r':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            elif player2_choice == 'sp':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            elif player2_choice == 'sc':
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
            else:
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
        elif player1_choice == 'sc':
            if player2_choice == 'p':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            elif player2_choice == 'l':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            elif player2_choice == 'r':
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
            else:
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
        elif player1_choice == 'sp':
            if player2_choice == 'r':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            elif player2_choice == 'sc':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            elif player2_choice == 'l':
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
            else:
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
        elif player1_choice == 'l':
            if player2_choice == 'p':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            elif player2_choice == 'sp':
                print(f'{player1_name} win the round!')
                player1_score = player1_score + 1
            elif player2_choice == 'r':
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
            else:
                print(f'{player2_name} win the round!')
                player2_score = player2_score + 1
    #Compare score
    if player1_score > player2_score:
        print(f'{player1_name} win the game!')
        global_player1_score = global_player1_score + 1
    elif player2_score > player1_score:
        print(f'{player2_name} win the game!')
        global_player2_score = global_player2_score + 1
    else:
        print('Draw game!')
    game = str(input("Ты победил,ещё раз? 'y' или 'n' : "))
    if game == 'n':
        game = 0
        print("Спасибо за игру!")
        end = input('Нажмите enter что бы выйти')