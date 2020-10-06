import math

import numpy as np
import csv


def get_puzzles(filename):
    """
    Reads the given csv and makes numpy array sudoku boards
    :param filename: Name of csv file
    :return: List of tuples containing both the board and solution of numpy boards
    """
    csv_dict = csv.DictReader(open(filename))

    boards = []
    solutions = []
    for line in csv_dict:
        boards += [make_np_board(line['Puzzle'])]
        solutions += [make_np_board(line['Solution'])]

    return [i for i in zip(boards, solutions)]


def make_np_board(puzzle_str):
    DIM = int(math.sqrt(len(puzzle_str)))
    board = np.zeros((DIM, DIM), int)
    i = 0
    for r in range(DIM):
        for c in range(DIM):
            if puzzle_str[i] != '.':
                board[r][c] = int(puzzle_str[i])
            i += 1
    return board


if __name__ == "__main__":
    training_puzzles = get_puzzles("puzzle.csv")

    for puzzle in training_puzzles:
        print(puzzle[0])
        print(puzzle[1])
