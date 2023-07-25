#_______________________            WELCOME TO TIC TAC TOE GAME             _____________________________#
#_______________________                       BY                           _____________________________#
#_______________________          MOHAMMED AHSAN WAKIR (FA22-BCT-001)       _____________________________#
#_______________________                ABDULLAH (FA22-BCT-004)             _____________________________#
 
#                      THE MIGHTY CODE STARTS FROM HEREヾ(⌐■_■)ノ♪
#______________________________________________________

# WE IMPORTED THE GRID OF THE GAME AND THE TOSS OF THE GAME BELOW.
from  Grid import printing_board
from  Toss import cointoss
# THE CHOICE OF SYMBOL BETWEEN THE COMPUTER AND THE USER.
def choosing_symbol():
    global symbol1; global symbol2
    symbol=0
    while symbol not in ["X","O"]:
        symbol=input("Choose the Symbol, 'X' or 'O': ").upper()
        if symbol=="X":
            symbol1="X"
            symbol2="O"
        elif symbol=="O":
            symbol1="O"
            symbol2="X"
        # SYMBOL 1 IS FOR USER AND SYMBOL2 IS FOR COMPUTER
        else:
            print("Invalid input. Please enter again.")
# LIST FOR BOARD
def board():
    global board
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    
    return (board)

# WE ARE GETTING THE INPUT FROM THE USER IN NUMERIC VALUES HERE AND THE NUMERIC VALUES ARE BEING CONVERTED INTO SYMBOLS.
def player_input(board):
    global player
    numbers=["1","2","3","4","5","6","7","8","9"]
    player=0
    while player not in numbers:
        
        player=input("Enter the number of the cell you want to place your cross, 1-9:\n")    
        
        if player=="1" and board[0][0]==" ":
            board[0][0]=symbol1
        elif player=="2" and board[0][1]==" ":
            board[0][1]=symbol1
        elif player=="3" and board[0][2]==" ":
            board[0][2]=symbol1
        elif player=="4" and board[1][0]==" ":
            board[1][0]=symbol1
        elif player=="5" and board[1][1]==" ":
            board[1][1]=symbol1
        elif player=="6" and board[1][2]==" ":
            board[1][2]=symbol1
        elif player=="7" and board[2][0]==" ":
            board[2][0]=symbol1
        elif player=="8" and board[2][1]==" ":
            board[2][1]=symbol1
        elif player=="9" and board[2][2]==" ":
            board[2][2]=symbol1
        else:
            print("Invalid number. Enter again.")
            player="0"

# ALL THE MOVES BY THE COMPUTER.
def computer_moves(board):
    # WINNING MOVES FOR THE COMPUTER______________________________________________________
    # WIN AT ROWS.
    if board[0][0] == board[0][1] == symbol2 and board[0][2]==" ":
        board[0][2] = symbol2
    elif board[0][1] == board[0][2] == symbol2 and board[0][0]==" ":
        board[0][0] = symbol2
    elif board[0][0] == board[0][2] == symbol2 and board[0][1]==" ":
        board[0][1] = symbol2

    elif board[1][0] == board[1][1] == symbol2 and board[1][2]==" ":
        board[1][2] = symbol2
    elif board[1][0] == board[1][2] == symbol2 and board[1][1]==" ":
        board[1][1] = symbol2
    elif board[1][1] == board[1][2] == symbol2 and board[1][0]==" ":
        board[1][0] = symbol2

    elif board[2][0] == board[2][1] == symbol2 and board[2][2]==" ":
        board[2][2] = symbol2
    elif board[2][0] == board[2][2] == symbol2 and board[2][1]==" ":
        board[2][1] = symbol2
    elif board[2][1] == board[2][2] == symbol2 and board[2][0]==" ":
        board[2][0] = symbol2

    # WIN AT COLUMNS.
    elif board[0][0] == board[1][0] == symbol2 and board[2][0]==" ":
        board[2][0] = symbol2
    elif board[0][0] == board[2][0] == symbol2 and board[1][0]==" ":
        board[1][0] = symbol2
    elif board[1][0] == board[2][0] == symbol2 and board[0][0]==" ":
        board[0][0] = symbol2

    elif board[0][1] == board[1][1] == symbol2 and board[2][1]==" ":
        board[2][1] = symbol2
    elif board[0][1] == board[2][1] == symbol2 and board[1][1]==" ":
        board[1][1] = symbol2
    elif board[0][1] == board[2][1] == symbol2 and board[1][1]==" ":
        board[1][1] = symbol2

    elif board[1][1] == board[2][1] == symbol2 and board[0][1]==" ":
        board[0][1] = symbol2

    elif board[0][2] == board[1][2] == symbol2 and board[2][2]==" ":
        board[2][2] = symbol2
    elif board[0][2] == board[2][2] == symbol2 and board[1][2]==" ":
        board[1][2] = symbol2
    elif board[1][2] == board[2][2] == symbol2 and board[0][2]==" ":
        board[0][2] = symbol2
    # WIN AT DIAGONALS
    elif board[0][0] == board[1][1] == symbol2 and board[2][2]==" ":
        board[2][2] = symbol2
    elif board[0][0] == board[2][2] == symbol2 and board[1][1]==" ":
        board[1][1] = symbol2
    elif board[1][1] == board[2][2] == symbol2 and board[0][0]==" ":
        board[0][0] = symbol2

    elif board[0][2] == board[1][1] == symbol2 and board[2][0]==" ":
        board[2][0] = symbol2
    elif board[1][1] == board[2][0] == symbol2 and board[0][2]==" ":
        board[0][2] = symbol2
    elif board[0][2] == board[2][0] == symbol2 and board[1][1]==" ":
        board[1][1] = symbol2

