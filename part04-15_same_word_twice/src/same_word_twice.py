# Write your solution here
my_list = []
while True:
    word = input("Word: ")
    if word in my_list:
        break
    my_list.append(word)
print("You typed in", len(my_list), "different words")