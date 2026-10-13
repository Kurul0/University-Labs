import random;
m = 6
n = 8
matrix = []

for i in range(m):
    matrix.append([])
    for j in range(n):
        value = random.randint(1, 100)
        matrix[i].append(value)

print("Початкова матриця:\n")
for i in range(m):
    for j in range(n):
        print(f"{matrix[i][j]:4}", end=" ")
    print()

max=matrix[0][0]
for i in range(m):
    for j in range(n):
        if matrix[i][j]>max:
            max=matrix[i][j]
print(); #для відступу після початкової матриці
print(f"Найбільший елемент матриці: {max}\n")

for i in range(m):
    for j in range(n):
        matrix[i][j]=matrix[i][j]/max
print("Нормалізована матриця:\n")

for i in range(m):
    for j in range(n):
        print(f"{matrix[i][j]:.4f}", end=" ")
    print()