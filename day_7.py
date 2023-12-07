CARD_VALUES = {"2": "0", "3": "1", "4": "2", "5": "3", "6": "4", "7": "5", "8": "6", "9": "7", "T": "8", "J": "9", "Q": "a", "K": "b", "A": "c"}
CARD_VALUES = {"J": "0","2": "1", "3": "2", "4": "3", "5": "4", "6": "5", "7": "6", "8": "7", "9": "8", "T": "9",  "Q": "a", "K": "b", "A": "c"}  # uncomment for part 2

class Hand:
    def __init__(self, hand):
        self.cards = hand[0]
        self.bid = int(hand[1])
        self.strength = int(self.get_strength(), 13)

    def get_strength(self):
        return self.get_shape() + "".join([CARD_VALUES[card] for card in self.cards])

    def get_shape(self):
        cards = {card: self.cards.count(card) for card in CARD_VALUES.keys()}

        # comment this section for part 2
        jokers = cards["J"]
        cards["J"] = 0
        max_card = max(cards, key=cards.get)
        cards[max_card] += jokers
        ##################################

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



def main():
    sorted_hands = sorted(hands, key=lambda x: x.strength)
    total_winnings = 0
    rank = 1
    for hand in sorted_hands:
        total_winnings += rank * hand.bid
        rank += 1
    print(total_winnings)


main()
