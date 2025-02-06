matrix = [[1,2,3],[4,5,6]]

def foo(matrix : list[list[int]]) -> list[list[int]]:
    tranpose = [[] for i in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            tranpose[i].append(matrix[j][i])
    return tranpose


print(foo(matrix))
 