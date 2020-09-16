# This program solves Sudoku
# Based on backtracking algorithm
# Inspired by Numberphile

# Correct Sudoku
# sudoku = [
#     [5, 8, 1, 6, 7, 2, 4, 3, 9],
#     [7, 9, 2, 8, 4, 3, 6, 5, 1],
#     [3, 6, 4, 5, 9, 1, 7, 8, 2],
#     [4, 3, 8, 9, 5, 7, 2, 1, 6],
#     [2, 5, 6, 1, 8, 4, 9, 7, 3],
#     [1, 7, 9, 3, 2, 6, 8, 4, 5],
#     [8, 4, 5, 2, 1, 9, 3, 6, 7],
#     [9, 1, 3, 7, 6, 8, 5, 2, 4],
#     [6, 2, 7, 4, 3, 5, 1, 9, 8]
# ]

# Sudoku to solve
sudoku = [
    [5, 8, 0, 6, 0, 0, 4, 0, 0],
    [7, 0, 0, 0, 0, 3, 6, 0, 0],
    [0, 0, 0, 0, 9, 1, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 1, 8, 0, 0, 0, 3],
    [0, 0, 0, 3, 0, 6, 0, 4, 5],
    [0, 4, 0, 2, 0, 0, 0, 6, 0],
    [9, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 1, 0, 0]
]

solved_sudoku = list(sudoku)

correct_set = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def possible(sudoku, x, y, number):
    square_number = 0
    if x <= 2:
        if y <= 2:
            square_number = 0
        if y > 2 and y <= 5:
            square_number = 1
        if y > 5 and y <= 8:
            square_number = 2
    if x > 2 and x <= 5:
        if y <= 2:
            square_number = 3
        if y > 2 and y <= 5:
            square_number = 4
        if y > 5 and y <= 8:
            square_number = 5
    if x > 5 and x <= 8:
        if y <= 2:
            square_number = 6
        if y > 2 and y <= 5:
            square_number = 7
        if y > 5 and y <= 8:
            square_number = 8
    # print(square_number)

    if number in sudoku[x]:
        return False
    elif number in reverse_sudoku(sudoku)[y]:
        return False
    elif number in sudoku_squares_to_rows(sudoku)[square_number]:
        return False
    else:
        return True


def check_rows(sudoku):
    check_handler = []
    rows = [False]*9
    for i, row in enumerate(sudoku):
        for j, number in enumerate(row):
            check_handler.append(number)
            if j == 8:
                check_handler.sort()
                if check_handler == correct_set:
                    rows[i] = True
                    # print(f'Row {i+1} is correct')
                else:
                    rows[i] = False
                    # print(f'Mistake in row {i+1}')
                check_handler = []
    return rows


def check_columns(sudoku):
    reversed_sudoku = reverse_sudoku(sudoku)
    columns = check_rows(reversed_sudoku)
    return columns


def reverse_sudoku(sudoku):
    reversed_sudoku = [[]for _ in range(9)]
    for row in sudoku:
        for j, number in enumerate(row):
            reversed_sudoku[j].append(number)
    return reversed_sudoku


def sudoku_squares_to_rows(sudoku):
    sudoku_squares = [[]for _ in range(9)]
    for i, row in enumerate(sudoku):
        for j, number in enumerate(row):
            # od i 0 - 2 pierwsze 3 kwadraty
            # print(j)
            if i <= 2:
                if j <= 2:
                    sudoku_squares[0].append(number)
                if j > 2 and j <= 5:
                    sudoku_squares[1].append(number)
                if j > 5 and j <= 8:
                    sudoku_squares[2].append(number)
            # od i 3 - 5 kolejne 3 kwadraty
            if i > 2 and i <= 5:
                if j <= 2:
                    sudoku_squares[3].append(number)
                if j > 2 and j <= 5:
                    sudoku_squares[4].append(number)
                if j > 5 and j <= 8:
                    sudoku_squares[5].append(number)
            # od i 6 - 8 kolejne 3 kwadraty
            if i > 5 and i <= 8:
                if j <= 2:
                    sudoku_squares[6].append(number)
                if j > 2 and j <= 5:
                    sudoku_squares[7].append(number)
                if j > 5 and j <= 8:
                    sudoku_squares[8].append(number)

    return sudoku_squares


def check_squares(sudoku):
    sudoku_squares = sudoku_squares_to_rows(sudoku)
    squares = check_rows(sudoku_squares)
    return squares


def check_sudoku(sudoku):
    rows = check_rows(sudoku)
    columns = check_columns(sudoku)
    squares = check_squares(sudoku)
    if all(rows) and all(columns) and all(squares):
        return True


def solve_sudoku(sudoku):
    global solved_sudoku
    if check_sudoku(solved_sudoku):
        print(solved_sudoku)
        return True

    for i, row in enumerate(sudoku):
        for j, number in enumerate(row):
            if i == len(solved_sudoku) and j == len(solved_sudoku[0]):
                print(solved_sudoku)
                return
            if number == 0:
                for guess in range(1, 10):
                    if possible(solved_sudoku, i, j, guess):
                        solved_sudoku[i][j] = guess
                        if solve_sudoku(solved_sudoku):
                            return True
                        solved_sudoku[i][j] = 0
                return False


solve_sudoku(sudoku)
