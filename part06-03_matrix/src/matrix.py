# Suggested solution
def read_matrix():
    with open("matrix.txt") as file:
        m = []
        for row in file:
            mrow = []
            items = row.split(",")
            for item in items:
                mrow.append(int(item))
            m.append(mrow)
 
    return m

def combine(matriisi: list):
    mlist = []
    for row in matriisi:
        mlist += row
    
    return mlist
 
def matrix_sum():
    mlist = combine(read_matrix())
    return sum(mlist)
 
def matrix_max():
    mlist = combine(read_matrix())
    return max(mlist)
 
def row_sums():
    matrix = read_matrix()
    sums = []
    for row in matrix:
        sums.append(sum(row))
    return sums

if __name__ == "__main__":
    read_matrix()
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())
