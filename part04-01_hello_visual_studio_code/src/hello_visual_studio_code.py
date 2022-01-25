# Write your solution here
while True:
    string = input("Editor:").lower()
    if string == "emacs" or string == "atom" or string == "vim":
        print("not good")
    elif string == "word" or string == "notepad":
        print("awful")
    elif string == "visual studio code":
        print("an excellent choice!")
        break