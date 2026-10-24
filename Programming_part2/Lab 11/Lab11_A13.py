students = []

with open('E:\\Codding\\University-Labs\\Programming_part2\\Lab 11\\Students.txt', mode='r', encoding='utf-8') as f1:
    for line in f1:
        if not line.strip():
            continue
        data = [item.strip() for item in line.split(';')]
        student_record = {
            "name": data[0],
            "birth_date": data[1],
            "year": data[2],
            "course": data[3],
            "group": data[4],
            "grade": [int(mark.strip()) for mark in data[5].split(',')]
        }
        students.append(student_record)

print(students)
    
total_group_score = 0
for student in students:
    student["average_score"] = sum(student["grade"])/len(student["grade"])
    total_group_score = total_group_score + student["average_score"]
group_average = total_group_score/len(students)

print("Середній бал групи:", round(group_average, 2))
print(f"{'ПІБ':<35} | {'Дата народж.':<15} | {'Рік':<15} | {'Курс':<15} | {'Група':<15} | {'Середній бал':<15}")
for student in students:
    print(f"{student['name']:<35} | {student['birth_date']:<15} | {student['year']:<15} | {student['course']:<15} | {student['group']:<15} | {round(student['average_score'], 2):<15}")
print()

print("Студенти з балом вище середнього:")
for student in students:
    if student['average_score'] > group_average:
        print(f"{student['name']:<35} | {student['birth_date']:<15} | {student['year']:<15} | {student['course']:<15} | {student['group']:<15} | {round(student['average_score'], 2):<15}")