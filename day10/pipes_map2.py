from collections import deque

import numpy as np


class Pipes:
    def __init__(self, input_data):
        self.input_data = input_data.splitlines()
        self.data = np.pad(np.array([[char for char in line.strip()] for line in self.input_data]),
                           1, constant_values='.',)
        self.connections = {
            '-': [(0, -1), (0, 1)],
            '|': [(-1, 0), (1, 0)],
            'L': [(-1, 0), (0, 1)],
            'J': [(-1, 0), (0, -1)],
            '7': [(1, 0), (0, -1)],
            'F': [(1, 0), (0, 1)],
            '.': [],
        }
        self.directions = np.array([[1, 0], [0, 1], [-1, 0], [0, -1]])
        self.starting_point = np.array(next(zip(*np.where(self.data == 'S'))))
        self.starting_directions = self.find_starting_directions()

    def find_starting_directions(self):
        # a coordinate is formed from row and column index
        # these 2 tuples represents the possible next points for the two directions from the starting point
        (left_coordinates, left_vector), (right_coordinates, right_vector) = [
            (self.starting_point + delta, delta) for delta in self.directions if tuple(-delta) in self.connections[self.data[tuple(self.starting_point + delta)]]
        ]
        return (left_coordinates, left_vector), (right_coordinates, right_vector)

    def update(self, point, direction):
        # determines the next point based on the current point and current position
        # tuple(-directions) == options[0] checks whether it is a valid connection between next point and current point
        options = self.connections[self.data[tuple(point)]]
        new_direction = np.array(
            options[1] if tuple(-direction) == options[0] else options[0]
        )
        return point + new_direction, new_direction

    def traverse_pipe_map(self):
        distance = 1
        left_path = [self.starting_point, self.starting_directions[0][0]]
        right_path = [self.starting_directions[1][0]]
        (left_coordinates, left_vector), (right_coordinates, right_vector) = self.starting_directions

        while not np.allclose(left_coordinates, right_coordinates):
            (left_coordinates, left_vector) = self.update(left_coordinates, left_vector)
            left_path.append(left_coordinates)
            (right_coordinates, right_vector) = self.update(right_coordinates, right_vector)
            right_path.append(right_coordinates)
            distance += 1

        ys, xs = zip(*(left_path + right_path[:-1][::-1]))
        dy, dx = np.diff([ys + (ys[0],), xs + (xs[0],)], axis=1)
        board = np.ones((self.data.shape[0] * 2, self.data.shape[1] * 2))
        ys, xs = map(np.array, [ys, xs])
        board[2 * ys, 2 * xs] = 0
        board[2 * ys + dy, 2 * xs + dx] = 0
        board = np.pad(board[1:-1, 1:-1], 1, constant_values=0)
        points = deque([(1, 1)])
        while points:
            point = points.popleft()
            if board[point] == 0:
                continue
            board[point] = 0
            for delta in self.directions:
                nb = tuple(delta + point)
                if board[nb]:
                    points.append(nb)
        print(int(board[::2, ::2].sum()))
