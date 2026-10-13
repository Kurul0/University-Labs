import re
with open('G:\\My Drive\\Programming_part2\\Lab 9\\Text_B13.txt', 'r', encoding='utf-8') as f1:
    full_text = f1.read()
text_step1 = re.sub(r'\bin\b', '_TEMP_', full_text)
text_step2 = re.sub(r'\bon\b', 'in', text_step1)
final_text = re.sub(r'\b_TEMP_\b', 'on', text_step2)

with open('G:\\My Drive\\Programming_part2\\Lab 9\\Text_B13_2.txt', 'w', encoding='utf-8') as f2:
    f2.write(final_text)
print('\nDone\n')