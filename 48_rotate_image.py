def swap(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    return matrix
def rotate(matrix):
    matrix = swap(matrix)
    n = len(matrix)
    for i in range(n):
        for j in range(n//2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n - 1 - j]
            matrix[i][n - 1 - j] = temp           
    return matrix    

if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    ans = rotate(matrix)
    print(ans)