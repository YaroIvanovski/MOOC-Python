# Write your solution here
num = int(input("Please type in a number:"))
x = 1
y = num

while x < y:
    print(x)
    print(y)
    x += 1
    y -= 1
if x == y:
    print(x)