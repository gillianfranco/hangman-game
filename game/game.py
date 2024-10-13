import fileHandler
from random import choice
import drawings

def play():
    words_list = list()
    file = fileHandler.open_file_reading('words.txt')
    for row in file:
        word = row.strip()
        words_list.append(word)

    drawn_word = choice(words_list)

    #For organizing
    for i in range(50):
        print()

    typed_letters = []
    corrects = []
    quantity_errors = 0

    player_name = input('Enter your name: ')

    while True:
        secret_word = drawings.print_secret_word(drawn_word, corrects)

        if secret_word == drawn_word:
            print('You won the game!')
            break

        attempt = input('\nEnter a letter: ').lower().strip()

        if attempt in typed_letters:
            print('You already used this letter!')
            continue
        else:
            typed_letters += attempt
            if attempt in drawn_word:
                corrects += attempt
            else:
                quantity_errors += 1
                print('You missed!')

        score = drawings.draw_hangman(quantity_errors)

        if quantity_errors == 6:
            print('Hanged!')
            print(f'The correct word was {drawn_word}')
            break

    fileHandler.insert_score('score.txt', player_name, score)