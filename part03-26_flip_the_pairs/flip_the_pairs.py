# Write your solution here
num = int(input("Please type in a number:"))
i = 1
while i + 1 <= num:
    print(i + 1)
    print(i)
    i += 2
if i <= num:
    print(i)