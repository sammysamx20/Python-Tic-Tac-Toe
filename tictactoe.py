#Function Name: print_board(board)
#Description: prints a clear tictactoe board
#Parameters: board
#Pre-Conditions: input of board
#Post_conditions: An empty board
#Return values: None
##############################################

def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j] + '|', end="")
        print()
        print ("------")

#Function Name: choice_player_n(board)
#Description: If the player chooses "n" this will input "n"
#Parameters: board
#Pre-Conditions: input of n
#Post_conditions: A spot with filled n
#Return values: None
##############################################        
def choice_player_n(board):
        
        place_n(board)
        print_board(board)
        
        for i in range(4):
        
            place_k(board)
            print_board(board)
            if check_k_win(board) == 1:
                print("Player 2 Wins!")
                return 2

            place_n(board)
            print_board(board)

            if check_n_win(board) == 1:
                print("Player 1 Wins!")
                return 1
            
        
        print("It's a tie :(")
        return 3
       # 2nd player
        
#Function Name: choice_player_k(board)
#Description: If the player chooses "k" this will input "k"
#Parameters: board
#Pre-Conditions: input of k
#Post_conditions: A spot with filled k
#Return values: None
##############################################
def choice_player_k(board):
    
        place_k(board)
        print_board(board)
        
        for i in range(4):
            
            place_n(board)
            
            print_board(board)
            if check_n_win(board) == 1:
                print("Player 2 wins!")
                return 2
            
            place_k(board)
            print_board(board)
            if check_k_win(board) == 1:
                print("Player 1 wins!")
                return 1 
            
                
        print("It's a tie :(")        #1st player
        return 3
        
#Function Name: place_n(board)
#Description: Lets the player input a spot they want to put their "n"
#Parameters: board
#Pre-Conditions: input of i and j
#Post_conditions: A spot chosen for n
#Return values: None
##############################################
def place_n(board):       
    print("Where do you want to place your n?")
    i =  input("enter row 0-2")
    for x in range(len(i)):
        if(not(i[x]>='0' and i[x]<='2')):
            print("This is not going to be a point on the TicTacToe table")
            return place_n(board)
        
    j = input("enter column 0-2")
    for y in range(len(j)):
        if(not(j[y]>='0' and j[y]<='2')):
            print("This is not going to be a point on the TicTacToe table")
            return place_n(board)
    if board[int(i)][int(j)]== 'n':
        print("There is already a symbol there.")
        return place_n(board)
    elif board[int(i)][int(j)]== 'k':
        print("There is already a symbol there.")
        return place_n(board)
    else:
        board[int(i)][int(j)] = 'n'

#Function Name: place_k(board)
#Description: Lets the player input a spot they want to put their "k"
#Parameters: board
#Pre-Conditions: input of i and j
#Post_conditions: A spot chosen for k
#Return values: None
##############################################
def place_k(board):
    print("Where do you want to place your k?")
    i = input("enter row 0-2")
    
    for x in range(len(i)):
        if (not(i[x] >='0' and i[x] <='2')):
            print("This is not going to be a point on the TicTacToe table")
            return place_k(board)
    

    j = input("enter a column 0-2")  
    for y in range(len(j)):
        if(not(j[y]>='0' and j[y] <='2')):
            print("This is not going to be a point on the TicTacToe table")
            return place_k(board)


    if board[int(i)][int(j)]== 'k':
        print("There is already a symbol there.")
        return place_k(board)
    elif board[int(i)][int(j)]== 'n':
        print("There is already a symbol there.")
        return place_k(board)
    else:
        board[int(i)][int(j)] = 'k'

