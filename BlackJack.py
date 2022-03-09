from Card import Card
from Deck import Deck
from Player import Player
from BasicStrategy import BasicStrategy, BasicStrategy_with_PlayerDeviation


class BlackJack:
    def __init__(
        self,
        g_min_bet,
        num_of_deck,
        num_of_deck_before_s,
        can_dealer_hit_on_soft,
        bankroll_value_list,
        num_of_players=1,
        basic_strategy=True,
    ):
        self.deck = Deck(num_of_deck)
        self.dealer = Player(True, self.deck, self)
        self.player_list = []
        self.g_min_bet = g_min_bet
        self.num_of_deck_before_s = num_of_deck_before_s
        self.create_players(num_of_players, bankroll_value_list)
        self.current_player_list = []
        self.basic_strategy = basic_strategy
        self.can_dealer_hit_on_soft = can_dealer_hit_on_soft

    def create_players(self, num_of_players, bankroll_value_list):
        for i in range(num_of_players):
            player = Player(
                False, self.deck, i + 1, self, bankroll_value_list[i], self.g_min_bet
            )

            self.player_list.append(player)

    def play_n_rounds(self, num_of_rounds):
        max_true_count = -10000000
        max_tc_round = 0
        for i in range(num_of_rounds):
            print(f"#################### Round {i+1} ####################")
            current_tc = self.play_round()

            if current_tc > max_true_count:
                max_true_count = current_tc
                max_tc_round = i + 1

            self.clear_round()

        return max_true_count, max_tc_round

    def clear_round(self):

        # print(f"Current running count: {self.deck.count_card.running_count}")
        # print(f"Current true count: {self.deck.count_card.true_count}")

        self.deck.count_card.update_true_count(self.deck.num_of_deck_remaining())

        print(f"Current running count: {self.deck.count_card.running_count}")
        print(f"Current true count: {self.deck.count_card.true_count}")

        self.dealer.cards = []
        for player in self.player_list:
            player.cards = []
            player.has_insurance = False
            player.can_hit = True
            player.can_dd = True
            player.bankroll_value_list.append(player.bankroll)

        self.dealer.reveal_cards = False
        self.current_player_list = []

        for i in range(len(self.player_list)):
            self.player_list[i].player_index = str(i + 1)

    def ask_player_choice(self, current_player, dealer_status):
        choice = ""
        while choice != "S":

            player_card_score = current_player.score
            if current_player.is_pair:
                player_card_score = current_player.cards[-1].price

            # print("\nStrategy: ",BasicStrategy().choose_move(current_player.score, self.dealer.cards[0].price, current_player.is_pair, current_player.is_soft,player_card_score))

            # print("\nStrategy: ",
            # BasicStrategy_with_PlayerDeviation().choose_move_with_player_deviation(current_player.score,
            # self.dealer.cards[0].price,
            # current_player.is_pair,
            # current_player.is_soft,
            # player_card_score,
            # self.deck.count_card.true_count))
            print(
                f"""Enter for Player {current_player.player_index} \nS for Stand\nH for Hit\nD for Double Dowm\nSP for Split\n----> :"""
            )

            if self.basic_strategy:
                print(
                    "\nStrategy: ",
                    BasicStrategy().choose_move(
                        current_player.score,
                        self.dealer.cards[0].price,
                        current_player.is_pair,
                        current_player.is_soft,
                        player_card_score,
                        len(current_player.cards),
                    ),
                )
                print(
                    (
                        current_player.score,
                        self.dealer.cards[0].price,
                        current_player.is_pair,
                        current_player.is_soft,
                        player_card_score,
                        len(current_player.cards),
                    )
                )
                choice = BasicStrategy().choose_move(
                    current_player.score,
                    self.dealer.cards[0].price,
                    current_player.is_pair,
                    current_player.is_soft,
                    player_card_score,
                    len(current_player.cards),
                )
            else:
                print(
                    "\nStrategy: ",
                    BasicStrategy_with_PlayerDeviation().choose_move_with_player_deviation(
                        current_player.score,
                        self.dealer.cards[0].price,
                        current_player.is_pair,
                        current_player.is_soft,
                        player_card_score,
                        len(current_player.cards),
                        self.deck.count_card.true_count,
                    ),
                )
                print(
                    (
                        current_player.score,
                        self.dealer.cards[0].price,
                        current_player.is_pair,
                        current_player.is_soft,
                        player_card_score,
                        len(current_player.cards),
                        self.deck.count_card.true_count,
                    )
                )
                choice = BasicStrategy_with_PlayerDeviation().choose_move_with_player_deviation(
                    current_player.score,
                    self.dealer.cards[0].price,
                    current_player.is_pair,
                    current_player.is_soft,
                    player_card_score,
                    len(current_player.cards),
                    self.deck.count_card.true_count,
                )

            # choice = input()

            # choice = BasicStrategy_with_PlayerDeviation().choose_move(current_player.score,
            # self.dealer.cards[0].price, current_player.is_pair, current_player.is_soft, player_card_score)

            if choice == "H":
                p_bust = current_player.hit()
                current_player.show_cards()

                if p_bust == -1:
                    break

                if p_bust == 0:
                    print(f"Player {current_player.player_index} has Busted!!")
                    current_player.update_bankroll_value(-1)
                    return None

            if choice == "D":
                p_bust = current_player.double_down()
                current_player.show_cards()
                if p_bust == -1:
                    break
                if p_bust == 0:
                    print(f"Player {current_player.player_index} has Busted!!")
                    current_player.update_bankroll_value(-1)
                    return None
                choice = "S"

            if choice == "SP":
                split_player = current_player.split()
                # self.current_player_list.insert(i+1, split_player)
                does_split_player_exits = self.ask_player_choice(
                    split_player, dealer_status
                )
                if does_split_player_exits != None:
                    self.current_player_list.append(does_split_player_exits)

            if choice == -1:
                print("Some thing error caused!")
                break
        return current_player

    def play_round(self):

        if self.deck.num_of_deck_remaining() <= self.num_of_deck_before_s:
            self.deck.generate_cards()

        for player in self.player_list:
            player.update_bet()
            print(f"Player {player.player_index} is betting {player.current_bet}")

        self.current_player_list = self.player_list.copy()

        dealer_status = self.dealer.deal()
        self.dealer.show_cards()

        player_bj = []

        for i in range(len(self.player_list)):
            current_player = self.player_list[i]
            player_bj.append(current_player.deal())
            current_player.show_cards()

        if self.dealer.cards[0].value == "A":
            self.ask_for_insurance()

        if dealer_status:
            print("Dealer Has A BlackJack!!")
            for i in range(len(self.player_list)):
                current_player = self.player_list[i]

                if current_player.has_insurance:
                    print("Insurance Money Won!!")
                    current_player.update_bankroll_value(1)
                elif player_bj[i]:
                    print("Player Also Has A BlackJack!! PUSH!!")
                else:
                    self.player_list[i].update_bankroll_value(-1)
            return self.deck.count_card.true_count
        else:
            for i in range(len(self.player_list)):
                current_player = self.player_list[i]

                if player_bj[i] == 1:
                    print(f"Player {current_player.player_index} has a Blackjack!!")
                    current_player.update_bankroll_value(1.5)
                    self.current_player_list[i] = None

                if current_player.has_insurance:
                    print("Insurance Money Lost!")
                    current_player.update_bankroll_value(-0.5)

        for i in range(len(self.current_player_list)):

            if self.current_player_list[i] == None:
                continue

            self.current_player_list[i] = self.ask_player_choice(
                self.current_player_list[i], dealer_status
            )

        self.dealer.reveal_cards = True
        self.dealer.show_cards()

        player_exits = False
        for player in self.current_player_list:
            if player != None:
                player_exits = True

        if not player_exits:
            return self.deck.count_card.true_count

        while self.dealer.score < 17:
            if self.dealer.is_soft and not self.can_dealer_hit_on_soft:
                break
            d_bust_value = self.dealer.hit()
            self.dealer.show_cards()
            if d_bust_value == 0:
                print("Dealer Busted!")
                for current_player in self.current_player_list:

                    if current_player == None:
                        continue

                    current_player.update_bankroll_value(1)
                return self.deck.count_card.true_count

        for current_player in self.current_player_list:

            if current_player == None:
                continue

            if self.dealer.score == current_player.score:
                print("Push for Player", current_player.player_index)
                print("Bankroll_value", current_player.bankroll)
            elif self.dealer.score > current_player.score:
                print("Dealer Won!")
                current_player.update_bankroll_value(-1)
            elif self.dealer.score < current_player.score:
                print(f"Player {current_player.player_index} Won!")
                current_player.update_bankroll_value(1)

        # Experiment
        return self.deck.count_card.true_count

    def ask_for_insurance(self):
        if self.basic_strategy == False:
            for i in range(len(self.player_list)):
                current_player = self.player_list[i]
                print(
                    "Strategy: ",
                    BasicStrategy_with_PlayerDeviation().take_insurance(
                        self.deck.count_card.true_count
                    ),
                )

                print(
                    f"Enter for Player {current_player.player_index}\nWhether you wanna take the insurance: "
                )

                # choice = input()

                choice = BasicStrategy_with_PlayerDeviation().take_insurance(
                    self.deck.count_card.true_count
                )

                if choice == "I":
                    print(f"Player {current_player.player_index} took Insurance!")
                    current_player.has_insurance = True


if __name__ == "__main__":
    b = BlackJack(
        25, 6, 1.5, False, [1000, 1000, 1000], num_of_players=3, basic_strategy=False
    )
    b.play_n_rounds(100)
