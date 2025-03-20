matrix = [[1,2,3],[4,5,6],[7,8,9]]

def foo(matrix : list[list[int]]) -> list[list[int]]:
    matrix.reverse()
    for pos, i in enumerate(zip(*matrix)):
        matrix[pos] = list(i)


foo(matrix)
print(matrix)