#Function Name: check_k_win(board)
#Description: checks if the player with k has won
#Parameters: board
#Pre-Conditions: a board with 3 spots of k in a row
#Post_conditions: a message saying you have won
#Return values: None
##############################################
def check_k_win(board):
    
    if board[0][0] == "k" and board[0][1] == "k" and board[0][2] == "k":
            return 1
    if board[1][0] == "k" and board[1][1] == "k" and board[1][2] == "k":
            return 1
    if board[2][0] == "k" and board[2][1] == "k" and board[2][2] == "k":
            return 1
    if board[0][0] == "k" and board[1][0] == "k" and board[2][0] == "k":
            return 1
    if board[0][1] == "k" and board[1][1] == "k" and board[2][1] == "k":
            return 1
    if board[0][2] == "k" and board[1][2] == "k" and board[2][2] == "k":
            return 1
    if board[0][0] == "k" and board[1][1] == "k" and board[2][2] == "k":
            return 1
    if board[2][0] == "k" and board[1][1] == "k" and board[0][2] == "k":
            return 1
    
    
#Function Name: check_n_win(board)
#Description: checks if the player with n has won
#Parameters: board
#Pre-Conditions: a board with 3 spots of n in a row
#Post_conditions: a message saying you have won
#Return values: None
##############################################
def check_n_win(board):
    if board[0][0] == "n" and board[0][1] == "n" and board[0][2] == "n":
            return 1

    if board[1][0] == "n" and board[1][1] == "n" and board[1][2] == "n":
            return 1
    if board[2][0] == "n" and board[2][1] == "n" and board[2][2] == "n":
            return 1
    if board[0][0] == "n" and board[1][0] == "n" and board[2][0] == "n":
            return 1
    if board[0][1] == "n" and board[1][1] == "n" and board[2][1] == "n":
            return 1
    if board[0][2] == "n" and board[1][2] == "n" and board[2][2] == "n":
            return 1
    if board[0][0] == "n" and board[1][1] == "n" and board[2][2] == "n":
            return 1
    if board[2][0] == "n" and board[1][1] == "n" and board[0][2] == "n":
            return 1
    

#Function Name: get_piece()
#Description: gets input for piecese
#Parameters: None
#Pre-Conditions: None
#Post_conditions: None
#Return values: gets the input for piecese and returns them
##############################################

def get_piece():
    return input("What piece do you want? (choose k or n) : ")
    
#Function Name: main()
#Description: Holds functions to call them
#Parameters: None
#Pre-Conditions: None
#Post_conditions: Will call all functions
#Return values: None
##############################################
def main():
    player_1 = 0
    player_2 = 0
    tie = 0
    redo = True
    while redo == True:
        print("Tic-Tac-Toe Game")
        board = [[' ']*3, [' ']*3, [' ']*3]
        symbol_1 = get_piece()
        
        symbol_2 = get_piece()
    
        if symbol_1 == "k" and symbol_2 == "n":
            print_board(board)
            
            if choice_player_k(board) == 1:
                player_1 +=1
            elif choice_player_k(board) == 2:
                player_2 +=1
            elif choice_player_k(board)  == 3:
                tie +=1

            print("Player 1's Score: ", player_1)
            print("Player 2's Score: ", player_2)
            print("Ties:", tie)

        elif symbol_1 == "n" and symbol_2 == "k":
            print_board(board)
            if choice_player_n(board) == 1:
                player_1 +=1
            elif choice_player_n(board) == 2:
                player_2 +=1
            elif choice_player_n(board) == 3:
                tie +=1

            print("Player 1's Score: ", player_1)
            print("Player 2's Score: ", player_2)
            print("Ties:", tie)

        elif symbol_1 != "k" and "n":
            print("Choose a valid symbol.")
            

        elif symbol_2 != "k" and "n":
            print("Choose a valid symbol.")
            
        
        elif symbol_1 == symbol_2:
            print("You can't choose the same symbols! Pick again")
            

        

        repeat = int(input("Enter (1) to continue or press (0) to quit:" ))

      
        if(repeat == 1):
            redo = True
        
        if(repeat == 0):
            redo = False
    

main()

