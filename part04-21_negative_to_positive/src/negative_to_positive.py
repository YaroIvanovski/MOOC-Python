# Write your solution here
num = int(input("Please type in a positive integer: "))
for i in range(-num, num + 1):
    if i == 0:
        continue
    print(i)

"""Suggested solution
number = int(input("Please type in a positive integer: "))
 
for i in range(-number, number + 1):
    # Because in Python bool-type equals to
    # 0 and 1 (False and True), condition can also be written as follows
    # if i:
    if i != 0:
        print(i)
"""