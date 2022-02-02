from Cards import Card
from CountingCards import CountCards

import random

class Deck:
	def __init__(self,num_of_deck=4):
		self.num_of_deck = num_of_deck
		self.cards = []
		self.count_card = CountCards()
		self.generate_cards()

	def generate_cards(self):
		print("######################## Shuffling Cards!! #########################")
		self.count_card.reset()
		for nod in range(self.num_of_deck):
			for i in range(1,14): # 1 2 3 45 6 7 8 9 10 11 12 13
				for j in range(4):
					self.cards.append(Card(i,j))

	def draw_card(self, num_of_cards):
		card = []
		for i in range(num_of_cards):
			c = random.choice(self.cards)
			self.count_card.running_count += c.count
			card.append(c)
			self.cards.remove(c)

		return card

	def num_of_deck_remaining(self):
		return len(self.cards)/52
					

if __name__ == "__main__":
	d1 = Deck()
	print(d1.draw_card(2))