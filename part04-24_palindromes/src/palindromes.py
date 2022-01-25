
def palindromes(word: str):
    x = ""
    length = len(word) - 1
    while length >= 0:
        x += word[length]
        length -= 1
    return word == x

while True:
    word = input("Enter word: ")
    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    print("that wasn't a palindrome")

"""Suggested solution
def palindromes(word: str):
    for i in range(len(word)//2):
        if word[i] != word[len(word)-i-1]:
            return False
    return True
"""
