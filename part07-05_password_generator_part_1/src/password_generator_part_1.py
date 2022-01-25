# Write your solution here
import random
import string

def generate_password(length: int):
    ch = string.ascii_lowercase
    pas = '' .join(random.choice(ch) for i in range(length))
    return pas

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))

"""Suggested solution
from random import choice
from string import ascii_lowercase
 
def generate_password(length: int):
    passwd = ""
    for i in range(length):
        passwd += choice(ascii_lowercase)
 
    return passwd
"""