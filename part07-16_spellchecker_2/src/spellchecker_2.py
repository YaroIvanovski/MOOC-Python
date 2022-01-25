# Write your solution here
import difflib 
 
def wordlist():
    words = []
    with open("wordlist.txt") as file:
        for row in file:
            words.append(row.strip())
    return words
 
words = wordlist()
sentence = input("write text: ")
error = []
for word in sentence.split(' '):
    if word.lower() in words:
        print(word+ " ", end="")
    else:
        error.append(word)
        print("*" + word+ "* ", end="") 
print()
print("suggestions:")

for word in error:
    suggestion_list = difflib.get_close_matches(word, words)
    suggestions = ", ".join(suggestion_list)
    print(f"{word}: {suggestions}")