class MirrorsDomain:
    def __init__(self, input_data):
        self.input_data_parts = input_data.split("\n\n")
        self.mirror_patterns = []

    def parse_input(self):
        for part in self.input_data_parts:
            lines = part.splitlines()
            self.mirror_patterns.append([list(line) for line in lines])

    @staticmethod
    def are_columns_equal(pattern, column1_index, column2_index):
        for line in pattern:
            if line[column1_index] != line[column2_index]:
                return False
        return True

    def find_vertical_reflection_line(self, pattern):
        # a list where are kept the indexes of equal columns identified
        equal_columns_indexes = []

        # search for two consecutive equal columns
        for column_index in range(len(pattern[0]) - 1):
            if self.are_columns_equal(pattern, column_index, column_index + 1):
                equal_columns_indexes.append(column_index)

        index_list = 0
        while index_list < len(equal_columns_indexes):
            # the indexes of the nearby columns
            left_index = equal_columns_indexes[index_list] - 1
            right_index = equal_columns_indexes[index_list] + 2

            # if true then current pattern has a vertical line reflection
            flag = True

            # test nearby columns to see if equal
            while left_index >= 0 and right_index <= len(pattern[0]) - 1:
                if not self.are_columns_equal(pattern, left_index, right_index):
                    flag = False
                    break
                left_index -= 1
                right_index += 1

            # return the positions of reflective columns founded else -1, -1
            if flag:
                return equal_columns_indexes[index_list]
            elif equal_columns_indexes:
                index_list += 1
            else:
                return -1
        return -1

    @staticmethod
    def find_consecutive_rows_with_one_smudge(pattern):
        for row_index in range(len(pattern) - 1):
            smudge_indexes = []
            smudge_count = 0
            for char_index in range(len(pattern[row_index]) - 1):
                if pattern[row_index][char_index] != pattern[row_index + 1][char_index]:
                    smudge_count += 1
                    smudge_indexes.append((char_index, row_index))
            if smudge_count == 1:
                return smudge_indexes[0][1]
        return -1

    @staticmethod
    def find_nonconsecutive_rows_with_one_smudge(top_row, bottom_row, pattern):
        while top_row >= 0 and bottom_row <= len(pattern) - 1:
            smudge_count = 0
            if pattern[top_row] != pattern[bottom_row]:
                for column_index in range(len(pattern[top_row])):
                    if pattern[top_row][column_index] != pattern[bottom_row][column_index]:
                        smudge_count += 1
                if smudge_count == 1:
                    return top_row, bottom_row
            top_row -= 1
            bottom_row += 1
        return -1, -1

    @staticmethod
    def find_consecutive_columns_with_one_smudge(pattern):
        for column_index in range(len(pattern[0]) - 1):
            smudge_count = 0
            smudge_indexes = []
            for row_index in range(len(pattern)):
                if pattern[row_index][column_index] != pattern[row_index][column_index + 1]:
                    smudge_count += 1
                    smudge_indexes.append((row_index, column_index))
            if smudge_count == 1:
                return smudge_indexes[0][1]
        return -1

    @staticmethod
    def find_nonconsecutive_columns_with_one_smudge(left_column, right_column, pattern):
        while left_column >= 0 and right_column <= len(pattern[0]) - 1:
            smudge_count = 0
            for row_index in range(len(pattern)):
                if pattern[row_index][left_column] != pattern[row_index][right_column]:
                    smudge_count += 1
            if smudge_count == 1:
                return left_column, right_column
            left_column -= 1
            right_column += 1
        return -1, -1

    @staticmethod
    def find_horizontal_reflection_line(pattern):
        equal_rows_indexes = []
        # search for two consecutive equal rows
        for row_index in range(len(pattern) - 1):
            if pattern[row_index] == pattern[row_index + 1]:
                equal_rows_indexes.append(row_index)

        index_list = 0
        while index_list < len(equal_rows_indexes):
            # the indexes of the nearby rows
            top_row = equal_rows_indexes[index_list] - 1
            bottom_row = equal_rows_indexes[index_list] + 2

            # if true then current pattern has horizontal line reflection
            flag = True

            # test nearby rows to see if equal
            while top_row >= 0 and bottom_row <= len(pattern) - 1:
                if pattern[top_row] != pattern[bottom_row]:
                    flag = False
                    break
                top_row -= 1
                bottom_row += 1

            if flag:
                return equal_rows_indexes[index_list]
            elif equal_rows_indexes:
                index_list += 1
            else:
                return -1
        return -1

    def simple_reflection_sum(self):
        self.parse_input()
        patterns_sum = 0

        for pattern in self.mirror_patterns:
            column_index = self.find_vertical_reflection_line(pattern)
            if column_index != -1:
                patterns_sum += column_index + 1
            else:
                row_index = self.find_horizontal_reflection_line(pattern)
                patterns_sum += 100 * (row_index + 1)
        print(patterns_sum)

    def test_method(self):
        self.parse_input()
        patterns_sum = 0
        for pattern in self.mirror_patterns:
            # test if it has horizontal simple reflection line
            equal_rows_indexes = []
            # search for two consecutive equal rows
            for row_index in range(len(pattern) - 1):
                if pattern[row_index] == pattern[row_index + 1]:
                    equal_rows_indexes.append(row_index)
            # if there were found horizontal reflection lines
            if equal_rows_indexes:
                possible_row_flag = False
                for possible_row_index in equal_rows_indexes:
                    top_row, bottom_row = self.find_nonconsecutive_rows_with_one_smudge(possible_row_index,
                                                                                        possible_row_index + 1,
                                                                                        pattern)
                    if top_row != -1 and bottom_row != -1:
                        patterns_sum += 100 * (possible_row_index + 1)
                        possible_row_flag = True
                        continue
                if possible_row_flag:
                    continue
                smudged_row_index = self.find_consecutive_rows_with_one_smudge(pattern)
                if smudged_row_index != -1:
                    patterns_sum += 100 * (smudged_row_index + 1)
                    continue
            else:
                smudged_row_index = self.find_consecutive_rows_with_one_smudge(pattern)
                if smudged_row_index != -1:
                    top_row = smudged_row_index - 1
                    bottom_row = smudged_row_index + 2
                    others_equals = True
                    while top_row >= 0 and bottom_row <= len(pattern) - 1:
                        if pattern[top_row] != pattern[bottom_row]:
                            others_equals = False
                            break
                        top_row -= 1
                        bottom_row += 1
                    if others_equals:
                        patterns_sum += 100 * (smudged_row_index + 1)
                        continue
            # if there are no consecutive horizontal reflection lines means that could be smudged
            # if there are no possible horizontal reflection lines, we check for vertical ones
            equal_columns_indexes = []

            # search for two consecutive equal columns
            for column_index in range(len(pattern[0]) - 1):
                if self.are_columns_equal(pattern, column_index, column_index + 1):
                    equal_columns_indexes.append(column_index)

            if equal_columns_indexes:
                possible_column_flag = False
                founded = False
                for possible_column_index in equal_columns_indexes:
                    left_column, right_column = self.find_nonconsecutive_columns_with_one_smudge(
                        possible_column_index, possible_column_index + 1, pattern)
                    if left_column != -1 and right_column != -1:
                        patterns_sum += possible_column_index + 1
                        possible_column_flag = True
                        founded = True
                        continue
                    if founded:
                        break
                if possible_column_flag:
                    continue
                smudged_column_index = self.find_consecutive_columns_with_one_smudge(pattern)
                if smudged_column_index != -1:
                    left_column = smudged_column_index - 1
                    right_column = smudged_column_index + 2
                    while left_column >= 0 and right_column <= len(pattern[0]) - 1:
                        for row_index in range(len(pattern)):
                            if pattern[row_index][left_column] != pattern[row_index[right_column]]:
                                break
                    patterns_sum += (smudged_column_index + 1)
                    continue
            else:
                smudged_column_index = self.find_consecutive_columns_with_one_smudge(pattern)
                if smudged_column_index != -1:
                    patterns_sum += (smudged_column_index + 1)
                    continue
        print(patterns_sum)

    def testing(self):
        self.parse_input()
        for pattern in self.mirror_patterns:
            print(self.find_consecutive_columns_with_one_smudge(pattern))