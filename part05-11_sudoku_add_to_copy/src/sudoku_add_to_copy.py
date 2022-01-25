# Write your solution here
def print_sudoku(sudoku: list):
    r = 0
    for row in sudoku:
        s = 0
        for num in row:
            s += 1
            if num == 0:
                num = "_"
            m = f"{num} "
            if s % 3 == 0 and s < 8:
                m += " "
            print(m, end = "")
 
        print()
        r += 1
        if r % 3 == 0 and r < 8:
            print ()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    x = []
    for r in sudoku:
        x.append(r[:])
 
    x[row_no][column_no] = number
    return x


if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)