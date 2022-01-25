while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    select = int(input("Input: "))
    if select == 0:
        print("Bye now!")
        break
    if select == 1:
        with open("diary.txt", "a") as file:
            file.write(input("Diary entry: ") + '\n')
        print("Diary saved")
    if select == 2:
        with open("diary.txt") as file:
            for lines in file:
                print(lines)

"""Suggested solution
# Read the markings first
with open("diary.txt") as file:
    content = []
    for row in file:
        content.append(row.replace("\n",""))
 
# Open file for appending
with open("diary.txt", "a") as file:
    while True:
        print("1 - add an entry, 2 - read entries, 0 - quit")
        function = input("Function: ")
        if function == "1":
            entry = input("Diary entry: ")
            file.write(entry + "\n")
            content.append(entry)
            print("Diary saved")
        elif function == "2":
            print("Entries:")
            for entry in content:
                print(entry)
        elif function == "0":
            print("Bye now!")
            break
# Write your solution here

"""