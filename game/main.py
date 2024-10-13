import game
import fileHandler

def show_menu():
    print('=' * 30)
    print(' ' * 8 + 'Hangman Game')
    print('=' * 30)
    print('\n1 - Play')
    print('2 - Score')
    print('3 - Leave\n')
    print('=' * 30 + '\n')

def option_validation(question, minimum, maximum):
    while True:
        try:
            option = int(input(question))
            while (option < minimum) or (option > maximum):
                option = int(input('Invalid option. Try again: '))
            break
        except ValueError:
            print('Error! Enter only integer numbers.')
    return option

score_file = 'score.txt'

if fileHandler.file_exist(score_file):
    print('The file was found.')
else:
    print("The file wasn't found.")
    fileHandler.create_file(score_file)

while True:
    show_menu()

    choose = option_validation('Enter your choose here: ', 1, 3)

    match (choose):
        case 1:
            print('Play!')
            game.play()
        case 2:
            print('Score:\n')
            data = fileHandler.list_file('score.txt')
            if not data:
                print('Score is empty')
            else:
                for row in data:
                    item = row.strip().split('; ')
                    player_name = item[0]
                    player_score = item[1]
                    print(f'Player: {player_name}; Score: {player_score}')
                print()
        case 3:
            print('\nClosing the game... See you later!')
            break