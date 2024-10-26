board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def foo(board : list[list[str]]) -> bool:

    Rows = True
    Columns = True
    Grid3 = True
    board1 = board[:]

    for i in range(len(board1)):
        board1[i] = [board1[i][:].pop(j) for j in range(len(board1[i])) if board1[i][j] != "."]
    
    for row in range(len(board1)):
        if len(set(board1[row])) != len(board1[row]):
            Rows = False
    
    for column


    
    return board


print(foo(board))