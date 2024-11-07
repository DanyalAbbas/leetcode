matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

def foo(matrix : list[list[int]]) -> list[list[int]]:
    tranpose = [[] for i in range(3)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            tranpose[i].append(matrix[j][i])
    return tranpose


print(foo(matrix))
 