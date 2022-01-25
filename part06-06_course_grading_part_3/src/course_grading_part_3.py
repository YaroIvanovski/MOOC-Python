
student = input("Student information: ")
exercise= input("Exercises completed: ")
exam = input("Exam points: ")
 
def grade(points):
    a = 0
    limits = [15, 18, 21, 24, 28]
    while a < 5 and points >= limits[a]:
        a += 1
 
    return a
 
def to_points(num):
    return num // 4
 
students = {}
with open(student) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"
 
exercises = {}
with open(exercise) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        sum = 0
        for i in range(1, 8):
            sum += int(parts[i])
        exercises[parts[0]] = sum
 
exams = {}
with open(exam) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue 
        sum = 0
        for i in range(1, 4):
            sum += int(parts[i])
        exams[parts[0]] = sum
 
print("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")
for id, name in students.items():
    exec_nbr = exercises[id]
    exec_score = to_points(exec_nbr)
    exam_points = exams[id]
    total_points = exec_score + exam_points
    print(f"{name:30}{exec_nbr:<10}{exec_score:<10}{exam_points:<10}{total_points:<10}{grade(total_points):<10}")