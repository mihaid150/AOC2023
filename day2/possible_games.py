from read_input import get_input


class GameData:
    def __init__(self, games_info):
        self.games = self.parse_games_info(games_info)
        self.max_red_cubes = 12
        self.max_green_cubes = 13
        self.max_blue_cubes = 14

    @staticmethod
    def parse_games_info(games_info):
        games = []
        games_info = games_info.split("\n")
        for i, game in enumerate(games_info, start=1):
            _, game_data = game.split(": ", 1)
            game_sets = [GameData.parse_set(set_info) for set_info in game_data.split("; ")]
            games.append((i, game_sets))
        return games

    @staticmethod
    def parse_set(set_info):
        items = set_info.split(", ")
        return {color: int(count) for count, color in (item.split(" ") for item in items)}

    def ids_sum_of_possible_games(self):
        result = [game for game in self.games if not self.should_remove_game(game)]
        return sum(game[0] for game in result)

    def should_remove_game(self, game):
        for cubes_set in game[1]:
            if any(self.should_remove_set(color, value) for color, value in cubes_set.items()):
                return True
        return False

    def should_remove_set(self, color, value):
        return (color == 'blue' and value > self.max_blue_cubes) or \
               (color == 'red' and value > self.max_red_cubes) or \
               (color == 'green' and value > self.max_green_cubes)

    def display_games(self):
        for i, game in enumerate(self.games):
            print(f"Game {i + 1}: {game}")


def get_sum_of_possible_games():
    file_path = "day2/input.txt"
    input_data = get_input(file_path)

    games_data = GameData(input_data)
    print(games_data.ids_sum_of_possible_games())




