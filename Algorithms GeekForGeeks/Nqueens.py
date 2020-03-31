def isSafe(board,i,j,n):
    #CHECKING IN COLUMN
    for row in range(0,i):
        if(board[row][j]==1):
            return False
    #CHECKING IN LEFT DIAGONAL
    x,y=i,j
    while(x>=0 and y>=0):
        if(board[x][y]==1):
            return False
        x-=1;y-=1
    x,y=i,j
    #CHECKING IN RIGHT DIAGONAL
    while(x>=0 and y<n):
        if(board[x][y]==1):
            return False
        x-=1;y+=1
    return True
def solveNqueens(board,i,n):
    #BASE CASE ITS CASE WHERE WE HAVE TO PRINT BOARD
    if(i==n):
        #PRINT THE BOARD
        print(board)
    #WE HAVE TO PLACE QUEENS ON BOARD
    for j in range(n):
        if(isSafe(board,i,j,n)):
            board[i][j]=1
            place=solveNqueens(board,i+1,n)
            if(place==1):
                return True 
            #MEANS OUR ASSUMPTION IS WRONG
            board[i][j]=0   #BACKTRACKED
    return False
    
board=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

solveNqueens(board,0,5)

#-----------------------FOR UNDERSTANDING PURPOSE---------------------------

"""def isSafe(board,i,j,n):
    #CHECKING IN COLUMN
    for row in range(i):
        if(board[row][j]==1):
            return False
    #CHECKING IN RIGHT DIAGONAL
    row,column=i,j
    while(row>=0 and column<n):
        if(board[row][column]==1):
            return False
        row-=1
        column+=1
    #CHECKING IN LEFT DIAGONAL
    row,column=i,j
    while(row>=0 and column>=0):
        if(board[row][column]==1):
            return False
        row-=1
        column-=1
    return True
def solveNqueens(board,i,n):  
    if(i==n):
        print(board)
        return True
    for j in range(n):
        if(isSafe(board,i,j,n)):
            board[i][j]=1
            solveNqueens(board,i+1,n)
            board[i][j]=0  
  
board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
solveNqueens(board,0,4)
    
"""
    
