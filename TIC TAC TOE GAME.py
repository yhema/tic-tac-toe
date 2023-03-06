import numpy as np
grids=np.array([['-','-','-'],['-','-','-'],['-','-','-']])
player1='x'
player2='o'
def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range (3):
            if grids[r][c]==symbol:
                count=count+1
        if count==3:
             print(symbol,'won')
             return True
    return False
def check_col(symbol):
    for  c in range(3):
        count=0
        for r in range(3):
            if grids[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,'won')
            return True
        return False
def check_diagonals(symbol):
     if grids[0][2]==grids[1][1] and grids[2][0]==grids[1][1] and grids[1][1]==symbol:
         print(symbol,'won')
         return True
     if grids[0][0]==grids[1][1] and grids[1][1]==grids[2][2] and grids[1][1]==symbol:
         print(symbol,'won')
         return True
     return False  
    
def won(symbol):
    return check_rows(symbol) or check_col(symbol) or check_diagonals(symbol)
def place(symbol):
    print(np.matrix(grids))
    while(1):
        row=int(input('enter row'))
        col=int(input('enter column'))
        if row>0and row<4 and col>0 and col<4 and grids[row-1][col-1]=='-':
            break
        else:
            print('invalid input ,please! try again')
    grids[row-1][col-1]=symbol   
   
def play_game():
    for turn in range(9):
        if turn%2==0:
            print('x turn:')
            place(player1)
            if won(player1):
                break
        else:
            print('o turn')
            place(player2)
            if won(player2):
                break
    if not (won(player1)) and not(won(player2)):
        print('draw')
        
        
        
play_game()
            
             
        