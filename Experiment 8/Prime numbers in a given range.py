# 1. Print 'dimension: ' and read n
print("dimension: ", end="")
n = int(input())

# 2. Print 'first matrix:' and read the matrix
print("first matrix:")
matrix1 = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix1.append(row)

# 3. Print 'second matrix:' and read the matrix
print("second matrix:")
matrix2 = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix2.append(row)

# 4. Multiplication Logic (This part of your code was correct!)
result = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

# 5. Print Result
print("Resultant Matrix:")
for row in result:
    print(*(row))
