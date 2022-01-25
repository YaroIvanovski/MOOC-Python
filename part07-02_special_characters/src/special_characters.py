# Write your solution here
import string
def separate_characters(my_string: str):
    parts = ["", "", ""]
    for character in my_string:
        if string.ascii_letters.find(character)!= -1:
            parts[0] += character
        elif string.punctuation.find(character)!= -1:
            parts[1] += character
        else:
            parts[2] += character
            
    return (parts[0], parts[1], parts[2])

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])

"""Suggested solution
from string import ascii_letters, punctuation
 
def separate_characters(my_string: str):
    letters = ""
    special_characters = ""
    other_characters = ""
 
    for character in my_string:
        if character in ascii_letters:
            letters += character
        elif character in punctuation:
            special_characters += character
        else:
            other_characters += character
 
    return (letters, special_characters, other_characters)
"""