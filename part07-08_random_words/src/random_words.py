# Write your solution here
from random import sample

def words(n: int, beginning: str):
    list = []
    words_list = ""
 
    with open("words.txt") as file:
    
        for row in file:
            row = row.replace("\n", "")            
            row = row.strip() 
            if row.startswith(beginning):
                list.append(row)
    
        words_list = sample(list, n)
        return words_list
 
if __name__ == '__main__':
    word_list = words(3, "ca")
    for word in word_list:
        print(word)

"""Suggested solution
import random
def words(n: int, beginning: str):
    word_list = []
    with open("words.txt") as file:
        for word in file:
            word = word.replace("\n","")
            if word.startswith(beginning):
                word_list.append(word)
    if len(word_list) < n:
        raise ValueError("Not enough suitable words can be found!")
    return random.sample(word_list, n)
"""