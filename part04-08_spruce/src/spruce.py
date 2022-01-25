# Write your solution here
def spruce(n):
    print("a spruce!")
    for i in range(1, n + 1):
        print(" " *(n - i) + "*" * (2 * i - 1))
    print(" " * (n - 1) + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)

"""Suggested solution
def spruce(height):
    print("a spruce!")
    i = 1
    while i <= height:
        empty = height - i
        stars = 2 * i - 1
        print(" " * empty + "*" * stars)
        i += 1
    print(" " * (height - 1) + "*")
"""