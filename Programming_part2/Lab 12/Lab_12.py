class Node: 
    def __init__(self, data):         # конструктор вузла
        self.data = data              # збереження символу
        self.next = None              # порожній вказівник

header = Node(None)                   # створення ланки-заголовка
current = header                      # створення каретки

with open("E:\\Codding\\University-Labs\\Programming_part2\\Lab 12\\Text.txt", "r", encoding="utf-8") as file:
    text = file.read()

for char in text:                     # перебір символів
    new_node = Node(char)             # створення об'єкта
    current.next = new_node           # зв'язування вузлів
    current = new_node                # перехід на наступний об'єкт

print_ptr = header.next               # встановлення вказівника для читання

while print_ptr is not None:          # проходження списку
    print(print_ptr.data, end="")     # виведення символу
    print_ptr = print_ptr.next        # перехід на наступний об'єкт

print("\n")

if current.data == "!":
    print("Рядок закінчується знаком '!'")
else:
    print("Рядок НЕ закінчується знаком '!'")