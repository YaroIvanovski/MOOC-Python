# Write your solution here
def create_tuple(x: int, y: int, z: int):
    list = []
    list.append(x)
    list.append(y)
    list.append(z)
    minV = min(list)
    maxV = max(list)
    sumV = sum(list)

    tuple = (minV, maxV, sumV)
    return(tuple[0], tuple[1], tuple[2])   

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))

"""Suggested solution
def create_tuple(x: int, y: int, z: int):
    # The function returns a tuple formed from the parameters (smallest, greatest, sum)
    smallest = min([x, y, z])
    greatest = max([x, y, z])
    sum = x + y + z # sum([x, y, z]) also works
 
    return (smallest, greatest, sum)
"""