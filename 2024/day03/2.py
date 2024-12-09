import sys
import os
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import utils
import env

year = os.path.basename(os.path.dirname(os.path.dirname(__file__)))
day = os.path.basename(os.path.dirname(__file__)).split("day")[1]
part = os.path.basename(__file__).split(".")[0]


def find_first_do(line: str) -> int:
    # Find the first 'do()' in the line
    return line.find("do()")


def find_last_do(line: str) -> int:
    # Find the first 'do()' in the line
    return line.rfind("do()")


def find_first_dont(line: str) -> int:
    # Find the first 'dont()' in the line
    return line.find("don't()")


def find_last_dont(line: str) -> int:
    # Find the first 'dont()' in the line
    return line.rfind("don't()")


def run() -> int:
    result = 0
    print(f"Running Day {day} - Part {part}...")
    data = utils.donwload_data(int(year), int(day), env.get_session_cookie())

    ###############################

    # Regext to match '(mul\(\d{1,3}\,\d{1,3}\))'
    regex = r"(mul\(\d{1,3}\,\d{1,3}\))"

    enabled = True
    last_match_index = 0

    # Find all matches in the data
    for line in data:
        matches = re.findall(regex, line)

        for match in matches:

            # Todas as execuções até o "dont()" são válidas
            skip = False

            match_index = line.find(match)

            # if match_index > find_first_dont(line) and match_index < find_last_do(line):
            #     line = line[last_match_index  :]
            #     match_index = line.find(match)

            first_do = find_first_do(line)
            first_dont = find_first_dont(line)

            print("Index: ", match_index, "\tFirst do: ", first_do, "\tFirst dont: ", first_dont)

            line_print = line[: min(first_do + 4, first_dont + 6)]
            print("============")
            print(line_print)
            print("============")

            if first_dont < match_index and first_do > match_index:
                skip = True

            if not skip:
                print(f"VALID:\t {match}")

                number1 = int(match.split("(")[1].split(",")[0])
                number2 = int(match.split(",")[1].split(")")[0])
                result += number1 * number2

                last_match_index = match_index + len(match)

            else:
                print(f"SKIPED:\t {match}")

            # remove the pos 0 until the end of the match from the line
            # line = line[match_index + len(match):]

            if first_do > match_index and first_dont > match_index:
                line = line[last_match_index :]


    ###############################

    print(f"Result of Day {day} - Part {part}: {result}")

    return result


if __name__ == "__main__":
    run()
