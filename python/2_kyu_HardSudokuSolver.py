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

    get_all_candidates(puzzle)

    return try_all_candidates(puzzle)


def try_all_candidates(puzzle):
    for r in range(9):
        for c in range(9):
            num = puzzle[r][c]
            if is_fix_num(num):
                continue
            for i in num:
                if not check_num(puzzle, r, c, i):
                    continue
                puzzle[r][c] = i
                cleanup_candidates(puzzle)
                get_all_candidates(puzzle)
                try:
                    if not try_all_candidates(puzzle):
                        continue
                except ValueError:
                    continue

                return puzzle
            puzzle[r][c] = num
            return False
    return puzzle


def cleanup_candidates(puzzle):
    for r in range(9):
        for c in range(9):
            if type(puzzle[r][c]) is list:
                puzzle[r][c] = []


def get_all_candidates(puzzle):
    for r in range(9):
        for c in range(9):
            num = puzzle[r][c]
            if is_fix_num(num):
                continue
            candidates = []
            for i in range(1, 10):
                if check_num(puzzle, r, c, i):
                    candidates.append(i)
            if len(candidates) == 0:
                raise ValueError()
            puzzle[r][c] = candidates
            if len(candidates) == 1:
                get_all_candidates(puzzle)


def is_fix_num(num):
    return (isinstance(num, int) and num != 0) or (isinstance(num, list) and len(num) == 1)


def is_one_num_list(num):
    return type(num) is list and len(num) == 1


def is_equal_to_num_or_candidate(num, candidate):
    return num == candidate or (is_one_num_list(num) and num[0] == candidate)


def check_num(puzzle, row, col, num):
    for i in puzzle[row]:
        if is_equal_to_num_or_candidate(i, num):
            return False

    for r in puzzle:
        if is_equal_to_num_or_candidate(r[col], num):
            return False

    for r in get_range(row):
        for c in get_range(col):
            if is_equal_to_num_or_candidate(puzzle[r][c], num):
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
