import re
from itertools import chain, combinations
from functools import cache


class HotSprings:
    def __init__(self, input_data):
        self.input_data = input_data.splitlines()

    @staticmethod
    def powerset(unknown_list):
        # [0, 1, 2] -> (0, ), (1, ), (2, ), (0, 1), (0, 2), (1, 2), (0, 1, 2)
        return chain.from_iterable(combinations(unknown_list, r) for r in range(len(unknown_list) + 1))

    def generate_damaged_springs(self, line):
        # "???.### 1,1,3" -> [
        # #     ["###"],
        # #     ["#", "###"],
        # #     ["#", "###"],
        # #     ["#", "###"],
        # #     ["##", "###"],
        # #     ["#", "#", "###"],
        # #     ["##", "###"],
        # #     ["###", "###"],
        # # ]
        unknown_indexes = [index for index, char in enumerate(line) if char == "?"]
        for indexes_to_replace in self.powerset(unknown_indexes):
            chars = list(line)
            for i in indexes_to_replace:
                chars[i] = "#"
            yield re.findall(r"#+", ''.join(chars).replace("?", "."))

    @staticmethod
    def check_valid_arrangements(arrangement, springs_shape):
        # ['#', '#', '###'], [1, 1, 3] -> True
        return (len(arrangement) == len(springs_shape)
                and all(len(arrangement_element) == shape for arrangement_element, shape in zip(arrangement, springs_shape)))

    def count_valid_line_arrangements(self, line):
        springs, springs_numbers = line.split()
        springs_shape = list(map(int, springs_numbers.split(',')))

        return sum(self.check_valid_arrangements(arrangement, springs_shape) for arrangement in self.generate_damaged_springs(line))

    def sum_valid_springs_arrangements(self):
        count = 0
        for line in self.input_data:
            count += self.count_valid_line_arrangements(line)
        return count

    @cache
    def count_valid_solutions(self, line, springs_shape):
        # where line = "???.###" and arrangement = ['#', '#', '###'], [1, 1, 3]
        if not line:
            # if there are no more spots to check -> all damaged springs accounted
            return len(springs_shape) == 0
        if not springs_shape:
            # if there are no more damaged springs and could be operational ones, then valid arrangement
            return '#' not in line

        # for this step of the recursive loop, it extracts the first char and rest of the string from the given one
        char, rest_of_line = line[0], line[1:]
        if char == '.':
            # ignore dots because they don't affect the damaged spring groups, keep recursion
            return self.count_valid_solutions(rest_of_line, springs_shape)
        if char == '#':
            # if the current spring is damaged(starts with #), check whether the current group of springs could start at this position based on the spring shape
            current_spring_shape = springs_shape[0]
            # to be valid, there need to be
            if (
                    # long enough
                    len(line) >= current_spring_shape
                    # ensure no operation springs in the group
                    and all(c != '.' for c in line[:current_spring_shape])
                    # check the end of the group is an operational spring or end of line
                    and (len(line) == current_spring_shape or line[current_spring_shape] != '#')
            ):
                # if valid, call recursive the function for the next springs and next springs shape
                # line[current_spring_shape + 1:] means exclude the current group(current_spring_shape), springs_shape[1:] means go to the next shape
                return self.count_valid_solutions(line[current_spring_shape + 1:], springs_shape[1:])
            return 0
        if char == "?":
            # explore both opportunities for damaged or operational spring
            # makes 2 recursive calls assuming in each that the spring is either operational or either damaged so all the possible valid arrangements
            return self.count_valid_solutions(f"#{rest_of_line}", springs_shape) + self.count_valid_solutions(f".{rest_of_line}", springs_shape)

    def count_valid_line_arrangements2(self, line):
        springs, springs_numbers = line.split()
        springs_shape = tuple(map(int, springs_numbers.split(',')))

        # developed the springs 5 time larger for part 2
        springs = '?'.join([springs] * 5)
        springs_shape *= 5

        return self.count_valid_solutions(springs, springs_shape)

    def sum_valid_springs_arrangements2(self):
        count = 0
        for line in self.input_data:
            count += self.count_valid_line_arrangements2(line)
        return count
