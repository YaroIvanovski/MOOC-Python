# write your solution here
text = input("Write text: ").split(" ")

with open("wordlist.txt") as file:
    word = []
    for line in file:
        line = line.replace("\n", "")
        word.append(line)

for i in range(0, len(text)):
    if text[i].lower() not in word:
        text[i] = "*" + text[i] + "*"
    print(text[i], end = " ")
print()

"""Suggested solution
def wordlist():
    words = []
 
    with open("wordlist.txt") as file:
        for row in file:
            words.append(row.strip())
 
    return words
 
words = wordlist()
sentence = input("Write text: ")
 
for word in sentence.split(' '):
    if word.lower() in words:
        print(word + " ", end="")
    else:
        print("*" + word + "* ", end="")
 
print()
"""