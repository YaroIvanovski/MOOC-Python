# Copy here code of line function from previous exercise and use it in your solution
def line(num, sym):
    if sym == "":
        sym = "*"
    print(sym[0] * num)

def shape(num, sym, num2, sym2):
    i = 1
    while i <= num:
        line(i, sym)
        i += 1

    i = 1
    while i <= num2:
        line(num, sym2)
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")