class AlmanacData:
    def __init__(self, input_data):
        self.almanac = input_data.splitlines()
        self.almanac_dict = self.parse_data()

    def parse_data(self):
        parsed_data = {}
        current_map = None
        for line in self.almanac:
            if 'seeds' in line:
                seeds_numbers = line.split(":")
                numbers = [int(num) for num in seeds_numbers[1].split()]
                parsed_data['seeds'] = [numbers]
            elif 'map' in line:
                # Remove the colon from the key
                current_map = line.strip().rstrip(':')
                parsed_data[current_map] = []
            elif line.strip() and current_map is not None:
                parsed_data[current_map].append([int(x) for x in line.split()])

        return parsed_data

    def seed_to_soil_map(self, input_seed):
        map_index = 0
        seed_to_soil_map_list = self.almanac_dict['seed-to-soil map']
        seed_to_soil_map_list = sorted(seed_to_soil_map_list, key=lambda x: x[1])
        destination, source, length = seed_to_soil_map_list[map_index]
        match = False

        while not match:
            if input_seed < source:
                match = True
                return input_seed
            elif source <= input_seed < source + length:
                match = True
                return input_seed + (destination - source)
            else:
                map_index += 1
                if map_index == len(seed_to_soil_map_list) and input_seed >= source + length:
                    return input_seed
                destination, source, length = seed_to_soil_map_list[map_index]

    def soil_to_fertilizer_map(self, input_soil):
        map_index = 0
        soil_to_fertilizer_map_list = self.almanac_dict['soil-to-fertilizer map']
        soil_to_fertilizer_map_list = sorted(soil_to_fertilizer_map_list, key=lambda x: x[1])
        destination, source, length = soil_to_fertilizer_map_list[map_index]
        match = False

        while not match:
            if input_soil < source:
                match = True
                return input_soil
            elif source <= input_soil < source + length:
                match = True
                return input_soil + (destination - source)
            else:
                map_index += 1
                if map_index == len(soil_to_fertilizer_map_list) and input_soil >= source + length:
                    return input_soil
                destination, source, length = soil_to_fertilizer_map_list[map_index]

    def fertilizer_to_water_map(self, input_fertilizer):
        map_index = 0
        fertilizer_to_water_map_list = self.almanac_dict['fertilizer-to-water map']
        fertilizer_to_water_map_list = sorted(fertilizer_to_water_map_list, key=lambda x: x[1])
        destination, source, length = fertilizer_to_water_map_list[map_index]

        match = False
        while not match:
            if input_fertilizer < source:
                match = True
                return input_fertilizer
            elif source <= input_fertilizer < source + length:
                match = True
                return input_fertilizer + (destination - source)
            else:
                map_index += 1
                if map_index == len(fertilizer_to_water_map_list) and input_fertilizer >= source + length:
                    return input_fertilizer
                destination, source, length = fertilizer_to_water_map_list[map_index]

    def water_to_light_map(self, input_water):
        map_index = 0
        water_to_light_map_list = self.almanac_dict['water-to-light map']
        water_to_light_map_list = sorted(water_to_light_map_list, key=lambda x: x[1])
        destination, source, length = water_to_light_map_list[map_index]
        match = False

        while not match:
            if input_water < source:
                match = True
                return input_water
            elif source <= input_water < source + length:
                match = True
                return input_water + (destination - source)
            else:
                map_index += 1
                if map_index == len(water_to_light_map_list) and input_water >= source + length:
                    return input_water
                destination, source, length = water_to_light_map_list[map_index]

    def light_to_temperature_map(self, input_light):
        map_index = 0
        light_to_temperature_map_list = self.almanac_dict['light-to-temperature map']
        light_to_temperature_map_list = sorted(light_to_temperature_map_list, key=lambda x: x[1])
        destination, source, length = light_to_temperature_map_list[map_index]
        match = False

        while not match:
            if input_light < source:
                match = True
                return input_light
            elif source <= input_light < source + length:
                match = True
                return input_light + (destination - source)
            else:
                map_index += 1
                if map_index == len(light_to_temperature_map_list) and input_light >= source + length:
                    return input_light
                destination, source, length = light_to_temperature_map_list[map_index]

    def temperature_to_humidity_map(self, input_temperature):
        map_index = 0
        temperature_to_humidity_map_list = self.almanac_dict['temperature-to-humidity map']
        temperature_to_humidity_map_list = sorted(temperature_to_humidity_map_list, key=lambda x: x[1])
        destination, source, length = temperature_to_humidity_map_list[map_index]
        match = False

        while not match:
            if input_temperature < source:
                match = True
                return input_temperature
            elif source <= input_temperature < source + length:
                match = True
                return input_temperature + (destination - source)
            else:
                map_index += 1
                if map_index == len(temperature_to_humidity_map_list) and input_temperature >= source + length:
                    return input_temperature
                destination, source, length = temperature_to_humidity_map_list[map_index]

    def humidity_to_location_map(self, input_humidity):
        map_index = 0
        humidity_to_location_map_list = self.almanac_dict['humidity-to-location map']
        humidity_to_location_map_list = sorted(humidity_to_location_map_list, key=lambda x: x[1])
        destination, source, length = humidity_to_location_map_list[map_index]
        match = False

        while not match:
            if input_humidity < source:
                match = True
                return input_humidity
            elif source <= input_humidity < source + length:
                match = True
                return input_humidity + (destination - source)
            else:
                map_index += 1
                if map_index == len(humidity_to_location_map_list) and input_humidity >= source + length:
                    return input_humidity
                destination, source, length = humidity_to_location_map_list[map_index]

    def transform_seed(self, seed):
        soil = self.seed_to_soil_map(seed)
        fertilizer = self.soil_to_fertilizer_map(soil)
        water = self.fertilizer_to_water_map(fertilizer)
        light = self.water_to_light_map(water)
        temperature = self.light_to_temperature_map(light)
        humidity = self.temperature_to_humidity_map(temperature)
        location = self.humidity_to_location_map(humidity)
        return location

    def find_lowest_location_numbers(self):
        seeds = self.almanac_dict['seeds'][0]
        locations = [self.transform_seed(seed) for seed in seeds]
        return min(locations)

    def find_lowest_location_numbers_range_seeds(self):
        seeds_info = self.almanac_dict['seeds'][0]
        locations = []

        for i in range(0, len(seeds_info), 2):
            start = seeds_info[i]
            range_ = seeds_info[i + 1]
            for seed in range(start, start + range_):
                locations.append(self.transform_seed(seed))

        return min(locations)


