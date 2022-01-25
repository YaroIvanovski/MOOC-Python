# Write your solution here
num = int(input("Please type in a number:"))
for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(f"{i} x {j} = {i * j}")

"""Suggested solution
number = int(input("Please type in a number: "))
counter1 = 1
while counter1 <= number:
    counter2 = 1
    while counter2 <= number:
        print(f"{counter1} x {counter2} = {counter1*counter2}")
        counter2 += 1
    counter1 += 1
"""