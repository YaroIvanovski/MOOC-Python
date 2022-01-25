# Write your solution here
students = int(input("How many students on the course?"))
groupSize = int(input("Desire group size?"))
result = (students + groupSize -1) // groupSize

print(f"Number of groups formed: {result}")
