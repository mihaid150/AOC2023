# AOC2023 Day 1 Part 2

from read_input import get_input


def extract_calibration_sum2():
    file_path = "day1/input.txt"

    # A list of possible digits that could be met in the provided input
    spelled_digits = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5), ("six", 6), ("seven", 7),
                      ("eight", 8), ("nine", 9)]

    lines = get_input(file_path).split('\n')
    values_sum = 0

    for line in lines:
        token_list = []

        # All the digits that are in the spelled_digits list are searched and added to the token_list
        for token in spelled_digits:

            # If there are duplicated tokens in one line, we first search all of them and store their positions
            start = 0
            positions = []
            while True:
                start = line.find(token[0], start)
                if start == -1:
                    break
                positions.append(start)
                start += len(token[0])

            # Each position of the duplicated token is added in the token_list
            for position in positions:
                if 0 <= position < len(line):
                    token_list.append((token[1], position))

        # Searching for digits in the line in the format of integers
        i = 0
        for character in line:
            if character.isdigit():
                digit = int(character)
                token_list.append((digit, i))
            i += 1
        token_list = sorted(token_list, key=lambda x: x[1])

        # After searching for all the possible digits, the final number is formed and added to the sum
        if token_list:
            values_sum += token_list[0][0] * 10 + token_list[-1][0]

    print(values_sum)
