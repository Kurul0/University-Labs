m = 3
n = 4
matrix = []
with open('G:\\My Drive\\Programming_part2\\Lab8\\Matrix.txt', 'r', encoding='utf-8') as f1:
    for line in f1:
        row = []
        numbers_in_row = line.split()
        for number in numbers_in_row:
            row.append(int(number))
        matrix.append(row)
print("Matrix in a file:\n")

for row in matrix:
    for number in row:
        print(number, end=" ")
    print()

max_number = matrix[0][0]
for i  in range(m):
    for j in range(n):
        if matrix[i][j] > max_number:
            max_number = matrix[i][j]
print(f"\nThe biggest element in the matrix: {max_number}\n")