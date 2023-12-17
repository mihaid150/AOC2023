from collections import deque


class Universe:
    def __init__(self, input_data):
        self.input_data = input_data.splitlines()
        self.expanded_universe = [list(row) for row in self.input_data]  # conversion to list of lists for easy working
        self.galaxies_positions = {}
        self.expansion_rate = 1000000


    def expanse_universe(self):
        # identify free rows
        free_rows = []
        for line_index, line in enumerate(self.expanded_universe):
            if '#' not in line:
                free_rows.append(line_index)

        # duplicate free rows
        for free_row in reversed(free_rows):  # iteration in reverse order to avoid index shifting issues
            self.expanded_universe.insert(free_row, self.expanded_universe[free_row].copy())

        # identify free columns
        free_columns = []
        for column_index in range(len(self.expanded_universe[0])):
            if not any(row[column_index] == '#' for row in self.expanded_universe):
                free_columns.append(column_index)

        # duplicate free columns
        for row in self.expanded_universe:
            for free_column in reversed(free_columns):
                row.insert(free_column, '.')

    def assign_galaxies(self):
        counter = 0

        for index_line, line in enumerate(self.expanded_universe):
            for index_char, char in enumerate(line):
                if char == '#':
                    self.galaxies_positions[counter] = (index_line, index_char)
                    counter += 1

    def is_valid(self, x, y, visited):
        rows, cols = len(self.expanded_universe), len(self.expanded_universe[0])
        return 0 <= x < rows and 0 <= y < cols and not visited[x][y]

    def breadth_first_search(self, start, end):
        # perform bfs to find the shortest path from start to end
        if start == end:
            return 0

        rows, cols = len(self.expanded_universe), len(self.expanded_universe[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        # directions for up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # queue for bfs which stores coordinates and current length path
        queue = deque([(start[0], start[1], 0)])
        visited[start[0]][start[1]] = True

        while queue:
            x, y, dist = queue.popleft()

            # check each direction
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                if self.is_valid(new_x, new_y, visited):
                    if (new_x, new_y) == end:
                        return dist + 1

                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y, dist + 1))

    def sum_shortest_paths_bfs(self):
        # takes a lot of time for computing with bfs for large input so adapted instead to abs
        self.assign_galaxies()
        shortest_paths_sum = 0
        galaxy_numbers = list(self.galaxies_positions.keys())

        # iterate over each unique pair of galaxies
        for i in range(len(galaxy_numbers)):
            for j in range(i + 1, len(galaxy_numbers)):
                galaxy1 = galaxy_numbers[i]
                galaxy2 = galaxy_numbers[j]
                start = self.galaxies_positions[galaxy1]
                end = self.galaxies_positions[galaxy2]

                path_length = self.breadth_first_search(start, end)
                shortest_paths_sum += path_length

        print(shortest_paths_sum)

    @staticmethod
    def abs_path_length(start, end):
        # faster than bsf as time it takes
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

    def sum_shortest_paths_abs(self):
        self.expanse_universe()
        self.assign_galaxies()
        shortest_paths_sum = 0
        galaxy_numbers = list(self.galaxies_positions.keys())
        # iterate over each unique pair of galaxies
        for i in range(len(galaxy_numbers)):
            for j in range(i + 1, len(galaxy_numbers)):
                galaxy1 = galaxy_numbers[i]
                galaxy2 = galaxy_numbers[j]
                start = self.galaxies_positions[galaxy1]
                end = self.galaxies_positions[galaxy2]

                path_length = self.abs_path_length(start, end)
                shortest_paths_sum += path_length

        print(shortest_paths_sum)
