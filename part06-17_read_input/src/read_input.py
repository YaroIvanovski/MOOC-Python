def read_input(inpt: str, min: int, max: int):
    while True:
        try:
            num = int(input(inpt))
            if num >= min and num <= max:
                return num
        except ValueError:
            pass
        print(f"You must type in an integer between {min} and {max}")


if __name__ == "__main__":
    num = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", num)


"""Suggested solution
def read_input(prompt: str, lower_limit: int, upper_limit: int):
    while True:
        error = False
        try:
            number = int(input(prompt))
            if number < lower_limit or number > upper_limit:
                error = True
        except:
            error = True
        if error:
            print(f"You must type in an integer between {lower_limit} and {upper_limit}")
        else:
            return number
"""
