from Deck import Deck

import copy

class Player:
	def __init__(self,is_dealer,deck,player_index=-1,current_game=None,bankroll_value=None,min_bet=None):
		self.game = current_game
		self.bankroll = bankroll_value
		self.min_bet = min_bet
		self.current_bet = min_bet
		self.cards = []
		self.is_dealer = is_dealer
		self.deck = deck
		self.score = 0
		self.reveal_cards = False
		self.can_hit = True
		self.can_dd = True
		self.player_index = str(player_index)

		self.parent = None
		self.is_derivate = False

		self.is_pair = False
		self.is_soft = False

		self.has_insurance = False

		self.bankroll_value_list = [bankroll_value]

		# self.split_value = str(player_index)

	def update_bet(self):
		true_count = self.deck.count_card.true_count
		if(true_count <= 1.5):
			self.current_bet = self.min_bet
		elif(1.5 < true_count <= 2.5):
			self.current_bet = 2*self.min_bet
		elif(2.5 < true_count <= 3.5):
			self.current_bet = 4*self.min_bet
		elif(true_count > 3.5):
			self.current_bet = 8*self.min_bet

	def deal(self):
		self.cards.extend(self.deck.draw_card(2))
		self.cal_score()
		if self.score == 21:
			#Player Has A BlackJack
			return 1
		return 0

	def hit(self):
		if self.can_hit:
			can_dd = False
			self.cards.extend(self.deck.draw_card(1))
			self.cal_score()
			if self.score > 21:
				#Player Busted
				return 0
			return 1
		else:
			print("You can't Hit anymore!!")
			return -1

	def double_down(self):
		if self.can_dd:
			self.current_bet = 2*self.current_bet
			print(f"Bet After Doubling Down is {self.current_bet}")
			bust_value = self.hit()
			self.can_hit = False
			self.can_dd = False
			return bust_value
		else:
			print("Can't Double Down!!")

	def split(self):
		self.can_hit = True
		self.can_dd = True
		player_copy = copy.deepcopy(self)

		player_copy.cards = [self.cards.pop()]
		player_copy.parent = self
		player_copy.is_derivate = True

		player_copy.player_index += '.1'
		self.player_index += '.2'

		parent_bust = self.hit()
		player_copy.hit()

		if player_copy.cards[0].value == 'A':
			self.can_hit = False
			player_copy.can_hit = False
		
		player_copy.show_cards()
		self.show_cards()


		return player_copy


	def check_cards(self):
		# print("Checking for Pair")
		if (self.cards[0].value == self.cards[1].value) and (len(self.cards) == 2):
			self.is_pair = True
		else:
			self.is_pair = False



	def show_cards(self):
		if self.is_dealer:
			print("\nDealer's Card:")
			if self.reveal_cards == True:
				for card in self.cards:
					print(card.value)
				print("Score: ",self.score)
				return

			print(self.cards[0].value)
			print("XX")
			print("Score: ",self.cards[0].price)
			

		else:
			print(f"\nPlayer {self.player_index} Cards: ")
			for card in self.cards:
				print(card.value)
			print("Score: ",self.score)

	def cal_score(self):
		self.check_cards()
		self.is_soft = False

		ace_counter = 0
		score = 0
		for card in self.cards:
			if card.value == 'A':
				ace_counter = ace_counter + 1 # ace_counter += 1
			score += card.price

		while ace_counter > 0 and score > 21:
			is_soft = True
			score -= 10
			ace_counter -= 1

		self.score = score

	def update_bankroll_value(self, factor):
		p = self
		if self.is_derivate:
			p = self.parent

		p.bankroll += (factor * self.current_bet)
		print("Bankroll_value",self.player_index,p.bankroll)


if __name__ == "__main__":
	d = Player(is_dealer=False, deck=Deck(),player_index = 1 ,current_game=None)
	d.deal()
	d.show_cards()
	print()
	# print("score: ",d.score)
	d.reveal_cards = True
	d.show_cards()

	print()
	d.hit()
	d.show_cards()
	# print("Score: ",d.score)
	print()

