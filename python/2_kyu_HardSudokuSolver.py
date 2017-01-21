"""
2 kyu: Hard Sudoku Solver
https://www.codewars.com/kata/5588bd9f28dbb06f43000085/train/python
"""


def sudoku_solver(puzzle):
    if len(puzzle) != 9:
        raise Exception()

    if any([len(r) != 9 for r in puzzle]):
        raise Exception()

    zeros = sum([c.count(0) for c in [r for r in puzzle]])
    if 81 - zeros < 17:
        raise Exception()

    for r in range(len(puzzle)):
        for c in range(len(puzzle[r])):
            if puzzle[r][c] != 0:
                continue
            for num in range(1, 10):
                if check_num(puzzle, r, c, num):
                    puzzle[r][c] = num
                    if not sudoku_solver(puzzle):
                        continue

                    return puzzle
            puzzle[r][c] = 0
            return False
    return puzzle


def check_num(puzzle, row, col, num):
    if num in puzzle[row]:
        return False

    for r in puzzle:
        if num == r[col]:
            return False

    for r in get_range(row):
        for c in get_range(col):
            if num == puzzle[r][c]:
                return False

    return True


def get_range(n):
    if n >= 6:
        return range(6, 9)

    if n >= 3:
        return range(3, 6)

    return range(3)


p = [[0, 0, 6, 1, 0, 0, 0, 0, 8],
     [0, 8, 0, 0, 9, 0, 0, 3, 0],
     [2, 0, 0, 0, 0, 5, 4, 0, 0],
     [4, 0, 0, 0, 0, 1, 8, 0, 0],
     [0, 3, 0, 0, 7, 0, 0, 4, 0],
     [0, 0, 7, 9, 0, 0, 0, 0, 3],
     [0, 0, 8, 4, 0, 0, 0, 0, 6],
     [0, 2, 0, 0, 5, 0, 0, 8, 0],
     [1, 0, 0, 0, 0, 2, 5, 0, 0]]
print(sudoku_solver(p))
