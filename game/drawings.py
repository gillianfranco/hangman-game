def print_secret_word(word, corrects):
    secret_word = ''
    for letter in word:
        if letter in corrects:
            secret_word += letter
        else:
            secret_word += '\u2588'
    print(f'Guess ({len(word) - len(corrects)} letters): ')
    for letter in secret_word:
        print(f'{letter} ', end='')
    print()

    return secret_word

def draw_hangman(quantity_errors):
    score = 1000

    print('X==:==')
    print('X  :  ')
    if quantity_errors >= 1:
        print('X  0  ')
        score = 800
    else:
        print('X')

    row2 = ''
    if quantity_errors == 2:
        row2 = '  |  '
        score = 600
    elif quantity_errors == 3:
        row2 = ' /|  '
        score = 400
    elif quantity_errors >= 4:
        row2 = ' /|\ '
        score = 200

    print(f'X{row2}')

    row3 = ''
    if quantity_errors == 5:
        row3 = ' / '
        score = 100
    elif quantity_errors >= 6:
        row3 = ' / \ '
        score = 0

    print(f'X{row3}')

    print(f'X\n=======')

    return score