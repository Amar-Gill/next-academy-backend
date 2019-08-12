game_container = [
                ['_','_','_'],
                ['_','_','_'],
                ['_','_','_']
                ]

symbols = ['X','O']

game_won = False

turn = 0

def get_coordinates():
    while True:
        x_coordinate = int(input('Enter X coordinate: '))
        if x_coordinate < 0 or x_coordinate > 2:
            print()
            print('Hey that coordinate is out of the gameboard!')
            print()
        else:
            print()
            break
    while True:
        y_coordinate = int(input('Enter Y coordinate: '))
        if y_coordinate < 0 or y_coordinate > 2:
            print()
            print('Hey that coordinate is out of the gameboard!')
            print()
        else:
            print()
            break
    return x_coordinate, y_coordinate

def check_won(symbol):

    global game_won
    global turn

    unpacked_game_container = []

    for row in game_container:
        for i in range(3):
            unpacked_game_container.append(row[i])

    conditions = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6]
    ]

    for condition in conditions:
        if (unpacked_game_container[condition[0]] == symbol and unpacked_game_container[condition[1]] == symbol and unpacked_game_container[condition[2]] == symbol):
            print(f'Player {symbol} wins! Flawless Victory.')
            game_won = True
            return True

    if turn == 8:
        print('TIE GAME!')
        game_won = True
        return True
    
    return False

def tic_tac_toe(symbol):

    global game_won
    global turn

    print(f'Player {symbol} Turn')
    print('==============')
    print()

    #get input and check if coordinate within gameboard limits
    x_coordinate, y_coordinate = get_coordinates()
    print()

    #check coordinate for existing mark
    while game_container[2-y_coordinate][x_coordinate] != '_':
        print('WARNING - compilation error. self destructing in 54321')
        print()
        x_coordinate, y_coordinate = get_coordinates()

    #insert marker
    game_container[2 - y_coordinate][x_coordinate] = symbol
    print()

    #display gameboard
    print('OKAY - here is the current status of the game!')
    print()
    for row in game_container:
        print(row)
    print()

    
    #do checkwon(if checkwon = true? return true: return false)
    check_won(symbol)
    
    #increment turns
    turn += 1

    #default return value
    return False
    
while not game_won:
    for symbol in symbols:
        tic_tac_toe(symbol)
        if game_won == True:
            break

print()
print('Thanks for playing number one tic-tac-toe game!')

