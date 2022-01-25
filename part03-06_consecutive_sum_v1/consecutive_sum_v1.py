# Write your solution here
limit = int(input("Limit:"))
num = 1
value = 1
while value < limit:
    num += 1
    value += num
print(value)