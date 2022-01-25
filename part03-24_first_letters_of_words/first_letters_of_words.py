# Write your solution here
sentence = input("Please type in a sentence:")
sentence = " " + sentence
i = 1
while i < len(sentence):
    if sentence[i - 1] == " " and sentence[i] != " ":
        print(sentence[i])
    i += 1