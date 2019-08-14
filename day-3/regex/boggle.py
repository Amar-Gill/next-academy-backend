import re
import random

# initialize a list of size 16 to easily get random letters from dice
board = ['_', '_', '_', '_', '_', '_', '_',
         '_', '_', '_', '_', '_', '_', '_', '_', '_']

# this board is for testing purposes only
# board = ['A', 'B', 'C', 'D', 'E', 'Qu', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O']

#global set of coordinates to use during recursive word checking
coordinates = set()

#global variable to use in check function
word_found = False

#dice for random letters
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

#function to show board
def print_board():

    print('  '.join(board[:4]))

    print('\n')
    print('  '.join(board[4:8]))

    print('\n')
    print('  '.join(board[8:12]))

    print('\n')
    print('  '.join(board[12:16]))

    print('\n')

#function to change input letter s if==Q to Qu
def update_Qu(s):
    if s == 'Q':
        return 'Qu'
    else:
        return s


def shake():
    for i, char in enumerate(board):
        #get random number to select a dice from dice list
        random_index = int(random.random()*len(dice))
        #set the board at index i to the full dice string at random index
        board[i] = dice[random_index]
        #change board[i] to a random character within the string
        board[i] = board[i][int(random.random()*6)]
        #check if board[i] is Q and change to Qu
        board[i] = update_Qu(board[i])
        #remove the dice that was selected from list of dice
        dice.pop(random_index)



shake()

#require a list size 4 containing lists also size 4 for check algorithm
game_box = [
    board[0:4],
    board[4:8],
    board[8:12],
    board[12:16]
]


def check(word):
    global word_found
    global coordinates
    #c is first character in word, if Q, c=Qu
    #check function will accept the the input word minus c by way of splicing
    #therefore recursion index = 2 if c=Qu, else recursion_index = 1
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
                #now that we have x,y coordinates of first character
                #we can recursively search nearby squares for successive letters
                #function takes string argument of input word less character c
                check_4_real(x, y, word[recursion_index:])
                #once recursion is complete, clear coordinates set for next word
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
    #if input string is '', reached end of a valid word, return True
    if len(word) == 0:
        #change global variable to control output at bottom of recursive stack
        word_found = True
        return True
    
    #char to search for is first character of input string
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
