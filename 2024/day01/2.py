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

    list1 = []
    list2 = []

    for line in data:
        part1, part2 = line.split()

        list1.append(int(part1))
        list2.append(int(part2))

    diff_total = 0

    for index in range(len(list1)):
        number1 = list1[index]
        number2_count = list2.count(number1)

        diff_total += number1 * number2_count

    result = diff_total

    print(f"Result of Day {day} - Part {part}: {result}")

    return result


if __name__ == "__main__":
    run()
