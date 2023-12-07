CARD_VALUES = {"2": "0", "3": "1", "4": "2", "5": "3", "6": "4", "7": "5", "8": "6", "9": "7", "T": "8", "J": "9", "Q": "a", "K": "b", "A": "c"}

class Hand:
    def __init__(self, hand):
        self.cards = hand[0]
        self.bid = int(hand[1])
        self.strength = int(self.get_strength(), 13)

    def get_strength(self):
        return self.get_shape() + "".join([CARD_VALUES[card] for card in self.cards])

    def get_shape(self):
        cards = {card: self.cards.count(card) for card in CARD_VALUES.keys()}
        if 5 in cards.values():
            return "6"
        if 4 in cards.values():
            return "5"
        if 3 in cards.values():
            if 2 in cards.values():
                return "4"
            return "3"
        pairs = list(cards.values()).count(2)
        if pairs == 2:
            return "2"
        if pairs == 1:
            return "1"
        return "0"



with open("puzzle_inputs/day_7_input.txt", "r") as file:
    hands = [Hand(line.split()) for line in file.readlines()]



def part_1():
    sorted_hands = sorted(hands, key=lambda x: x.strength)
    total_winnings = 0
    rank = 1
    for hand in sorted_hands:
        total_winnings += rank * hand.bid
        rank += 1
    print(total_winnings)


part_1()
