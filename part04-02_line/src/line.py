# Write your solution here
def line(num, sym):
    if sym == "":
        sym = "*"
    print(sym[0] * num)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "X")
    line(5, "-")
    line(3, "")