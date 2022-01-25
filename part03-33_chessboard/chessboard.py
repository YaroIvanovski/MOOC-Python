# Write your solution here
def chessboard(size):
    i = 0
    while i < size:
        if i % 2 == 0:
            line = "10" * size
        else:
            line = "01" * size
        print(line[0:size])
        i += 1
    
# Testing the function
if __name__ == "__main__":
    chessboard(3)
