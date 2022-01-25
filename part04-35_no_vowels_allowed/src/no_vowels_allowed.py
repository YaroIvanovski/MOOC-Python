# Write your solution here
import re
def no_vowels(list):
    result = re.sub(r'[AEIOU]', '', list, flags=re.IGNORECASE)
    return result

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))

"""Suggested solution
def no_vowels(my_string: str):
    vowels = "aeiou"
    result = ""
 
    for letter in my_string:
        if letter not in vowels:
            result += letter
 
    return result
"""