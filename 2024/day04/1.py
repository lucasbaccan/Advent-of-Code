import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import utils
import env

year = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
day = os.path.basename(os.path.dirname(__file__)).split("day")[1]
part = os.path.basename(__file__).split(".")[0]


def horizontal_normal_find(data):
    result = 0

    for index, line in enumerate(data):
        line = line.strip()

        # Count the number of "XMAS" in the line
        result += line.count("XMAS")

    return result


def horizontal_recursive_find(data):
    result = 0

    for index, line in enumerate(data):
        line = line.strip()

        # Count the number of "SAMX" in the line
        result += line.count("SAMX")

    return result


def vertical_normal_find(matrix):
    result = 0

    # X
    # M
    # A
    # S

    for index_vertical, line in enumerate(matrix):
        for index_horizontal, char in enumerate(line):
            if char == "X":
                if index_vertical + 3 < len(matrix):
                    if (
                        matrix[index_vertical + 1][index_horizontal] == "M"
                        and matrix[index_vertical + 2][index_horizontal] == "A"
                        and matrix[index_vertical + 3][index_horizontal] == "S"
                    ):
                        result += 1

    return result


def vertical_recursive_find(matrix):
    result = 0

    # S
    # A
    # M
    # X

    for index_vertical, line in enumerate(matrix):
        for index_horizontal, char in enumerate(line):
            if char == "S":
                if index_vertical + 3 < len(matrix):
                    if (
                        matrix[index_vertical + 1][index_horizontal] == "A"
                        and matrix[index_vertical + 2][index_horizontal] == "M"
                        and matrix[index_vertical + 3][index_horizontal] == "X"
                    ):
                        result += 1

    return result


def diagonal_down_find(matrix):
    result = 0

    # X
    #  M
    #   A
    #    S

    for index_vertical, line in enumerate(matrix):
        for index_horizontal, char in enumerate(line):
            if char == "X":
                if index_vertical + 3 < len(matrix) and index_horizontal + 3 < len(line):
                    if (
                        matrix[index_vertical + 1][index_horizontal + 1] == "M"
                        and matrix[index_vertical + 2][index_horizontal + 2] == "A"
                        and matrix[index_vertical + 3][index_horizontal + 3] == "S"
                    ):
                        result += 1

    return result


def diagonal_up_find(matrix):
    result = 0

    #    S
    #   A
    #  M
    # X

    for index_vertical, line in enumerate(matrix):
        if index_vertical < 3:
            continue

        for index_horizontal, char in enumerate(line):
            if char == "S":
                if index_vertical - 3 >= 0 and index_horizontal + 3 < len(line):
                    if (
                        matrix[index_vertical - 1][index_horizontal + 1] == "A"
                        and matrix[index_vertical - 2][index_horizontal + 2] == "M"
                        and matrix[index_vertical - 3][index_horizontal + 3] == "X"
                    ):
                        result += 1

    return result


def diagonal_recursive_down_find(matrix):
    result = 0

    # S
    #  A
    #   M
    #    X

    for index_vertical, line in enumerate(matrix):
        for index_horizontal, char in enumerate(line):
            if char == "S":
                if index_vertical + 3 < len(matrix) and index_horizontal - 3 >= 0:
                    if (
                        matrix[index_vertical + 1][index_horizontal - 1] == "A"
                        and matrix[index_vertical + 2][index_horizontal - 2] == "M"
                        and matrix[index_vertical + 3][index_horizontal - 3] == "X"
                    ):
                        result += 1

    return result


def diagonal_recursive_up_find(matrix):
    result = 0

    #    X
    #   M
    #  A
    # S

    for index_vertical, line in enumerate(matrix):
        if index_vertical < 3:
            continue

        for index_horizontal, char in enumerate(line):
            if char == "X":
                if index_vertical - 3 >= 0 and index_horizontal - 3 >= 0:
                    if (
                        matrix[index_vertical - 1][index_horizontal - 1] == "M"
                        and matrix[index_vertical - 2][index_horizontal - 2] == "A"
                        and matrix[index_vertical - 3][index_horizontal - 3] == "S"
                    ):
                        result += 1

    return result


def run() -> int:
    result = 0
    print(f"Running Day {day} - Part {part}...")
    data = utils.donwload_data(int(year), int(day), env.get_session_cookie())

    ###############################
    # Create a matrix with only the letters
    matrix = []
    for line in data:
        matrix.append([char for char in line.strip()])

    # Horizontal
    result += horizontal_normal_find(data)
    result += horizontal_recursive_find(data)

    # Vertical
    result += vertical_normal_find(matrix)
    result += vertical_recursive_find(matrix)

    # Diagonal Down
    result += diagonal_down_find(matrix)
    result += diagonal_recursive_down_find(matrix)

    # Diagonal Up
    result += diagonal_up_find(matrix)
    result += diagonal_recursive_up_find(matrix)

    ###############################

    print(f"Result of Day {day} - Part {part}: {result}")

    return result


if __name__ == "__main__":
    run()