# COUNTER MOVES BY COMPUTER TO THE USER____________________________________________________
# COUNTER AT ROWS
    elif board[0][0] == board[0][1] == symbol1  and board[0][2]==" ":
        board[0][2] = symbol2
    elif board[0][1] == board[0][2] == symbol1  and board[0][0]==" ":
        board[0][0] = symbol2
    elif board[0][0] == board[0][2] == symbol1  and board[0][1]==" ":
        board[0][1] = symbol2

    elif board[1][0] == board[1][1] == symbol1  and board[1][2]==" ":
        board[1][2] = symbol2
    elif board[1][0] == board[1][2] == symbol1  and board[1][1]==" ":
        board[1][1] = symbol2
    elif board[1][1] == board[1][2] == symbol1  and board[1][0]==" ":
        board[1][0] = symbol2

    elif board[2][0] == board[2][1] == symbol1  and board[2][2]==" ":
        board[2][2] = symbol2
    elif board[2][0] == board[2][2] == symbol1  and board[2][1]==" ":
        board[2][1] = symbol2
    elif board[2][1] == board[2][2] == symbol1  and board[2][0]==" ":
        board[2][0] = symbol2

# COUNTER AT COLUMN
    elif board[0][0] == board[1][0] == symbol1  and board[2][0]==" ":
        board[2][0] = symbol2
    elif board[0][0] == board[2][0] == symbol1  and board[1][0]==" ":
        board[1][0] = symbol2
    elif board[1][0] == board[2][0] == symbol1  and board[0][0]==" ":
        board[0][0] = symbol2

    elif board[0][1] == board[1][1] == symbol1  and board[2][1]==" ":
        board[2][1] = symbol2
    elif board[0][1] == board[2][1] == symbol1  and board[1][1]==" ":
        board[1][1] = symbol2
    elif board[0][1] == board[2][1] == symbol1  and board[1][1]==" ":
        board[1][1] = symbol2

    elif board[1][1] == board[2][1] == symbol1  and board[0][1]==" ":
        board[0][1] = symbol2

    elif board[0][2] == board[1][2] == symbol1  and board[2][2]==" ":
        board[2][2] = symbol2
    elif board[0][2] == board[2][2] == symbol1  and board[1][2]==" ":
        board[1][2] = symbol2
    elif board[1][2] == board[2][2] == symbol1  and board[0][2]==" ":
        board[0][2] = symbol2
# COUNTER AT DIAGONALS
    elif board[0][0] == board[1][1] == symbol1  and board[2][2]==" ":
        board[2][2] = symbol2
    elif board[0][0] == board[2][2] == symbol1  and board[1][1]==" ":
        board[1][1] = symbol2
    elif board[1][1] == board[2][2] == symbol1  and board[0][0]==" ":
        board[0][0] = symbol2

    elif board[0][2] == board[1][1] == symbol1  and board[2][0]==" ":
        board[2][0] = symbol2
    elif board[1][1] == board[2][0] == symbol1  and board[0][2]==" ":
        board[0][2] = symbol2
    elif board[0][2] == board[2][0] == symbol1  and board[1][1]==" ":
        board[1][1] = symbol2
#------------------------------------------------------------------------
   
# COUNTER AT CENTER.
    elif board[1][1]==" ":
        board[1][1] = symbol2
