class Universe:
    def __init__(self, input_data):
        self.input_data = input_data.splitlines()
        self.galaxies_positions = self.get_galaxies_positions()
        self.empty_rows = self.get_empty_rows()
        self.empty_columns = self.get_empty_columns()
        self.expansion_rate = 1000000

    def get_galaxies_positions(self):
        galaxies_positions = []
        for row_index, row in enumerate(self.input_data):
            for col_index, char in enumerate(row):
                if char == '#':
                    galaxies_positions.append((row_index, col_index))
        return galaxies_positions

    def get_empty_rows(self):
        return [index for index, row in enumerate(self.input_data) if '#' not in row]

    def get_empty_columns(self):
        columns = zip(*self.input_data)
        return [index for index, column in enumerate(columns) if '#' not in column]

    def calculate_path_length(self, start, end):
        path_length = 0

        # Vertical distance
        for row in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
            path_length += self.expansion_rate if row in self.empty_rows else 1

        # Horizontal distance
        for col in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
            path_length += self.expansion_rate if col in self.empty_columns else 1

        return path_length

    def sum_shortest_paths(self):
        total_path_length = 0
        for i, galaxy1 in enumerate(self.galaxies_positions):
            for galaxy2 in self.galaxies_positions[i + 1:]:
                total_path_length += self.calculate_path_length(galaxy1, galaxy2)

        return total_path_length
