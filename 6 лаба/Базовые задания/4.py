MATRIX1 = [ [ 1, 5, 6, 7],
           [ 6, 0, 0, 0],
           [-9, 5, 1, 0] ]

MATRIX2 = [ [ 1, 5, 6],
           [ 6, 0, 0],
           [-9, 5, 1],
           [7, 0, 0] ]

with open('Матрица1.txt','w') as f:
    for i in MATRIX1:
        for j in i:
            f.write(str(j)+' ')
        f.write('\n')

with open('Матрица2.txt','w') as f:
    for i in MATRIX2:
        for j in i:
            f.write(str(j)+' ')
        f.write('\n')


def read_matrix(file_name):
    with open(file_name, 'r') as file:
        matrix = []
        for line in file:
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix

def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix2)):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    return result

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

matrix1 = read_matrix('Матрица1.txt')
matrix2 = read_matrix('Матрица2.txt')

result_matrix = multiply_matrices(matrix1, matrix2)

print_matrix(matrix1)
print("   X")
print_matrix(matrix2)
print("   =")
print_matrix(result_matrix)