# COUNTER FOR TRICK MOVES.
    elif board[1][2]==symbol1 and board[2][2]==" ":
        board[2][2]=symbol2
    elif board[1][0]==symbol1 and board[2][1]==" ":
        board[2][1]=symbol2
# COUNTER AT EDGES.
    elif board[0][0]==board[2][2]==symbol1 and board[0][1]==" ":
        board[0][1] = symbol2
    elif board[0][2]==board[2][0]==symbol1 and board[0][1]==" ":
        board[0][1] = symbol2
# RANDOM MOVES BY THE COMPUTER AT FIRST MOVE.
    elif board[0][0]==" ":
        board[0][0] = symbol2
    elif board[0][2]==" ":
        board[0][2] = symbol2
    elif board[2][0]==" ":
        board[2][0] = symbol2
    elif board[2][2]==" ":
        board[2][2] = symbol2
    elif board[0][1]==" ":
        board[0][1] = symbol2
    elif board[1][0]==" ":
        board[1][0] = symbol2
    elif board[1][2]==" ":
        board[1][2] = symbol2
    elif board[2][1]==" ":
        board[2][1] = symbol2

    else:
        print("Its going through else")

# CONDITIONS FOR WIN AND DRAW.
def check_win(board):

    symbols=[symbol1, symbol2]

    if board[0][0]==board[0][1]==board[0][2] and board[0][0]!=" ":
        if board[0][0]==symbol1:
            print(f"{name1} won!")
            return True        
        else:
            print(f"{name2} won!")
            return True
    elif board[1][0]==board[1][1]==board[1][2] and board[1][0]!=" ":
        if board[1][0]==symbol1:
            print(f"{name1} won!")
            return True
        else:
            print(f"{name2} won!")
            return True
    elif board[2][0]==board[2][1]==board[2][2] and board[2][0]!=" ":
        if board[2][0]==symbol1:
            print(f"{name1} won!")
            return True
        else:
            print(f"{name2} won!")
            return True
    elif board[0][0]==board[1][0]==board[2][0] and board[0][0]!=" ":
        if board[0][0]==symbol1:
            print(f"{name1} won!")
            return True
        else:
            print(f"{name2} won!")
            return True
    elif board[0][1]==board[1][1]==board[2][1] and board[0][1]!=" ":
        if board[0][1]==symbol1:
            print(f"{name1} won!")
            return True
        else:
            print(f"{name2} won!")
            return True
    elif board[0][2]==board[1][2]==board[2][2] and board[0][2]!=" ":
        if board[0][2]==symbol1:
            print(f"{name1} won!")
            return True
        else:
            print(f"{name2} won!")
            return True
    elif board[0][0]==board[1][1]==board[2][2] and board[0][0]!=" ":
        if board[0][0]==symbol1:
            print(f"{name1} won!")
            return True
        else:
            print(f"{name2} won!")
            return True
    elif board[0][2]==board[1][1]==board[2][0] and board[0][2]!=" ":
        if board[0][2]==symbol1:
            print(f"{name1} won!")
            return True
        else:
            print(f"{name2} won!")
            return True

    
    elif board[0][0] in symbols and board[0][1] in symbols and board[0][2] in symbols and\
        board[1][0] in symbols and board[1][1] in symbols and board[1][2] in symbols and\
        board[2][0] in symbols and board[2][1] in symbols and board[2][2] in symbols:

        print("Game is a draw")
        return True

#_________________ GAME STARTING POINT ___________________#
print("_______________________________________________________________________________________________________________\n")
print("                                             Welcome to The Game                                                 ")
print("                                                 Tic-Tac-Toe                                                     ")
print("_______________________________________________________________________________________________________________\n")

name=input("Please enter your name:\n")
if name=="":
    name1="you"
else:
    name1=name
name2="Computer"

game_repetition="Y"
board()
while game_repetition=="Y":
    
    printing_board(board)
    choosing_symbol()
    user_turn = cointoss()
    if user_turn==True:
        print("You won the toss. Go for the first move")

    else:
        print("Computer won the toss. Computer goes for the first move")
    while True:
        if user_turn == True:
            player_input(board)
            printing_board(board)
            #check_win(board)
            if check_win(board)==True:
                break 
            else:
                user_turn=False
        else:
            computer_moves(board)
            printing_board(board)
            #check_win(board)
            if check_win(board)==True:
                break
            else:
                user_turn=True
    game_repetition=input("Do you want to repeat the game?\n'Y' Yes and 'N' for No. Anything else will be considered as No:\n").upper()
    board= [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
print("Game has quitted. Thank's for playing.")

#_______________________          END OF THE MIGHTY CODE ╰(*°▽°*)╯             _____________________________#