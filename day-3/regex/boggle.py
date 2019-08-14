import re
import random

board = ['_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_']

# board = ['A', 'B', 'C', 'D', 'E', 'Qu', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O']

coordinates = set()

word_found = False

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
    for i, char in enumerate(board):
        random_index = int(random.random()*len(dice))
        board[i] = dice[random_index]
        board[i] = board[i][int(random.random()*6)]
        board[i] = update_Qu(board[i])
        dice.pop(random_index)



shake()


game_box = [
    board[0:4],
    board[4:8],
    board[8:12],
    board[12:16]
]


def check(word):
    global word_found
    global coordinates
    c = word[0]
    if c == 'Q':
        c = 'Qu'
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
                # add to list
                check_4_real(x, y, word[recursion_index:])
                coordinates.clear()
    if word_found == False:            
        return False
    else:
        word_found = False
        return True


def check_4_real(x, y, word):
    global word_found
    global coordinates
    coordinates.add((x,y))
    #base case - termination
    if len(word) == 0:
        word_found = True
        return True
    
    c = word[0]
    if c == 'Q':
        c = 'Qu'
        recursion_index = 2
    else:
        recursion_index = 1
    # check left
    if x>0:
        if game_box[y][x-1] == c and (x-1,y) not in coordinates:
            check_4_real(x-1, y, word[recursion_index:])
    # check right
    if x <3:
        if game_box[y][x+1] == c and (x+1,y) not in coordinates:
            check_4_real(x+1, y, word[recursion_index:])
    # check top
    if y>0:
        if game_box[y-1][x] == c and (x,y-1) not in coordinates:
            check_4_real(x, y-1, word[recursion_index:])
    # check bottom
    if y<3:
        if game_box[y+1][x] == c and (x,y+1) not in coordinates:
            check_4_real(x, y+1, word[recursion_index:])
    # check top left
    if x>0 and y>0:
        if game_box[y-1][x-1] == c and (x-1,y-1) not in coordinates:
            check_4_real(x-1,y-1,word[recursion_index:])
    # check bottom left
    if x>0 and y<3:
        if game_box[y+1][x-1] == c and (x-1,y+1) not in coordinates:
            check_4_real(x-1,y+1,word[recursion_index:])
    # check top right
    if x < 3 and y>0:
        if game_box[y-1][x+1] == c and (x+1,y-1) not in coordinates:
            check_4_real(x+1,y-1,word[recursion_index:])
    # check bottom right
    if x < 3 and y < 3:
        if game_box[y+1][x+1] == c and (x+1,y+1) not in coordinates:
            check_4_real(x+1,y+1,word[recursion_index:])

    return False

print_board()
