students = input("Student information: ")
exercises = input("Exercises completed: ")
points = input("Exam points: ")

with open(students) as file:
    next(file)
    name = {}
    for lines in file:
        lines = lines.replace("\n", "")
        student = lines.split(';')
        name[student[0]] = student[1] + " " + student[2]

with open(exercises) as file:
    next(file)
    exercise = {}
    for lines in file:
        lines = lines.replace("\n", "")
        student = lines.split(';')
        exercise[student[0]] = 0
        for i in student[1:]:
            exercise[student[0]] = exercise[student[0]] + int(i)

with open(points) as file:
    next(file)
    point = {}
    for lines in file:
        lines = lines.replace("\n", "")
        student = lines.split(';')
        point[student[0]] = 0
        for i in student[1:]:
            point[student[0]] = point[student[0]] + int(i)

total = {}

for key, value in name.items():
    total[key] = exercise[key] // 4 + point[key]
    if total[key] >= 0 and total[key] <= 14:
        print(f"{value} 0")
    if total[key] >= 15 and total[key] <= 17:
        print(f"{value} 1")
    if total[key] >= 18 and total[key] <= 20:
        print(f"{value} 2")
    if total[key] >= 21 and total[key] <= 23:
        print(f"{value} 3")
    if total[key] >= 24 and total[key] <= 27:
        print(f"{value} 4")
    if total[key] >= 28:
        print(f"{value} 5")

"""Suggested solution
student_data = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")
 
def grade(points):
    a = 0
    limits = [15, 18, 21, 24, 28]
    while a < 5 and points >= limits[a]:
        a += 1
 
    return a
 
def to_points(number):
    return number // 4
 
students = {}
with open(student_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"
 
exercises = {}
with open(exercise_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        esum = 0
        for i in range(1, 8):
            esum += int(parts[i])
        exercises[parts[0]] = esum
 
exams = {}
with open(exam_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue 
        esum = 0
        for i in range(1, 4):
            esum += int(parts[i])
        exams[parts[0]] = esum
 
for student_id, name in students.items():
    total = exams[student_id] + to_points(exercises[student_id])
    print(f"{name} {grade(total)}")
"""