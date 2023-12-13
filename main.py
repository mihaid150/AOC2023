from day1.calibration import extract_calibration_sum
from day1.calibration2 import extract_calibration_sum2
from day2.possible_games import get_sum_of_possible_games
from day2.power_set_of_cubes import get_power_set_of_cubes
from day3.sum_adjacent_parts import EngineSchematicData
from day4.scratchcards import ScratchCardsData
from day5.almanac_mapping import AlmanacData
from day6.race import RaceData
from day7.camel_cards import CamelCardsData
from read_input import get_input

# Day1 part 1
# extract_calibration_sum()

# Day1 part 2
# extract_calibration_sum2()

# Day2 part 1
# get_sum_of_possible_games()

# Day 2 part 2
# get_power_set_of_cubes()

# Day 3 part 1
# engine = EngineSchematicData(get_input("day3/input.txt"))
# print(engine.compute_engine_sum())

# Day 3 part 2
# engine = EngineSchematicData(get_input("day3/input.txt"))
# print(engine.compute_sum_of_all_gear_ratios())

# Day 4 part 1
# scratch_card = ScratchCardsData(get_input("day4/input.txt"))
# print(scratch_card.find_scratch_cards_points())

# Day 4 part 2
# scratch_card = ScratchCardsData(get_input("day4/input.txt"))
# scratch_card.process_scratchcards()

# Day 5 part 1
# almanac = AlmanacData(get_input("day5/input.txt"))
# almanac.parse_data()

# Day 5 part 2
# almanac = AlmanacData(get_input("day5/input.txt"))
# almanac.part2_mapping()

# Day 6 part 1
# race = RaceData(get_input("day6/input.txt"))
# race.find_number_of_winning_scenarios()

# Day 7 part 1
camel_cards = CamelCardsData(get_input("day7/input.txt"))
print(camel_cards.get_total_winnings_jokers())

