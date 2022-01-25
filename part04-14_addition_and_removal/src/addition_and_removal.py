# Write your solution here
my_list = []
count = 0
print(f"The list is now {my_list}")
while True:
    item = input("a(d)d, (r)emove or e(x)it: ")
    if item == "x":
        print("Bye!")
        break
    if item == "d":
       # print(f"The list is now {my_list}")
        count += 1
        my_list.append(count)
        
    if item == "r":
      #  print(f"The list is now {my_list}")
        count -= 1
        my_list.pop(count)
        
    print(f"The list is now {my_list}")

"""Suggested solution
list = []
while True:
    print(f"The list is now {list}")
    selection = input("a(d)d, (r)emove or e(x)it:")
    if selection == "d":
        # Value of item is length of the list + 1
        item = len(list) + 1
        list.append(item)
    elif selection == "r":
        list.pop(len(list) - 1)
    elif selection == "x":
        break
 
print("Bye!")
"""
