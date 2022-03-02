class Card:
    def __init__(self, value, suit):
        card_list = [None, "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.value = card_list[value]
        self.price = self.cal_card_price(self.value)
        self.count = self.cal_card_count(self.price)
        self.suit = suit

    def cal_card_price(self, card_value):
        if card_value == "A":
            return 11
        if card_value in ["J", "Q", "K"]:
            return 10
        if card_value >= 2 and card_value <= 10:
            return card_value

    def cal_card_count(self, card_price):
        if card_price < 7:
            return 1
        elif card_price > 9:
            return -1
        else:
            return 0
