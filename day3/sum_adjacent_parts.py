class EngineSchematicData:
    DIRECTIONS = [
        (-1, -1),  # Top-left
        (-1, 0),  # Up
        (-1, 1),  # Top-right
        (0, -1),  # Left
        (0, 1),  # Right
        (1, -1),  # Bottom-left
        (1, 0),  # Down
        (1, 1),  # Bottom-right
    ]

    def __init__(self, engine_schematic):
        self.engine_schematic = [list(line) for line in engine_schematic.split("\n")]
        self.processed_locations = set()
        self.total_sum = 0
        self.adjacent_numbers = []

    @staticmethod
    def is_valid_symbol(char):
        return not (char.isdigit() or char == '.')

    def is_adjacent_to_symbol(self, row, col):
        for dx, dy in self.DIRECTIONS:
            if 0 <= row + dx < len(self.engine_schematic) and 0 <= col + dy < len(self.engine_schematic[row + dx]):
                if self.is_valid_symbol(self.engine_schematic[row + dx][col + dy]):
                    return True
        return False

    def compute_engine_sum(self):
        self.total_sum = 0
        for i, row in enumerate(self.engine_schematic):
            j = 0
            while j < len(row):
                if row[j].isdigit() and (i, j) not in self.processed_locations:
                    number, init_j = row[j], j
                    while j + 1 < len(row) and row[j + 1].isdigit():
                        number += row[j + 1]
                        j += 1

                    for col_index in range(init_j, j + 1):
                        self.processed_locations.add((i, col_index))
                        if self.is_adjacent_to_symbol(i, col_index):
                            self.total_sum += int(number)
                            break
                j += 1
        return self.total_sum

    def _get_full_part_number(self, row, col):
        # start with the digit at (row, col)
        number_str = self.engine_schematic[row][col]

        # fan out to the left
        left_col = col - 1
        while left_col >= 0 and self.engine_schematic[row][left_col].isdigit():
            number_str = self.engine_schematic[row][left_col] + number_str
            left_col -= 1

        # fan out to the right
        right_col = col + 1
        while right_col < len(self.engine_schematic[row]) and self.engine_schematic[row][right_col].isdigit():
            number_str += self.engine_schematic[row][right_col]
            right_col += 1

        return int(number_str)

    def _get_gear_ratio(self, row, col):
        self.adjacent_numbers = []
        for dx, dy in self.DIRECTIONS:
            adjacent_row, adjacent_col = row + dx, col + dy
            if 0 <= adjacent_row <= len(self.engine_schematic) and 0 <= adjacent_col <= len(self.engine_schematic[adjacent_row]):
                if self.engine_schematic[adjacent_row][adjacent_col].isdigit():
                    part_number = self._get_full_part_number(adjacent_row, adjacent_col)
                    if part_number not in self.adjacent_numbers:
                        self.adjacent_numbers.append(part_number)
        if len(self.adjacent_numbers) == 2:
            return self.adjacent_numbers[0] * self.adjacent_numbers[1]
        return 0

    def compute_sum_of_all_gear_ratios(self):
        self.total_sum = 0
        for i, row in enumerate(self.engine_schematic):
            for j, char in enumerate(row):
                self.total_sum += self._get_gear_ratio(i, j) if char == "*" else 0

        return self.total_sum
