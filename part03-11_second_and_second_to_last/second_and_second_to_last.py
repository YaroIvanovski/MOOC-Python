# Write your solution here
string = input("Please type in a string:")
if string[1] != string[len(string) - 2]:
    print("The second and the second to last characters are different")
else:
    print(f"The second and the second to last characters are {string[1]}")