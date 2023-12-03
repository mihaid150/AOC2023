from read_input import get_input
from day2.possible_games import GameData


def power_set(game_sets):
    max_red_cube = 1
    max_green_cube = 1
    max_blue_cube = 1

    # for each dictionary the maximum values are computed
    for cubes_set in game_sets:
        for color, value in cubes_set.items():
            if color == 'red' and value > max_red_cube:
                max_red_cube = value
            if color == 'green' and value > max_green_cube:
                max_green_cube = value
            if color == 'blue' and value > max_blue_cube:
                max_blue_cube = value
    return max_red_cube * max_green_cube * max_blue_cube


def get_power_set_of_cubes():
    file_path = "day2/input.txt"
    input_data = get_input(file_path)

    games_data = GameData(input_data).games
    games_sum = 0
    for game in games_data:
        games_sum += power_set(game[1])
    print(games_sum)
