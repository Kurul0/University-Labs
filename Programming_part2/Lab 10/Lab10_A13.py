A = set(map(int, input("\nВведи числа від 1 до 25 через пробіл:").split()))
B = set(map(int, input("\nВведи числа від 1 до 25 через пробіл:").split()))

C = A | B #об'єднання
D = A & B #перетин
E = A - B #різниця
F = B - A #різниця

print("\nA належить С:\n", A.issubset(C))
print("D належить C:\n", D.issubset(C))
print("E перетин F перетин D = C:\n", C == E | F | D)
print("E перетин з F = пуста множина\n", E.isdisjoint(F))

print("A:", A)
print("B:", B)
print("C:", C)
print("D:", D)
print("E:", E)
print("F:", F)