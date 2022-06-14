from random import randint
 
def lottery_numbers(amount: int, lower: int, upper: int):
    numbers = []

    while len(numbers) < amount:
        num = randint(lower, upper)
        if num not in numbers:
            numbers.append(num)
          
    return sorted(numbers)


if __name__ == "__main__":
    for num in lottery_numbers(7, 1, 40):
        print(num)
