import numpy as np

import data

PUZZLE_STR = ".......19..4..8...9...468...6..24..3..........1..63..83...816....5..7..........54"
DIM = 9
SQUARE_DIM = 3

runs = 0


def main():
    puzzle = data.make_np_board(PUZZLE_STR)
    print(puzzle)

    sol = solve(puzzle, 0, 0)
    print('\n', sol)
    print(runs)


def solve(puzzle, r, c):
    global runs
    runs += 1
    if c == 0 and r == DIM:
        return puzzle
    else:
        if puzzle[r][c] == 0:
            for i in range(1, DIM + 1):
                if is_valid(puzzle, i, r, c):
                    puzzle[r][c] = i

                    # Iterate r and c
                    next_c = c + 1
                    next_r = r
                    if next_c == DIM:
                        next_c = 0
                        next_r = r + 1

                    # Solve at the next space and return the solution
                    # If no solution, try the next i
                    sol = solve(np.copy(puzzle), next_r, next_c)
                    if sol is not None:
                        return sol
            # All possibilities for this space don't work, thus current config is bad
            # Causes backtracking to occur
            return None
        else:
            # Skip a space that's already filled it
            # Iterate r and c
            c += 1
            if c == DIM:
                c = 0
                r += 1
            return solve(puzzle, r, c)


def is_valid(puzzle, i, r, c):
    if (i in puzzle[r]) or (i in puzzle[:, c]) or (i in get_square(puzzle, r, c)):
        return False
    else:
        return True


def get_square(puzzle, r, c):
    r = (r // SQUARE_DIM) * SQUARE_DIM
    c = (c // SQUARE_DIM) * SQUARE_DIM
    return puzzle[r:r+SQUARE_DIM, c:c+SQUARE_DIM]


if __name__ == "__main__":
    main()
