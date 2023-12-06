class Player:

    def __init__(self, name, chips, hand):
        self.chips = chips
        self._hand = hand
        self.name = name
        self.bet_amount = 0

    def get_hand(self):
        return self._hand

    def set_bet_amount(self, bet_amount):
        self.bet_amount = bet_amount

    def get_bet_amount(self):
        return self.bet_amount

    def add_card_to_hand(self, card_to_be_added):
        self._hand.append(card_to_be_added)

    def set_chips(self, new_chip_value):
        self.chips = new_chip_value

    def add_chips(self, chips_to_be_added):
        self.chips += chips_to_be_added

    def remove_chips(self, amount):
        if amount < self.chips:
            self.chips -= amount
        else:
            print("not enough money ")

    def __str__(self):
        hand_str = ""
        for card in self._hand:

            hand_str += card.__str__() + "|"

        return "name:{name}, hole cards:{hand}, chips left:{chips}".format(name=self.name, hand=hand_str, chips=self.chips)





