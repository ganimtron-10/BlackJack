class BasicStrategy:
	pair_card = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				 [-1, 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
				 [-1, 'N', 'Y/N', 'Y/N', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'N'],
				 [-1, 'N', 'Y/N', 'Y/N', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'N'],
				 [-1, 'N', 'N', 'N', 'N', 'Y/N', 'Y/N', 'N', 'N', 'N', 'N', 'N'],
				 [-1, 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
				 [-1, 'N', 'Y/N', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'N', 'N'],
				 [-1, 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'N'],
				 [-1, 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
				 [-1, 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'N', 'N'],
				 [-1, 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
				 [-1, 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y']]

	soft_card = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				 [-1, 'H', 'H', 'H', 'H', 'DH', 'DH', 'H', 'H', 'H', 'H', 'H'],
				 [-1, 'H', 'H', 'H', 'H', 'DH', 'DH', 'H', 'H', 'H', 'H', 'H'],
				 [-1, 'H', 'H', 'H', 'DH', 'DH', 'DH', 'H', 'H', 'H', 'H', 'H'],
				 [-1, 'H', 'H', 'H', 'DH', 'DH', 'DH', 'H', 'H', 'H', 'H', 'H'],
				 [-1, 'H', 'H', 'DH', 'DH', 'DH', 'DH', 'H', 'H', 'H', 'H', 'H'],
				 [-1, 'S', 'DS', 'DS', 'DS', 'DS', 'DS', 'S', 'S', 'H', 'H', 'H'],
				 [-1, 'S', 'S', 'S', 'S', 'S', 'DS', 'S', 'S', 'S', 'S', 'S'],
				 [-1, 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
				 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

	hard_card = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				 [-1, 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
				 [-1, 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
				 [-1, 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
				 [-1, 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
				 [-1, 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
				 [-1, 'H', 'H', 'DH', 'DH', 'DH', 'DH', 'H', 'H', 'H', 'H', 'H'],
				 [-1, 'H', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'H', 'H'],
				 [-1, 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH', 'DH'],
				 [-1, 'H', 'H', 'H', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],
				 [-1, 'H', 'S', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],
				 [-1, 'H', 'S', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],
				 [-1, 'H', 'S', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],
				 [-1, 'H', 'S', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H'],
				 [-1, 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
				 [-1, 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
				 [-1, 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
				 [-1, 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
				 [-1, 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']]

	def choose_move(self,player_card,dealer_card,is_pair,is_soft,player_pair_value,num_of_p_cards):
		# print(player_card,dealer_card,is_pair,is_soft)
		if is_pair:
			return self.choose_from_pair_cards(player_pair_value,dealer_card,player_card,num_of_p_cards)
		elif is_soft:
			return self.choose_from_soft_cards(player_card, dealer_card,num_of_p_cards)
		else:
			return self.choose_from_hard_cards(player_card, dealer_card,num_of_p_cards)

	def choose_from_pair_cards(self,p_c,d_c,player_total_score,num_of_p_cards):
		choice = self.pair_card[p_c][d_c]
		if choice == 'Y/N' or choice == 'Y':
			return 'SP'
		elif choice == 'N':
			return self.choose_from_hard_cards(player_total_score,d_c,num_of_p_cards)

	def choose_from_soft_cards(self,p_c,d_c,num_of_p_cards):
		choice = self.soft_card[p_c][d_c]
		if choice == 'DH' or choice == 'DS':
			if num_of_p_cards == 2:
				return 'D'
			else:
				return choice[1]
		else:
			return choice

	def choose_from_hard_cards(self,p_c,d_c,num_of_p_cards):
		choice = self.hard_card[p_c][d_c]

		if choice == 'DH':
			if num_of_p_cards == 2:
				return 'D'
			else:
				return choice[1]
		else:
			return choice
		



class BasicStrategy_with_PlayerDeviation(BasicStrategy):
	pd_cards = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				[-1, -1, 'D 1', -1, -1, -1, -1, 'D 3', -1, -1, -1, -1],
				[-1, -1, -1, -1, -1, 'SP 5', 'SP 4', -1, -1, -1, 'D 4', 'D 4'],
				[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 'D 1'],
				[-1, -1, 'S 3', 'S 2', 'SH 0', 'SH -2', 'SH -1', -1, -1, -1, -1, -1],
				[-1, -1, 'SH -1', 'SH -2', -1, -1, -1, -1, -1, -1, -1, -1],
				[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 'S 4', -1],
				[-1, -1, -1, -1, -1, -1, -1, -1, -1, 'S 5', 'S 0', -1],
				[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
				[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

	def choose_move_with_player_deviation(self,player_card,dealer_card,is_pair,is_soft,player_pair_value,num_of_p_cards,true_count):


		if is_pair and (2*player_pair_value == player_card):
			choice_pair = self.pd_cards[player_pair_value][dealer_card]
			if choice_pair != -1:
				choice_pair = choice_pair.split(" ")
				if int(choice_pair[1]) <= true_count:
					return choice_pair[0]

		elif not is_soft:
			choice = self.pd_cards[player_card][dealer_card]

			if choice != -1:
				choice = choice.split(' ')
				if choice[0] == 'SH':
					if true_count >= int(choice[1]):
						return 'S'
					else:
						return 'H'
				elif choice == 'D' and num_of_p_cards == 2:
					return 'D'
				else:
					if true_count >= int(choice[1]):
						return choice[0]



		return self.choose_move(player_card,dealer_card,is_pair,is_soft,player_pair_value,num_of_p_cards)

	def take_insurance(self,true_count):
		if true_count >= 3:
			return 'I'
		else:
			return 'NI'




if __name__ == '__main__':
	bs_pd = BasicStrategy_with_PlayerDeviation()
	choice = bs_pd.choose_move_with_player_deviation(10,11,False,False,10,3,3.0)
	print(choice)

	print(bs_pd.take_insurance(-2.0))

	

	# pd = bs_pd.pd_cards

	# for i in range(len(pd)):
	# 	for j in range(len(pd[0])):
	# 		pd[i][j] = -1


	# pd[9][2] = 'D 1'
	# pd[9][7] = 'D 3'
	# pd[10][11] = 'D 4'
	# pd[10][5] = 'SP 5'
	# pd[10][6] = 'SP 4'
	# pd[10][10] = 'D 4'
	# pd[11][11] = 'D 1'
	# pd[12][2] = 'S 3'
	# pd[12][3] = 'S 2'
	# pd[12][4] = 'SH 0'
	# pd[12][5] = 'SH -2'
	# pd[12][6] = 'SH -1'
	# pd[13][2] = 'SH -1'
	# pd[13][3] = 'SH -2'
	# pd[15][10] = 'S 4'
	# pd[16][9] = 'S 5'
	# pd[16][10] = 'S 0'

	# print(pd)
