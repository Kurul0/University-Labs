import random
m = 4 #rows
n = 5 #columns
matrix = []

for i in range (m):
    matrix.append([])
    for j in range (n):
        value = random.randint(10, 99)
        matrix[i].append(value)

print("Початкова матриця")
for i in range (m):
    for j in range (n):
        print(f"{matrix[i][j]:4}", end=" ")
    print()

min_val = matrix[0][0]
for i in range (m):
    for j in range (n):
        if matrix[i][j]<min_val:
            min_val=matrix[i][j]
print(); #для відступу після початкової матриці
print(f"Найменше число у матриці: {min_val}\n")

print("Відформатована матриця:\n")
for i in range (m):
    for j in range (n):
        matrix[i][j]=matrix[i][j]-min_val
        print(f"{matrix[i][j]:4}", end=" ")
    print()