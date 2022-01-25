# Write your solution here
def read_input(input_info: str, min: int, max: int):
    while True:
        try:
            num = int(input(input_info))
            if num >= min and num <= max:
                return num
        except ValueError:
            pass
        
        print("You must type in an integer between 5 and 10")

if __name__ == "__main__":
    num = read_input("Please type in a number: ")
    print("You typed in: ", num)

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