# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        m = int(max(new_file.readlines(), key=lambda x: int(x)))
        return m

if __name__ == "__main__":
    print(largest())

"""Suggested solution
def largest():
    with open("numbers.txt") as file:
        start = True
        biggest = 0
        for number in file:
            if start or int(number) > biggest:
                biggest = int(number)
                start = False
        return biggest
"""