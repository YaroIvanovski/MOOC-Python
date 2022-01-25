# Write your solution here
many = int(input("How many items: "))
count = 0
my_list = []
while count <= many -1:
    count += 1
    item = int(input(f"Item {count}: "))
    my_list.append(item)
print(my_list)

"""Suggested solution
numbers = int(input("How many items: "))
list = []
 
while len(list) < numbers:
    number = int(input(f"Item {len(list) + 1}: "))
    list.append(number)
 
print(list)
"""