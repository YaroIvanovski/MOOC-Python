# Write your solution here
def add_student(students: dict, name: str):
    students[name] = {}
 
def print_student(students: dict, name: str):
    if not name in students:
        print(f"{name}: no such person in the database")
        return
 
    students_completed_courses = students[name]
 
    print(f"{name}:")
    if len(students_completed_courses) == 0:
        print(" no completed courses")
    else:
        print(f" {len(students_completed_courses):} completed courses:")
        sum = 0
        for course, grade in students_completed_courses.items():
            course_grade = grade[1]
            print(f"  {course} {course_grade}")
            sum += course_grade
 
        print(f" average grade {sum/len(students_completed_courses):.1f}")
 
def add_course(students: dict, name: str, completion: tuple):
    students_completed_courses = students[name]
    course_name = completion[0]
    course_grade = completion[1]
 
    # failed course is not recorded in the database
    if course_grade==0:
        return
 
    # if previous grade is higher, new grade is not recorded in the database
    if course_name in students_completed_courses:
        if students_completed_courses[course_name][1] > course_grade:
            return
 
    students_completed_courses[course_name] = completion
 
def summary(students: dict):
    print(f"students {len(students)}")
    most_courses_count = 0
    best_avg_grade = 0
    for name, completions in students.items():
        if len(completions) > most_courses_count:
            most_courses = name
            most_courses_count = len(students[most_courses])
 
        sum = 0
        for course, grade in completions.items():
            sum += grade[1]
 
        if len(completions)==0:
            avg = 0
        else:
            avg = sum/len(completions)
 
        if avg>best_avg_grade:
            best_avg_grade = avg
            best = name
 
    print(f"most courses completed {most_courses_count} {most_courses}")
    print(f"best average grade {best_avg_grade:.1f} {best}")

if __name__ == "__main__" :
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)