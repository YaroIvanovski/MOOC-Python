# write your solution here
def read_fruits():
    fruits = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            parts = line.split(";")
            fruit = parts[0]
            price = float(parts[1])
            fruits[fruit] = price
    
    return fruits

if __name__ == "__main__":
    print(read_fruits())

"""Suggested solution
def read_fruits():
    with open("fruits.csv") as file:
        fruits = {}
        for row in file:
            # split to two pieces
            data = row.split(";")
            # name first, price second
            fruits[data[0]] = float(data[1])
    return fruits
"""