from BlackJack import BlackJack

# import matplotlib.pyplot as plt

num_of_player = int(input("Enter Num of Player: "))

while num_of_player > 7 or num_of_player < 1:
    print("Invalid Num of Player! Enter value between 1 to 7!")
    num_of_player = int(input("Enter Num of Player: "))

min_bet_for_game = int(input("Enter Minimum Bet for the Game: "))
num_of_deck = int(input("Enter Number of decks: "))
num_of_deck_before_s = float(input("Enter Number of deck to remain before shuffling: "))
num_of_rounds = int(input("Enter Number of Rounds: "))

game_type = input("Whether Playing Deviation required(y/n): ")

if game_type == "y" or game_type == "Y":
    game_type = False
else:
    game_type = True

can_dealer_hit_on_soft = input("Can Dealer hit on soft 17(y/n): ")

if can_dealer_hit_on_soft == "n" or can_dealer_hit_on_soft == "N":
    can_dealer_hit_on_soft = False
else:
    can_dealer_hit_on_soft = True

bankroll_value_list = []

for player in range(num_of_player):
    print("#############Enter Values for Player", player + 1, "################")
    bankroll_value = int(input("Enter Initial Bankroll Value: "))
    bankroll_value_list.append(bankroll_value)


num_of_streak = int(input("Enter number of streak: "))

b = BlackJack(
    min_bet_for_game,
    num_of_deck,
    num_of_deck_before_s,
    can_dealer_hit_on_soft,
    bankroll_value_list,
    num_of_player,
    game_type,
)

for i in range(num_of_streak):
    print(f"################## Streak {i} ######################")

    max_tc, max_tc_round = b.play_n_rounds(num_of_rounds)

    print(f"Maximum True Count is {max_tc} for round {max_tc_round}")

#     for player in b.player_list:
#       plt.plot(player.bankroll_value_list)


# plt.xlabel("Number of Rounds")
# plt.ylabel("Bankroll Value")

# plt.show()
