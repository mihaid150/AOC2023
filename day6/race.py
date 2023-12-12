class RaceData:
    def __init__(self, input_data):
        self.race_data = input_data.splitlines()
        self.races = {}

    def process_input(self):
        line = self.race_data[0]
        _, numbers = line.split(":")
        time_numbers = [int(num) for num in numbers.split()]
        line = self.race_data[1]
        _, numbers = line.split(":")
        distance_numbers = [int(num) for num in numbers.split()]
        for i, time_number in enumerate(time_numbers, start=0):
            self.races[time_number] = distance_numbers[i]

    def find_number_of_winning_scenarios(self):
        # self.process_input()
        self.process_input2()
        product = 1
        for total_time, max_distance in self.races.items():
            winning_scenario_count = 0
            for charging_time in range(0, total_time + 1):
                remaining_time = total_time - charging_time
                traveled_distance = remaining_time * charging_time
                if traveled_distance > max_distance:
                    winning_scenario_count += 1
            product *= winning_scenario_count
        print(product)

    def process_input2(self):
        line = self.race_data[0]
        _, numbers = line.split(":")
        time_numbers = [int(num) for num in numbers.split()]
        line = self.race_data[1]
        _, numbers = line.split(":")
        distance_numbers = [int(num) for num in numbers.split()]
        time = 0
        for time_number in reversed(time_numbers):
            if time == 0:
                time = time_number
            else:
                time = time + time_number * pow(10, len(str(time)))
        distance = 0
        for distance_number in reversed(distance_numbers):
            if distance == 0:
                distance = distance_number
            else:
                distance = distance + distance_number * pow(10, len(str(distance)))
        self.races[time] = distance




