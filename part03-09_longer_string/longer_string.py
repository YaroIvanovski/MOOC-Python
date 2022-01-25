# Write your solution here
string1 = input("Please type in string 1:")
string2 = input("Please type in string 2:")
x = len(string1)
y = len(string2)

if x > y:
    print(f"{string1} is longer")
elif y > x:
    print(f"{string2} is longer")
else:
    print("The strings are equally long")