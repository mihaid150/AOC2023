class AlmanacData:
    def __init__(self, input_data):
        self.almanac = input_data.splitlines()
        self.map_dict = {}
        self.seeds_list = []

    def parse_data(self):
        current_map = None
        for line in self.almanac:
            if 'seeds' in line:
                seeds_numbers = line.split(":")
                numbers = [int(num) for num in seeds_numbers[1].split()]
                numbers_range = []
                i = 0
                while i < len(numbers):
                    start = numbers[i]
                    range_ = numbers[i + 1]
                    end = start + range_ - 1
                    numbers_range.append((start, end))
                    i += 2
                numbers_range = sorted(numbers_range, key=lambda x: x[0])
                self.seeds_list = numbers_range
            elif 'map' in line:
                current_map = line.strip().rstrip(':')
                self.map_dict[current_map] = []
            elif line.strip() and current_map is not None:
                values = [int(x) for x in line.split()]
                start = values[1]
                range_ = values[2]
                end = values[0]
                domain = (start, start + range_ - 1)
                shift = end - start
                codomain = (end, start + range_ - 1 + shift)
                map_list = (domain, codomain)
                self.map_dict[current_map].append(map_list)
                self.map_dict[current_map].sort(key=lambda x: x[0])

    @staticmethod
    def map_interval(interval, map_list):
        # This function maps a given interval through the provided map list
        mapped_intervals = []

        for (source_start, source_end), (dest_start, dest_end) in map_list:
            if interval[0] < source_start and interval[1] < source_start:
                # Interval is entirely before the source interval
                continue
            elif interval[0] > source_end:
                # Interval is entirely after the source interval
                continue
            else:
                # Overlapping cases
                new_start = max(interval[0], source_start)
                new_end = min(interval[1], source_end)
                shift = dest_start - source_start
                mapped_intervals.append((new_start + shift, new_end + shift))

        if not mapped_intervals:
            mapped_intervals.append(interval)

        return mapped_intervals

    def part2_mapping(self):
        seed_to_soil_map = self.map_dict['seed-to-soil map']
        soil_to_fertilizer_map = self.map_dict['soil-to-fertilizer map']
        fertilizer_to_water_map = self.map_dict['fertilizer-to-water map']
        water_to_light_map = self.map_dict['water-to-light map']
        light_to_temperature_map = self.map_dict['light-to-temperature map']
        temperature_to_humidity_map = self.map_dict['temperature-to-humidity map']
        humidity_to_location_map = self.map_dict['humidity-to-location map']
        lowest_location = float('inf')

        for seeds_interval in self.seeds_list:
            mapped_soil = self.map_interval(seeds_interval, seed_to_soil_map)
            mapped_fertilizer = []
            for soil_interval in mapped_soil:
                mapped_fertilizer.extend(self.map_interval(soil_interval, soil_to_fertilizer_map))
            mapped_water = []
            for fertilizer_interval in mapped_fertilizer:
                mapped_water.extend(self.map_interval(fertilizer_interval, fertilizer_to_water_map))
            mapped_light = []
            for water_interval in mapped_water:
                mapped_light.extend(self.map_interval(water_interval, water_to_light_map))
            mapped_temperature = []
            for light_interval in mapped_light:
                mapped_temperature.extend(self.map_interval(light_interval, light_to_temperature_map))
            mapped_humidity = []
            for temperature_interval in mapped_temperature:
                mapped_humidity.extend(self.map_interval(temperature_interval, temperature_to_humidity_map))
            mapped_location = []
            for humidity_interval in mapped_humidity:
                mapped_location.extend(self.map_interval(humidity_interval, humidity_to_location_map))
            for location_interval in mapped_location:
                if location_interval[0] < lowest_location:
                    lowest_location = location_interval[0]

        print("Lowest location: ")
        print(lowest_location)
