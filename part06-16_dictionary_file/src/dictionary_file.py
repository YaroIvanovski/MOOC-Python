# Write your solution here
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    select = int(input("Function: "))
    if select == 1:
        fi = input("The word in Finnish: ")
        en = input("The word in English: : ")

        with open("dictionary.txt", "a") as filename:
            filename.write(f"{fi} - {en}\n")
        print("Dictionary entry added")
    
    if select == 2:
        search = input("Search term: ")
        with open("dictionary.txt") as filename:
            for row in filename:
                row = row.replace("\n", "")
                if search in row:
                    print(row)

    if select == 3:
        print("Bye!")
        break

"""Suggested solution
def read_dictionary():
    # Words are stored in a list. If the translation would always
    # be to same direction (e.g. from English to Finnish),
    # using dictionary as a data structure would be a good idea
    dictionary = []
 
    with open("dictionary.txt") as file:
        # In the example file, word pair is at one line as
        # finnish;english, for example
        # auto;car
        for row in file:
            row = row.replace("\n","")
            dictionary.append(tuple(row.split(";")))
 
    return dictionary
 
def add_word(dictionary: list):
    word_fi = input("The word in Finnish: ")
    word_en = input("The word in English: ")
    # Add to list
    dictionary.append((word_fi, word_en))
 
    # Write to file
    with open("dictionary.txt", "a") as file:
        file.write(word_fi + ";" + word_en + "\n")
        print("Dictionary entry added")
 
def search_word(dictionary: list):
    word = input("Search term: ")
    for word_fi, word_en in dictionary:
        if word in word_fi or word in word_en:
            print(f"{word_fi} - {word_en}")
  
dictionary = read_dictionary()
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = input("Function: ")
    if function == "1":
        add_word(dictionary)
    elif function == "2":
        search_word(dictionary)
    elif function == "3":
        print("Bye!")
        break
"""