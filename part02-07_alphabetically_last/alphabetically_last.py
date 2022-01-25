# Write your solution here
word = input("Please type in the 1st word:")
word2 = input("Please type in the 2nd word:")

if word > word2:
    print(f"{word} comes alphabetically last")
elif word2 > word:
    print(f"{word2} comes alphabetically last")
else:
    print("You gave the same word twice")
