# Copy here code of line function from previous exercise

def line(num, sym):
    if sym == "":
        sym = "*"
    print(sym[0] * num)

def triangle(size):
    # You should call function line here with proper parameters
    i = 0
    while i < size:
        i += 1
        line(i, '#')
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
