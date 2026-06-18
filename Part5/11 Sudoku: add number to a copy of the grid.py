# Write your solution here
def print_sudoku(sudoku: list):

    for row_no in range(9):
        for column_no in range(9):
            
            if sudoku[row_no][column_no] == 0:
                    print("_", end=" ")
            else:
                print(f"{sudoku[row_no][column_no]}", end=" ")

            if (column_no+1) % 3 == 0:
                print(" ", end="")
        print()
        if (row_no+1) % 3 == 0:
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_list_local = []
    for row in sudoku:
        new_list_local.append(row[:])

    new_list_local[row_no][column_no] = number
    return new_list_local

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
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
