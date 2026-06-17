# Write your solution here

def row_correct(sudoku: list, row_no: int):
    checker_list_local = []
    for item in sudoku[row_no]:
        if item in checker_list_local and item != 0:
            return False
        elif item != 0:
            checker_list_local.append(item)
    
    return True

def column_correct(sudoku: list, column_no: int):
    checker_list_local = []
    for row in sudoku:
        if row[column_no] in checker_list_local and row[column_no] != 0:
            return False
        elif row[column_no] != 0:
            checker_list_local.append(row[column_no])
    
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    checker_list_local = []
    for row_local in range(row_no,row_no+3):
        for column_local in range(column_no,column_no+3):
            if sudoku[row_local][column_local] in checker_list_local and sudoku[row_local][column_local] != 0:
                return False
            elif sudoku[row_local][column_local] != 0:
                checker_list_local.append(sudoku[row_local][column_local])

    return True

def sudoku_grid_correct(sudoku: list):

    row_check = True
    column_check = True
    block_check = True

    for row in range(9):
        row_check = row_correct(sudoku,row)
        if not row_check:
            break
    
    if row_check:
        for column in range(9):
            column_check = column_correct(sudoku,column)
            if not column_check:
                break
    else:
        return False
    
    if row_check and column_check:
        for row in range(0,9,3):
            for column in range(0,9,3):
                block_check = block_correct(sudoku,row,column)
                if not block_check:
                    break
            if not block_check:
                    break
    else:
        return False
    
    if row_check and column_check and block_check:
        return True
    else:
        return False



if __name__ == "__main__":


    sudoku1 = [
    [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
    [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
    [ 0, 5, 6, 0, 0, 0, 8, 3, 9 ],
    [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
    [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
    [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
    [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
    [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
    [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))
