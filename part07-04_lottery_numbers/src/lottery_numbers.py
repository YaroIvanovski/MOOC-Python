# Write your solution here
from random import randint
def lottery_numbers(amount: int, lower: int, upper: int):
    list = []
    i = 1
    while (i <= amount):
        num = randint(lower, upper)
        if num not in list:
            list.append(num)
        i += 1   
    return sorted(list)

if __name__ == "__main__":
    for num in lottery_numbers(7, 1, 40):
        print(num)