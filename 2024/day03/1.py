import sys
import os
import re

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

    # Regext to match '(mul\(\d{1,3}\,\d{1,3}\))'
    regex = r"(mul\(\d{1,3}\,\d{1,3}\))"

    # Find all matches in the data
    for line in data:
        matches = re.findall(regex, line)
        for match in matches:
            number1 = int(match.split("(")[1].split(",")[0])
            number2 = int(match.split(",")[1].split(")")[0])
            result += number1 * number2

    ###############################

    print(f"Result of Day {day} - Part {part}: {result}")

    return result


if __name__ == "__main__":
    run()
