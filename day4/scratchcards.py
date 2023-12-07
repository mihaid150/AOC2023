class ScratchCardsData:
    def __init__(self, input_data):
        self.scratch_cards = input_data.splitlines()
        self.winning_numbers = []
        self.numbers = []
        self.total_points = 0
        self.card_matches = {}
        self.total_processed_cards = 0

    def find_scratch_cards_points(self):
        for card in self.scratch_cards:
            winning_numbers_count = 0

            # parse the sets
            _, card_numbers = card.split(":")
            set1, set2 = [num_set.strip() for num_set in card_numbers.split("|")]
            self.winning_numbers = list(map(int, set1.split()))
            self.numbers = list(map(int, set2.split()))

            # count matches between the two sets
            for winning_number in self.winning_numbers:
                if winning_number in self.numbers:
                    winning_numbers_count += 1

            # compute the total points based on card matches
            if winning_numbers_count >= 1:
                self.total_points += pow(2, winning_numbers_count - 1)

        return self.total_points

    def find_card_matches(self):
        for card_index, card in enumerate(self.scratch_cards, start=1):
            card_matches_count = 0
            card_number, card_numbers = card.split(":")
            set1, set2 = [num_set.strip() for num_set in card_numbers.split("|")]
            self.winning_numbers = list(map(int, set1.split()))
            self.numbers = list(map(int, set2.split()))

            for winning_number in self.winning_numbers:
                if winning_number in self.numbers:
                    card_matches_count += 1
            self.card_matches[card_index] = card_matches_count

    def process_scratchcards(self):
        self.find_card_matches()
        original_cards = list(self.card_matches.keys())
        cards = original_cards.copy()
        index = 0

        while index < len(cards):
            card = cards[index]
            self.total_processed_cards += 1
            original_index = original_cards.index(card)
            cars_copies = original_cards[original_index + 1: original_index + 1 + self.card_matches[card]]
            if cars_copies:
                for card_copy in cars_copies:
                    cards.append(card_copy)
            index += 1

        print(self.total_processed_cards)
