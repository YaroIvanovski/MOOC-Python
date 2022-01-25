# Write your solution here
def one(x):
    name = input("name: ")
    if name in x:
        for number in x[name]:
            print(number)
    else:
        print("no number")

def two(x):
    name = input("name: ")
    number = input("number: ")
    if name not in x:
        x[name] = []
    x[name].append(number)
    print("ok!")

def main():
    x = {}
    while True:
        command = input("command (1 search, 2 add, 3 quit): ")
        if command == "1":
            one(x)
        if command == "2":
            two(x)
        if command == "3":
            break
    print("quitting...")

main()