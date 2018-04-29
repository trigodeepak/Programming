#Program to solve the sudoku
a = [[0,9,0,0,0,0,0,0,5],
     [0,8,07,0,0,05,0,0,0],
     [02,0,0,06,04,0,03,0,0],
     [0,02,0,9,0,0,0,04,0],
     [0,03,0,0,8,0,0,06,0],
     [0,04,0,0,0,06,0,07,0],
     [0,0,9,0,3,8,0,0,04],
     [0,0,0,5,0,0,6,3,0],
     [3,0,0,0,0,0,0,1,0]]

def check_in_row(row,item):
    if item in a[row]:
        return True
    else:
        return False
def check_in_column(col,item):
    for i in xrange(9):
        if a[i][col] == item:
            return True
    return False

def used_in_box(row,col,item):
    for i in range(3):
        for j in range(3):
            if(a[i+row][j+col] == item):
                return True
    return False

def safe_insert(row,col,item):
    return not check_in_column(col,item) and not check_in_row(row,item) and not used_in_box(row - row%3,col-col%3,item)

def find_row_column(l):
    for i in xrange(9):
        for j in xrange(9):
            if a[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False

def Solve_sudoku():
    l = [0,0]
    if (not find_row_column(l)):
        return True

    row = l[0]
    col = l[1]

    for i in xrange(1,10):
        if(safe_insert(row,col,i)):
            a[row][col] = i

            if(Solve_sudoku()):
                return True

            a[row][col] = 0

    return False

if Solve_sudoku():
    for i in a:
        print i
