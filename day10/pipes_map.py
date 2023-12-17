class Pipes:
    directions = [
        (-1, 0),  # top
        (1, 0),  # bottom
        (0, -1),  # left
        (0, 1)  # right
    ]

    def __init__(self, input_data):
        self.input_data = input_data.splitlines()
        self.pipes_map = []
        self.source_position = None

    def parse_input(self):
        for line in self.input_data:
            current_line = []
            for tile in line:
                current_line.append([tile, -1])
            self.pipes_map.append(current_line)

    def test_tile(self, char, line_index, tile_index, direction):
        if char == '-':
            if direction == (0, -1): # left
                if self.pipes_map[line_index][tile_index - 1][0] in ['F', 'L', 'S', '-']:
                    return True
                else:
                    return False
            elif direction == (0, 1): # right
                if self.pipes_map[line_index][tile_index + 1][0] in ['J', '7', 'S', '-']:
                    return True
                else:
                    return False
            else:
                return False
        elif char == '|':
            if direction == (-1, 0): # top
                if self.pipes_map[line_index - 1][tile_index][0] in ['F', '7', 'S', '|']:
                    return True
                else:
                    return False
            elif direction == (1, 0): # bottom
                if self.pipes_map[line_index + 1][tile_index][0] in ['L', 'J', 'S', 'I']:
                    return True
                else:
                    return False
            else:
                return False
        elif char == 'J':
            if direction == (-1, 0): # top
                if self.pipes_map[line_index - 1][tile_index][0] in ['7', 'F', 'S', '|']:
                    return True
                else:
                    return False
            elif direction == (0, -1): # left
                if self.pipes_map[line_index][tile_index - 1][0] in ['F', 'L', 'S', '-']:
                    return True
                else:
                    return False
            else:
                return False
        elif char == 'F':
            if direction == (0, 1): # right
                if self.pipes_map[line_index][tile_index + 1][0] in ['-', 'S', 'J', '7']:
                    return True
                else:
                    return False
            elif direction == (1, 0): # bottom
                if self.pipes_map[line_index + 1][tile_index][0] in ['|', 'L', 'S', 'J']:
                    return True
                else:
                    return False
            else:
                return False
        elif char == 'L':
            if direction == (-1, 0): # top
                if self.pipes_map[line_index - 1][tile_index][0] in ['|', 'S', 'F', '7']:
                    return True
                else:
                    return False
            elif direction == (0, 1): # right
                if self.pipes_map[line_index][tile_index + 1][0] in ['-', '7', 'S', 'J']:
                    return True
                else:
                    return False
            else:
                return False
        elif char == '7':
            if direction == (0, -1): # left
                if self.pipes_map[line_index][tile_index - 1][0] in ['-', 'S', 'F', 'L']:
                    return True
                else:
                    return False
            elif direction == (1, 0): # bottom
                if self.pipes_map[line_index + 1][tile_index][0] in ['|', 'L', 'S', 'J']:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def find_source_pipe(self):
        self.parse_input()
        for index_line, pipe_line in enumerate(self.pipes_map, start=0):
            for index_tile, tile in enumerate(pipe_line, start=0):
                if tile[0] == 'S':
                    tile[1] = 0
                    self.source_position = (index_line, index_tile)

        # traversing source line
        source_line = self.pipes_map[self.source_position[0]]
        for index_tile, tile in enumerate(source_line, start=0):
            if tile[0] != '.' and tile[0] != 'S':
                for direction in self.directions:
                    dx, dy = direction
                    x = self.source_position[0] + dx
                    y = index_tile + dy
                    if x < 0:
                        x = 0
                    if x >= len(self.pipes_map):
                        x = len(self.pipes_map) - 1
                    if y < 0:
                        y = 0
                    if y >= len(source_line):
                        y = len(source_line) - 1
                    if self.pipes_map[x][y][1] != -1 and self.test_tile(tile[0], self.source_position[0], index_tile, direction):
                        value = self.pipes_map[x][y][1]
                        self.pipes_map[self.source_position[0]][index_tile][1] = value + 1

    def check_map(self):
        for line in self.pipes_map:
            for tile in line:
                if tile[0] != '.' and tile[1] == -1:
                    return False
        return True

    def max_map(self):
        max_tile = -1
        for line in self.pipes_map:
            for tile in line:
                if tile[1] > max_tile:
                    max_tile = tile[1]
        return max_tile

    def traverse_map(self):
        self.find_source_pipe()

        while True:
            index_line = self.source_position[0] + 1
            for line in self.pipes_map[self.source_position[0] + 1:]:
                for index_tile, tile in enumerate(line, start=0):
                    if tile[0] != '.':
                        for direction in self.directions:
                            dx, dy = direction
                            x = index_line + dx
                            y = index_tile + dy
                            if x < 0:
                                x = 0
                            if x >= len(self.pipes_map):
                                x = len(self.pipes_map) - 1
                            if y < 0:
                                y = 0
                            if y >= len(line):
                                y = len(line) - 1
                            if self.pipes_map[x][y][1] != -1 and self.test_tile(tile[0], index_line, index_tile, direction) and self.pipes_map[index_line][index_tile][1] == -1:
                                value = self.pipes_map[x][y][1]
                                self.pipes_map[index_line][index_tile][1] = value + 1
                index_line += 1

            first_pipes = list(reversed(self.pipes_map[:self.source_position[0]]))

            index_line = self.source_position[0] - 1

            for line in first_pipes:
                for index_tile, tile in enumerate(line, start=0):
                    if tile[0] != '.':
                        for direction in self.directions:
                            dx, dy = direction
                            x = index_line + dx
                            y = index_tile + dy
                            if x < 0:
                                x = 0
                            if x >= len(self.pipes_map):
                                x = len(self.pipes_map) - 1
                            if y < 0:
                                y = 0
                            if y >= len(line):
                                y = len(line) - 1
                            if self.pipes_map[x][y][1] != -1 and self.test_tile(tile[0], index_line, index_tile, direction) and self.pipes_map[index_line][index_tile][1] == -1:
                                value = self.pipes_map[x][y][1]
                                self.pipes_map[index_line][index_tile][1] = value + 1
                index_line -= 1
            source_line = self.pipes_map[self.source_position[0]]
            for index_tile, tile in enumerate(source_line, start=0):
                if tile[0] != '.' and tile[0] != 'S':
                    for direction in self.directions:
                        dx, dy = direction
                        x = self.source_position[0] + dx
                        y = index_tile + dy
                        if x < 0:
                            x = 0
                        if x >= len(self.pipes_map):
                            x = len(self.pipes_map) - 1
                        if y < 0:
                            y = 0
                        if y >= len(source_line):
                            y = len(source_line) - 1
                        if self.pipes_map[x][y][1] != -1 and self.test_tile(tile[0], self.source_position[0],
                                                                            index_tile, direction):
                            value = self.pipes_map[x][y][1]
                            self.pipes_map[self.source_position[0]][index_tile][1] = value + 1
            if self.check_map():
                break

        # for line in self.pipes_map:
        #     print(line)

        print(self.max_map())

