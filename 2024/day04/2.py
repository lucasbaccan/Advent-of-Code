import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import utils
import env

year = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
day = os.path.basename(os.path.dirname(__file__)).split("day")[1]
part = os.path.basename(__file__).split(".")[0]


def run() -> int:
    result = 0
    print(f"Running Day {day} - Part {part}...")
    data = utils.donwload_data(int(year), int(day), env.get_session_cookie())

    ###############################
    # Create a matrix with only the letters
    matrix = []
    for line in data:
        matrix.append([char for char in line.strip()])

    for horizontal_index, line in enumerate(matrix):
        # Skip the first line
        if horizontal_index == 0:
            continue

        # Skip the last line
        if horizontal_index == len(matrix) - 1:
            continue

        for vertical_index, char in enumerate(line):
            # Skip the first element of the line
            if vertical_index == 0:
                continue

            # Skip the last element of the line
            if vertical_index == len(line) - 1:
                continue

            # Check if is an "A" in the matrix
            if char == "A":
                # M M
                #  A
                # S S
                if (
                    matrix[horizontal_index - 1][vertical_index - 1] == "M"
                    and matrix[horizontal_index - 1][vertical_index + 1] == "M"
                    and matrix[horizontal_index + 1][vertical_index - 1] == "S"
                    and matrix[horizontal_index + 1][vertical_index + 1] == "S"
                ):
                    result += 1

                # S S
                #  A
                # M M
                if (
                    matrix[horizontal_index - 1][vertical_index - 1] == "S"
                    and matrix[horizontal_index - 1][vertical_index + 1] == "S"
                    and matrix[horizontal_index + 1][vertical_index - 1] == "M"
                    and matrix[horizontal_index + 1][vertical_index + 1] == "M"
                ):
                    result += 1

                # M S
                #  A
                # M S
                if (
                    matrix[horizontal_index - 1][vertical_index - 1] == "M"
                    and matrix[horizontal_index - 1][vertical_index + 1] == "S"
                    and matrix[horizontal_index + 1][vertical_index - 1] == "M"
                    and matrix[horizontal_index + 1][vertical_index + 1] == "S"
                ):
                    result += 1

                # S M
                #  A
                # S M
                if (
                    matrix[horizontal_index - 1][vertical_index - 1] == "S"
                    and matrix[horizontal_index - 1][vertical_index + 1] == "M"
                    and matrix[horizontal_index + 1][vertical_index - 1] == "S"
                    and matrix[horizontal_index + 1][vertical_index + 1] == "M"
                ):
                    result += 1

    ###############################

    print(f"Result of Day {day} - Part {part}: {result}")

    return result


if __name__ == "__main__":
    run()
