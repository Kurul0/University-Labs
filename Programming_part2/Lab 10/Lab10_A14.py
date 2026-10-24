def find_operators (text):
    valid_signs = {',', '.', '!', ';', ':', '-', '?'}
    return valid_signs.intersection(text)

with open ("E:\\Codding\\University-Labs\\Programming_part2\\Lab 10\\Lab10_A14_INPUT.txt" , 'r', encoding='utf-8') as f1:
    result = find_operators (f1.read())

print(f"\nThe result is {result}\n")