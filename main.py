import random

available_index = [1,2,3,4,6,7,8,9]
n=3



def display_board(board):
    print("+-------+-------+-------+")
    for i in range (0,3):
        print("|      ","|      " ,"|       " ,end="|\n")
        print("|","  "+board[i][0]+"   |" , "  "+board[i][1]+"   |" , "  "+board[i][2]+"   "  , end="|\n")
        print("|      ","|      " ,"|       " ,end="|\n")
        print("+-------+-------+-------+")

def enter_move(board):
    try :
        move = int(input("Enter your move : "));
    except : 
        print("incorrect move")    
        enter_move(board)
    if(move < 0 or move  > 9 ):
       print("incorrect move")    
       enter_move(board) 
    x_index=((move-1)// n)
    y_index=move - (x_index * n) -1
    if(board[x_index][y_index] in ("x" , "X" , "o" , "O")):
       print("incorrect move")    
       enter_move(board) 
    board[x_index][y_index]="x"
    del available_index[available_index.index(move)]
    if victory_for(board, "x"):
        print("You won");
        return
    if len(available_index) == 0 :
        print("Game over")
        return
    else :
        draw_move(board)


def make_list_of_free_fields(board):
    board +=[[str(y*n + x)  for x in range(1,n+1)] for y in range (0,n)]
    board[1][1]="o"


def victory_for(board, sign):
    for i in range (n):
        if(board[i][0]+board[i][1]+board[i][2] == 3*sign):
            return True
        if(board[0][i]+board[1][i]+board[2][i] == 3*sign):
            return True
    if board[0][0] + board[1][1]+ board[2][2] == 3*sign:
        return True
    if board[2][0] + board[1][1]+ board[0][2] == 3*sign:
        return True
    return False


def draw_move(board):
    move =  random.choice(available_index);
    del available_index[available_index.index(move)]
    x_index=((move-1)// n)
    y_index=move - (x_index * n) -1
    board[x_index][y_index]="o"
    display_board(board)
    if victory_for(board, "o"):
        print("Computer won");
        return
    if len(available_index) == 0 :
        print("Game over")
        return
    else :
        enter_move(board)
board = []
make_list_of_free_fields(board)
display_board(board)
enter_move(board)
