# Write your solution here
def histogram(my_str: str):
    characters = {}
    for character in my_str:
        if not character in characters:
            characters[character] = 0
        characters[character] += 1
 
    for character, value in characters.items():
        stars = "*" * value
        print(f"{character} {stars}")

if __name__ == "__main__":
    histogram("abba")
