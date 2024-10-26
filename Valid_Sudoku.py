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
    board2 = board[:]
    board3 = board[:]

    board3 = [board[j][i:i+3] for i in range(0,len(board),3) for j in range(9)]
    gridbox = []
    rand = []
    count = 0
    for i in board3:
        rand += i
        count += 1
        if count % 3 == 0:
            gridbox.append(rand)
            rand = []

    for i in range(len(board1)):
        board1[i] = [board1[i][:].pop(j) for j in range(len(board1[i])) if board1[i][j] != "."]
        board2[i] = [board[k][i] for k in range(len(board)) if board[k][i] != "."]
        gridbox[i] = [j for j in gridbox[i] if j != "."]
    
    for i in range(len(board)):
        if len(set(board1[i])) != len(board1[i]):
            Rows = False
        if len(set(board2[i])) != len(board2[i]):
            Columns = False
        if len(set(gridbox[i])) != len(gridbox[i]):
            Grid3 = False

    return Rows and Columns and Grid3


print(foo(board))
