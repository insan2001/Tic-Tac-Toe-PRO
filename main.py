import os
from logic import win_checker
import random 

ROWS = 9
COLS = 9
symbols = {
    "SYMBOL1" : "+",
    "SYMBOL2" : "*"    
}


GAME_BOARD = [
    [" "," "," "," "," "," "," "," "," "],
    [" ","1"," "," ","2"," "," "," "," "],
    [" "," "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "," "],
    [" ","4"," "," ","5"," "," ","6"," "],
    [" "," "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "," "],
    [" ","7"," "," ","8"," "," "," "," "],
    [" "," "," "," "," "," "," "," "," "],
]

game_dict = {
    #   row*cols
    1 : [1, 1],
    2 : [1, 4],
    3 : [1, 7],
    4 : [4, 1],
    5 : [4, 4],
    6 : [4, 7],
    7 : [7, 1],
    8 : [7, 4],
    9 : [7, 7],
}

# This function will detect which place should replace in main frame (row column selector)
def r_c_selector(user_selection):
    # when -1 it correctly gives the index order of row, col
    row = (user_selection-1) // 3
    col = (user_selection-1) % 3

    # if you need real world row, column add +1 each
    return row , col

def instructions():
    print("""
    Welcome to the advance Tic Tac Toe game module
    In this game first player can choose which main
    column you would like to play first. Here is a sample

                +---+---+---+
                | 1 | 2 | 3 |
                +---+---+---+
                | 4 | 5 | 6 |
                +---+---+---+
                | 7 | 8 | 9 |
                +---+---+---+
                
    This this your main Tic Tac Toe Frame            
    only once you can decide which frame you like to play
    then the game decide the main frame depend on the previous
    player output. For instance if you play the game in the 
    middle frame first and you selected 3 the next player can only
    play in the upper right corner of the main frame or first player
    selected 8 then the other player can only play in the bottom middle
    frame.

    When a player align 3 peace in a line then the main frame will become
    non playable and that place marked for the player who align 3 peace in
    that frame. To win in this game you need to make a line in main frame.
  
    """)

def draw(gameboard):
    if not gameboard:
        GAME_BOARD =  GAME_BOARD
    else:
        GAME_BOARD =gameboard
        
    for i in range(ROWS):
        if i == 3 or i == 6:
            print("===================================")
        elif i != 0:
            print("---+---+---|---+---+---|---+---+---")

        for j in range(COLS):
            if j < 8:
                if j == 2 or j == 5:
                    print("", GAME_BOARD[i][j], end=" |")
                else:
                    print("", GAME_BOARD[i][j], end=" :")
            else:
                print("", GAME_BOARD[i][j], end="  \n")

def update(choice, player, mainframe, GAME_BOARD):
    row, col = r_c_selector(choice)
    place = game_dict[mainframe]
    main_row = place[0] + row -1
    main_col = place[1] + col -1

    if GAME_BOARD[main_row][main_col] != symbols["SYMBOL1"] and GAME_BOARD[main_row][main_col] != symbols["SYMBOL2"]:
        symbol = symbols["SYMBOL1"] if player == 1 else symbols["SYMBOL2"]
        GAME_BOARD[main_row][main_col] = symbol
        return player, GAME_BOARD, 0

    else:
        # same player will get a chance
        changed_player = 1 if player == 2 else 2
        return changed_player, GAME_BOARD, 1

# This will occupy the entire tic tac toe for the winner
def winner_fill(gameboard, mainframe, winner):
    rows, cols = r_c_selector(mainframe)
    rows += 1
    cols += 1
    start = lambda number:(number -1)*3 
    end = lambda number: number*3
    
    for row in range(start(rows), end(rows)):
        for col in range(start(cols), end(cols)):
            symbol = f"SYMBOL{winner}"
            gameboard[row][col] = symbols[symbol]
    
    return gameboard

# This will create a out line of simple tic tac toe
# [
# [1,2,3], 
# [4,5,6], 
# [7,8,9]
# ]

def box_genrator(mainframe, GAME_BOARD):
    row, col = r_c_selector(mainframe)
    row += 1
    col += 1
    start = lambda number:(number -1)*3 
    end = lambda number: number*3
    box = [GAME_BOARD[i][start(col): end(col)] for i in range(start(row), end(row))]
    return box

# [
#     [0,0,0],
#     [0,0,0],
#     [0,0,0]
# ]

def prototype(mainframe):
    _layout = [mainframe[(i-1)*3:(3*i)] for i in range(1,4)]
    print("\n")
    for i in range(3):
        if i>0:
            print("---+---+---")
        for j in range(3):
            if j < 2:
                print("", _layout[i][j], end=" |")
            else:
                print("", _layout[i][j], end=" \n")
    print("\n")

def play(player, gameboard, mainframe=0, round=1, win=[], mainframe_layout=[0,0,0,0,0,0,0,0,0]):

    draw(gameboard)

    if not mainframe:
        mainframe = int(input("Choose your main frame (1-9) >> "))

    current_player = 1 if player == 2 else 2
    sym1 = symbols["SYMBOL1"]
    sym2 = symbols["SYMBOL2"]
    
    if mainframe:
        print("Proto type of your Main TicTacToe")
        _layout = mainframe_layout.copy()
        _layout[mainframe-1] = "P"
        prototype(_layout)

    print(f"Player 1 {sym1} | Player 2 {sym2} | MainFrame : {mainframe}")

    choice = int(input(f"Player {current_player} [Choose your number(1-9)]: "))
    previous_player, GAME_BOARD, value = update(choice, current_player, mainframe, gameboard)
    box = box_genrator(mainframe, GAME_BOARD)
    turn = round - value

    # This determine the player won a box or not
    if not win_checker(box) and turn <= 81:
        os.system("cls")
        if not value and (choice not in win):
            mainframe = choice

        play(previous_player, GAME_BOARD, mainframe, turn+1, win, mainframe_layout)
        
    else:
        os.system("cls")
        print(f"Player {current_player} has won the box {mainframe} in the game")
        
        # after a player won it will scan for victory in main box
        # this is a reference for the win in main frame
        mainframe_layout[mainframe-1] = current_player

        # This will create the main frame pattern to scanable by win_checker
        game_final = [mainframe_layout[(i-1)*3:(3*i)] for i in range(1,4)]
        
        if win_checker(game_final):
            gameboard = winner_fill(GAME_BOARD, mainframe, previous_player)
            draw(gameboard)
            print(f"\nPlayer {current_player} has won the game!!!")
            prototype(mainframe_layout)
            
        elif turn == 81:
            gameboard = winner_fill(GAME_BOARD, mainframe, previous_player)
            draw(gameboard)
            print("We are running out of moves!!! Please restart the game...")
            prototype(mainframe_layout)

        else:
            gameboard = winner_fill(GAME_BOARD, mainframe, previous_player)
            win.append(mainframe)

            if not value and (choice not in win) and choice != mainframe:
                mainframe = choice

            elif choice == mainframe:
                # if the player choose the mainframe number and win the box then it stuck on the same frame
                # and can't play anymore so bypass that this will randomly select a playable frame
                print("Programe automatically choose a random box to play")
                mainframe = random.choice([i for i in range(1,10) if i not in win])

            # this have the completed boxes
            play(current_player, gameboard, mainframe, turn+1, win, mainframe_layout)

def start():
    instructions()
    select = input("Do you like to play (y/N) >> ")

    if select.lower() == "y":
        play(2, GAME_BOARD)
    else:
        print("Quiting......")
        print("Quit")

start()