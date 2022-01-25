# Write your solution here
word = input('Please type a word:')
character = input('Please type a character:')
count = -9
while count <= len(word):
    index = word.find(character) 
    if index >= 0 and len(word) - index > 2:
        print(word[index:index + 3])
        index = word.find(character)
        index += 1
        word = word[index:]
    count += 1
    
""" Suggested solution
word = input("Please type in a word: ")
character = input("Please type in a character: ")
 
index = 0
 
while index + 3 <= len(word):
    if word[index] == character:
        print(word[index:index+3])
    index += 1
"""