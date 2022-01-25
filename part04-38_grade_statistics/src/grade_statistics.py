# Write your solution here

ex_po = [] # exam points
ex_co = [] # exercises completed

while True:
    inpt = input("Exam points and exercises completed: ")
    if inpt == "":
        break    
    else:
        ex_po.append(int(inpt.split(" ")[0]))
        ex_co.append(int(inpt.split(" ")[1]) // 10)
 
print("Statistics:")
score = []
count = 0
sum = 0 
for i in range(0, len(ex_po)):
    sum = sum + ex_po[i] + ex_co[i]
    if ex_po[i] < 10:
        score.append(0)
        count += 1
    else:
        score.append(ex_po[i] + ex_co[i])
        
average = sum / len(ex_po)
print("Points average:", average) 

grades = {'5': 0, '4': 0, '3': 0, '2': 0, '1': 0, '0': 0} # dictionary 
 
for i in range(0, len(score)):
    if score[i] >= 0 and score[i] <= 14:
        grades['0'] = grades['0'] + 1
    elif score[i] >= 15 and score[i] <= 17:
        grades['1'] = grades['1'] + 1
    elif score[i] >= 18 and score[i] <= 20:
        grades['2'] = grades['2'] + 1
    elif score[i] >= 21 and score[i] <= 23:
        grades['3'] = grades['3'] + 1
    elif score[i] >= 24 and score[i] <= 27:
        grades['4'] = grades['4'] + 1
    else:
        grades['5'] = grades['5'] + 1
 
percentage = 100 - grades['0'] * 100 / len(ex_po)
print("Pass percentage:", f'{percentage:.1f}')

print("Grade distribution:")
for key, value in grades.items():
    print("  " + key + ": ", end = "")
    for i in range(0, value):
        print("*", end = "")
    print()

"""Suggested solution
def exam_and_exercise_completed(inpt):
    space = inpt.find(" ")
    exam = int(inpt[:space])
    exercise = int(inpt[space+1:])
    return [exam, exercise]
 
def exercise_points(amount):
    return amount // 10
 
def grade(points):
    boundary = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if points >= boundary[i]:
            return i
 
def mean(points):
    return sum(points) / len(points)
 
def main():
    points = []
    grades = [0] * 6
    while True:
        inpt = input("Exam points and exercises completed: ")
        if len(inpt) == 0:
            break
 
        exam_and_exercises = exam_and_exercise_completed(inpt)
        exercise_pnts = exercise_points(exam_and_exercises[1])
        total_points = exam_and_exercises[0] + exercise_pnts
 
        points.append(total_points)
        grd = grade(total_points)
        if exam_and_exercises[0] < 10:
            grd = 0
        grades[grd] += 1
 
    pass_pros = 100 * (len(points) - grades[0]) / len(points)
 
    print("Statistics:")
    print(f"Points average: {mean(points):.1f}")
    print(f"Pass percentage: {pass_pros:.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        stars = "*" * grades[i]
        print(f"  {i}: {stars}")
 
main()
"""