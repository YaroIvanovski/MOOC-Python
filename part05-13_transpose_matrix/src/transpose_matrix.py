# Write your solution here
def transpose(matrix: list):
    x = len(matrix)
    for i in range(x):
        for j in range(i, x):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

if __name__ == "__main__":
    transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
