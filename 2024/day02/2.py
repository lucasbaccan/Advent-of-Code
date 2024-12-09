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

    for line in data:
        numbers = line.split(" ")
        # Convert to numbers
        numbers = [int(number) for number in numbers]

        # Get the size of the numbers
        size = len(numbers)

        # Count how many numbers increase
        increase_count = count_increase_numbers(numbers)
        # Count how many numbers decrease
        decrease_count = count_decrease_numbers(numbers)

        safe = True

        # If the size is not the same size of the increase and decrease count,
        # it means that the numbers are not safe
        if (size - 1) != increase_count and (size - 1) != decrease_count:
            if increase_count > 1 and decrease_count > 1:
                safe = False
                continue

        increase = increase_count > decrease_count
        numbers = normalize_list(numbers, increase)

        for index, number in enumerate(numbers):
            # Skip last number
            if index == len(numbers) - 1:
                break

            next_number = int(numbers[index + 1])

            diff = abs(number - next_number)

            if diff == 0 or diff > 3:
                safe = False
                break

        if safe:
            result += 1

    print(f"Result of Day {day} - Part {part}: {result}")

    return result


def count_increase_numbers(numbers: list):
    size = len(numbers)
    increase_count = 0

    for index, number in enumerate(numbers):
        if index == size - 1:
            break

        next_number = numbers[index + 1]

        if next_number > number:
            increase_count += 1

    return increase_count


def count_decrease_numbers(numbers: list):
    size = len(numbers)
    decrease_count = 0

    for index, number in enumerate(numbers):
        if index == size - 1:
            break

        next_number = numbers[index + 1]

        if next_number < number:
            decrease_count += 1

    return decrease_count


def normalize_list(numbers: list, increase: bool):
    final_list = []
    remove = False
    for index, number in enumerate(numbers):
        # Find the wrong number in the list and remove it
        if index == len(numbers) - 1:
            break

        next_number = int(numbers[index + 1])

        if increase:
            if next_number < number:
                remove = True
        else:
            if next_number > number:
                remove = True

        if remove:
            remove = False
            if index == len(numbers) - 2:
                final_list.append(number)

            continue

        final_list.append(number)

    print("ORIGINAL:", numbers)
    print("FINAL   :", final_list)

    return final_list


if __name__ == "__main__":
    run()
