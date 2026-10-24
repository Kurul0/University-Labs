students = []

with open('E:\\Codding\\University-Labs\\Programming_part2\\Lab 11\\Students.txt', mode='r', encoding='utf-8') as f1:
    for line in f1:
        if not line.strip():
            continue
        data = [item.strip() for item in line.split(';')]
        print(data)
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