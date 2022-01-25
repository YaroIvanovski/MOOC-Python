# Write your solution here
def same_chars(txt, num, num2):
    if num >= len(txt) or num2 >= len(txt):
        return False
    return txt[num] == txt[num2]


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))