class Card:
    def __init__(self, value, suit):
        card_list = [None, "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.value = card_list[value]
        self.price = self.cal_card_price()
        self.count = self.cal_card_count()
        self.suit = suit

    def cal_card_price(self):
        if self.value == "A":
            return 11
        if self.value in ["J", "Q", "K"]:
            return 10
        if self.value >= 2 and self.value <= 10:
            return self.value

    def cal_card_count(self):
        if self.price < 7:
            return 1
        elif self.price > 9:
            return -1
        else:
            return 0
