# Write your solution here
string = input("Please type in a word:")
character = input("Please type in a character:")
index = string.find(character)
length = len(string) -1
if index < 0:
    print()
elif index < length - 1:  
    print(string[index] + string[index + 1] + string[index + 2])

""" Suggested solution
word = input("Please type in a word: ")
character = input("Please type in a character: ")
 
index = word.find(character)
if index!=-1 and len(word)>=index+3:
    print(word[index:index+3])
"""