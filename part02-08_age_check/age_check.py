# Write your solution here
num = int(input("What is your age?"))
if num < 0:
    print("That must be a mistake")
elif num < 5:
    print("I suspect you can't write quite yet...")
else:
    print(f"Ok, you're {num} years old")    