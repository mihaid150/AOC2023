# AOC2023 Day 1 Part 1

from read_input import get_input


def extract_calibration_sum():
    file_path = "day1/input.txt"

    lines = get_input(file_path).split('\n')
    values_sum = 0

    for line in lines:
        for character in line:
            if character.isdigit():
                first_digit = int(character)
                break
        for character in reversed(line):
            if character.isdigit():
                last_digit = int(character)
                break
        values_sum += 10 * first_digit + last_digit

    return values_sum
