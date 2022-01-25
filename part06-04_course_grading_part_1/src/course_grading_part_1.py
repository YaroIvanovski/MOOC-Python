# write your solution here
student = input("Student information: ")
exercise = input("Exercises completed: ")
 
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
    
for student_id, name in students.items():
    print(f"{name} {exercises[student_id]}")