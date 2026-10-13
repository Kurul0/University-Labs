max_count = 0
max_line = ""
with open('G:\\My Drive\\Programming_part2\\Lab8\\F1.txt', 'r', encoding='utf-8') as f1:
    for line in f1:
        current_k_count = line.lower().count('к')
        if current_k_count > max_count:
            max_count = current_k_count
            max_line = line
if max_count == 0:
    print("There is no line with the letter 'к' in the file.")
else:
    with open('G:\\My Drive\\Programming_part2\\Lab8\\F2.txt', 'w', encoding='utf-8') as f2:
        f2.write(max_line)
    print ("Done")
    print ()
    print(f"The line with the most 'к' characters is: \n {max_line}")
    print ()
    print(f"The number of 'к' characters in that line: {max_count}")