from collections import Counter
class CamelCardsData:
    def __init__(self, input_data):
        self.given_input = input_data.splitlines()
        self.camel_cards_strength = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3,
                                     '4': 2, '3': 1, '2': 0}
        self.camel_cards_strength_joker = {'A': 12, 'K': 11, 'Q': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, 'J': 0}
        self.types_order = {'Five of a kind': 6, 'Four of a kind': 5, 'Full house': 4, 'Three of a kind': 3,
                            'Two pair': 2, 'One pair': 1, 'High card': 0}
        self.cards_bids = {}

    def process_input(self):
        for line in self.given_input:
            card, bid = line.split()
            self.cards_bids[card] = int(bid)

    @staticmethod
    def process_card(card):
        camel_cards = {'A': 0, 'K': 0, 'Q': 0, 'J': 0, 'T': 0, '9': 0, '8': 0, '7': 0, '6': 0, '5': 0, '4': 0, '3': 0,
                       '2': 0}
        for symbol in card:
            camel_cards[symbol] += 1

        count_five = list(camel_cards.values()).count(5)
        count_four = list(camel_cards.values()).count(4)
        count_three = list(camel_cards.values()).count(3)
        count_two = list(camel_cards.values()).count(2)
        count_one = list(camel_cards.values()).count(1)

        if count_five == 1:
            return 'Five of a kind'
        elif count_four == 1 and count_one == 1:
            return 'Four of a kind'
        elif count_three == 1 and count_two == 1:
            return 'Full house'
        elif count_three == 1 and count_one == 2:
            return 'Three of a kind'
        elif count_two == 2 and count_one == 1:
            return 'Two pair'
        elif count_two == 1 and count_one == 3:
            return 'One pair'
        else:
            return 'High card'

    def compare_cards(self, card1, card2):
        type1 = self.process_card(card1)
        type2 = self.process_card(card2)

        if self.types_order[type1] > self.types_order[type2]:
            return card1, card2
        elif self.types_order[type1] < self.types_order[type2]:
            return card2, card1
        else:
            for i in range(0, 5):
                if self.camel_cards_strength[card1[i]] > self.camel_cards_strength[card2[i]]:
                    return card1, card2
                elif self.camel_cards_strength[card1[i]] < self.camel_cards_strength[card2[i]]:
                    return card2, card1
                else:
                    continue
        return card1, card2

    def get_total_winnings(self):
        self.process_input()
        cards = list(self.cards_bids.keys())
        ordered_cards = []
        winning = 0

        while len(cards) != 0:
            current_maximum = cards[0]
            for card in cards:
                if card == current_maximum:
                    continue
                elif self.compare_cards(card, current_maximum) == (card, current_maximum):
                    current_maximum = card
                elif self.compare_cards(card, current_maximum) == (current_maximum, card):
                    continue

            ordered_cards.append(current_maximum)
            cards.remove(current_maximum)

        for i, card in enumerate(reversed(ordered_cards), start=1):
            winning += i * self.cards_bids[card]

        return winning

    @staticmethod
    def process_card_joker_scenarios(card):
        jokers = card.count('J')
        free_jokers_card = [char for char in card if char != 'J']
        counts = sorted(Counter(free_jokers_card).values(), reverse=True)

        if not counts:
            counts = [0]
        if counts[0] + jokers == 5:
            return 'Five of a kind'
        elif counts[0] + jokers == 4:
            return 'Four of a kind'
        elif counts[0] + jokers == 3 and counts[1] == 2:
            return 'Full house'
        elif counts[0] + jokers == 3:
            return 'Three of a kind'
        elif counts[0] == 2 and (jokers or counts[1] == 2):
            return 'Two pair'
        elif counts[0] == 2 or jokers:
            return 'One pair'
        else:
            return 'High card'

    def compare_cards_jokers(self, card1, card2):
        type1 = self.process_card_joker_scenarios(card1)
        type2 = self.process_card_joker_scenarios(card2)

        if self.types_order[type1] > self.types_order[type2]:
            return card1, card2
        elif self.types_order[type1] < self.types_order[type2]:
            return card2, card1
        else:
            for i in range(0, 5):
                if self.camel_cards_strength_joker[card1[i]] > self.camel_cards_strength_joker[card2[i]]:
                    return card1, card2
                elif self.camel_cards_strength_joker[card1[i]] < self.camel_cards_strength_joker[card2[i]]:
                    return card2, card1
                else:
                    continue

    def get_total_winnings_jokers(self):
        self.process_input()
        cards = list(self.cards_bids.keys())
        ordered_cards = []
        winning = 0

        while len(cards) != 0:
            current_maximum = cards[0]
            for card in cards:
                if card == current_maximum:
                    continue
                elif self.compare_cards_jokers(card, current_maximum) == (card, current_maximum):
                    current_maximum = card
                elif self.compare_cards_jokers(card, current_maximum) == (current_maximum, card):
                    continue

            ordered_cards.append(current_maximum)
            cards.remove(current_maximum)

        for i, card in enumerate(reversed(ordered_cards), start=1):
            winning += i * self.cards_bids[card]

        return winning


