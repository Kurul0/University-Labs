lines_count = 0
with open('G:\\My Drive\\Programming_part2\\Lab 9\\Text_A13.txt', 'r', encoding='utf-8') as f1:
    for line in f1:
        current_line = line.strip()
        if len(current_line) < 40:
            lines_count = lines_count + 1
print(f"\nThe amount of lines with less than 40 characters = {lines_count}\n")