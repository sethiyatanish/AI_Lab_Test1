def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))


def is_valid(board, row, col, num):
    # Check the row
    for j in range(9):
        if board[row][j] == num:
            return False

    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Find the top-left corner of the 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    # Check the 3x3 subgrid
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):
    # Find an empty cell
    for row in range(9):
        for col in range(9):

            if board[row][col] == 0:

                # Try digits 1 through 9
                for num in range(1, 10):

                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        # Recursively solve the remaining cells
                        if solve_sudoku(board):
                            return True

                        # Undo the choice if it leads to failure
                        board[row][col] = 0

                # No digit works in this cell
                return False

    # No empty cells remain
    return True


# Example Sudoku puzzle; 0 represents an empty cell
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Original Sudoku:")
print_board(board)

if solve_sudoku(board):
    print("\nSolved Sudoku:")
    print_board(board)
else:
    print("\nNo solution exists.")
