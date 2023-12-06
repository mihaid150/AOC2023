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
