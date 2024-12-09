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

    result = 0

    for line in data:
        # Remove all the non-digit characters
        numbers = "".join(filter(str.isdigit, line))

        first_number = numbers[0]
        last_number = numbers[-1]

        concatenated = first_number + last_number
        result += int(concatenated)

    ###############################

    print(f"Result of Day {day} - Part {part}: {result}")

    return result


if __name__ == "__main__":
    run()
