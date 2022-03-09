from Card import Card
from CountCard import CountCard
from Deck import Deck


def test_card():
    card = Card(1, 0)
    assert card.value == "A"
    assert card.suit == 0
    assert card.price == 11
    assert card.count == -1

    card = Card(5, 4)
    assert card.value == 5
    assert card.suit == 4
    assert card.price == 5
    assert card.count == 1

    assert card.cal_card_price("J") == 10
    assert card.cal_card_count(8) == 0


def test_count_card():
    countcard = CountCard()
    assert countcard.running_count == 0
    assert countcard.true_count == 0

    countcard = CountCard(3.14, -7)
    assert countcard.running_count == 3.14
    assert countcard.true_count == -7

    countcard.update_true_count(2.3)
    assert countcard.true_count == 3.14 / 2.3  # running_count / num_of_remianing_deck

    countcard.reset()
    assert countcard.running_count == 0
    assert countcard.true_count == 0


def test_deck():
    deck = Deck()
    assert deck.num_of_deck == 4
    assert len(deck.cards) == 208  # (4 * 13) * 4
    assert deck.num_of_deck_remaining() == 4

    drawn_cards = deck.draw_card(2)
    assert len(drawn_cards) == 2
    assert isinstance(drawn_cards[0], Card)

    drawn_cards = deck.draw_card(5)
    assert len(drawn_cards) == 5
    assert isinstance(drawn_cards[3], Card)

    assert (
        deck.num_of_deck_remaining() == (208 - 7) / 52
    )  # total_cards - drawn_cards / num_of_cards_in_deck

    deck.generate_cards()
    assert len(deck.cards) == 208 + 201  # new set of cards + remianing set of cards

    deck = Deck(8)
    assert deck.num_of_deck == 8
    assert len(deck.cards) == 416
    assert deck.num_of_deck_remaining() == 8


def test_player():
    pass


def test_basic_startegy():
    pass


def test_blackjack():
    pass
