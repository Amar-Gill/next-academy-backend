import re
import random
import string

board = ['_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_']

dice = [
    'AAEEGN',
    'ELRTTY',
    'AOOTTW',
    'ABBJOO',
    'EHRTVW',
    'CIMOTU',
    'DISTTY',
    'EIOSST',
    'DELRVY',
    'ACHOPS',
    'HIMNQU',
    'EEINSU',
    'EEGHNW',
    'AFFKPS',
    'HLNNRZ',
    'DEILRX'
]


def print_board():
    # s = '  '.join(s)
    # regex = r"Q.?"
    # s = re.sub(regex, r"Qu", s)
    # print(s)

    print('  '.join(board[:4]))

    print('\n')
    print('  '.join(board[4:8]))

    print('\n')
    print('  '.join(board[8:12]))

    print('\n')
    print('  '.join(board[12:16]))

    print('\n')


def update_Qu(s):

    if s == 'Q':
        return 'Qu'
    else:
        return s


def shake():
    # letters = string.ascii_uppercase
    for i, char in enumerate(board):
        random_index = int(random.random()*len(dice))
        board[i] = dice[random_index]
        board[i] = board[i][int(random.random()*6)]
        board[i] = update_Qu(board[i])
        dice.pop(random_index)


def check_old(board, str):
    horizontal_string = ''.join(board)
    horizontal_string = horizontal_string*3

    regex = f"{str}"
    match = re.search(regex, horizontal_string)

    if match:
        print('VALID WORD')
    else:
        print('INVALID WORD')

    horizontal_string = horizontal_string[::-1]

    match = re.search(regex, horizontal_string)

    if match:
        print('VALID WORD')
    else:
        print('INVALID WORD')

    vertical_string = ''

    for i in range(4):
        vertical_string = vertical_string + ''.join(board[i::4])

    vertical_string = vertical_string*3

    match = re.search(regex, vertical_string)

    if match:
        print('VALID WORD')
    else:
        print('INVALID WORD')

    vertical_string = vertical_string[::-1]

    match = re.search(regex, vertical_string)

    if match:
        print('VALID WORD')
    else:
        print('INVALID WORD')


shake()

game_box = [
    ''.join(board[0:4]),
    ''.join(board[4:8]),
    ''.join(board[8:12]),
    ''.join(board[12:16]),
]


def check(word):
    coordinates = []
    c = word[0]
    if c == 'Q':
        c == 'Qu'
        recursion_index = 2
    else:
        recursion_index = 1
    x = 0
    y = 0
    #obtain coordinates of first char in word
    for i, row in enumerate(game_box):
        for j, char in enumerate(row):
            if c == char:
                x, y = j, i
                # print(f"{x}, {y}")
                # add to list of tuples
                coordinates.append((x,y))
                if check_4_real(x, y, word[recursion_index:], coordinates) == True:
                    return True
    return False


def check_4_real(x, y, word, coordinates*):
    if len(word) == 1:
        print('Indeed you have a valid word!')
        return True
    c = word[0]
    if c == 'Q':
        c == 'Qu'
        recursion_index = 2
    else:
        recursion_index = 1
    # check left
    if x>0:
        if game_box[y][x-1] == c and (x-1,y) not in coordinates:
            coordinates.append((x-1,y))
            check_4_real(x-1, y, word[recursion_index:])
    # check right
    if x < (len(game_box[y])-1):
        if game_box[y][x+1] == c and (x+1,y) not in coordinates:
            coordinates.append((x+1,y))
            check_4_real(x+1, y, word[recursion_index:])
    # check top
    if y>0:
        if game_box[y-1][x] == c and (x,y-1) not in coordinates:
            coordinates.append((x,y-1))
            check_4_real(x, y-1, word[recursion_index:])
    # check bottom
    if y<3:
        if game_box[y+1][x] == c and (x,y+1) not in coordinates:
            coordinates.append((x,y+1))
            check_4_real(x, y+1, word[recursion_index:])
    # check top left
    if x>0 and y>0:
        if game_box[y-1][x-1] == c and (x-1,y-1) not in coordinates:
            coordinates.append((x-1,y-1))
            check_4_real(x-1,y-1,word[recursion_index:])
    # check bottom left
    if x>0 and y<3:
        if game_box[y+1][x-1] == c and (x-1,y+1) not in coordinates:
            coordinates.append((x-1,y+1))
            check_4_real(x-1,y+1,word[recursion_index:])
    # check top right
    if x< (len(game_box[y]) - 1) and y>0:
        if game_box[y-1][x+1] == c and (x+1,y-1) not in coordinates:
            coordinates.append((x+1,y-1))
            check_4_real(x+1,y-1,word[recursion_index:])
    # check bottom right
    if x < (len(game_box[y])-1) and y < 3:
        if game_box[y+1][x+1] == c and (x+1,y+1) not in coordinates:
            coordinates.append((x+1,y+1))
            check_4_real(x+1,y+1,word[recursion_index:])

    return False

#recursion ['WORD']
# ['ORD']
# ['RD']
# ['D']
# if len word == 1, return True, else return false

print_board()
