# Write your solution here

from random import randint, sample
 
def generate_strong_password(length: int, val1: bool, val2: bool):
    pas = chr(randint(97, 122))
 
    special_characters = [33, 63, 61, 43, 45, 40, 41, 35]
    if length == 0:
        # Raise error when the length of password is 0
        raise ValueError("Wrong parameters for the function")
    elif length == 1:
        if val1 == False and val2 == False:
            # The length of password is 1 and should contain 1 letter
            pass
        else:
            # Raise error when the length of password is 1 and should contain at least 1 letter, 1 number and 1 special character
            raise ValueError("Wrong parameters for the function")
    elif length == 2:
        if val1 == True and val2 == True:
            # Raise error when the length of password is 2 and should contain at least 1 letter, 1 number and 1 special character
            raise ValueError("Wrong parameters for the function")
        elif val1 == False and val2 == True:
            # The length of password is 2 and should contain 1 letter and 1 special character
            pas = pas + chr(special_characters[randint(0, 7)])
        elif val1 == True and val2 == False:
            # The length of password is 2 and should contain 1 letter and 1 number
            pas = pas + chr(randint(48, 57))
        else:
            # The length of password is 2 and should contain 2 letters
            pas = pas + chr(randint(97, 122))
    else:
        if val1 == True and val2 == True:
            # Contains at least 1 number, 1 special character and 1 letter
            numbers = randint(1, length - 2)
            characters = randint(1, length - 1 - numbers)
            for i in range(0, numbers):
                pas = pas + chr(randint(48, 57))
            for i in range(0, characters):
                pas = pas + chr(special_characters[randint(0, 7)])
            for i in range(0, length - 1 - numbers - characters):
                pas = pas + chr(randint(97, 122))  
        elif val1 == False and val2 == True:
            # Contains at least 1 special character and 1 letter
            characters = randint(1, length - 1)
            for i in range(0, characters):
                pas = pas + chr(special_characters[randint(0, 7)])
            for i in range(0, length - 1 - characters):
                pas = pas + chr(randint(97, 122))                     
        elif val1 == True and val2 == False:
            # Contains at least 1 number and 1 letter
            numbers = randint(1, length - 1)
            for i in range(0, numbers):
                pas = pas + chr(randint(48, 57))
            for i in range(0, length - 1 - numbers):
                pas = pas + chr(randint(97, 122))
        else:
            # Only contains letter
            for i in range(0, length-1):
                pas = pas + chr(randint(97, 122))
    
    return ''.join(sample(pas, len(pas)))
 
if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))

"""Suggested solution
from random import choice, randint
from string import ascii_lowercase, digits
 
def generate_strong_password(length: int, numbers: bool, special_characters: bool):
    special_chars = "!?=+-()#"
    # One letter at beginning of the password
    passwd = choice(ascii_lowercase)
    choice_set = ascii_lowercase
 
    # If numbers is wanted, add at least one number
    if numbers:
        passwd = add_character(passwd, digits)
        choice_set += digits
 
    # same for special characters
    if special_characters:
        passwd = add_character(passwd, special_chars)
        choice_set += special_chars
 
    # build the rest of the password from the whole set
    while (len(passwd) < length):
        passwd = add_character(passwd, choice_set)
 
    return passwd
 
# Add a random character from the given set either
# at the beginning or end of the string
def add_character(passwd: str, characters):
    character = choice(characters)
    if randint(1,2) == 1:
        return character + passwd
    else:
        return passwd + character

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))
"""