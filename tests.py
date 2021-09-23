import unittest
import deck_of_cards as doc


class TestCard(unittest.TestCase):
    def test_card_init(self):
        card1 = doc.Card("Hearts", 3)
        card2 = doc.Card("Hearts", 3)
        self.assertEqual(card1, card2)

    def test_suit_and_value(self):
        card = doc.Card("Hearts", 3)
        self.assertEqual("Hearts", card.suit)
        self.assertEqual(3, card.value)

    def test_suit_as_string(self):
        deck = doc.Deck()
        card_clubs = deck.cards[0]
        card_diamonds = deck.cards[13]
        card_hearts = deck.cards[26]
        card_spades = deck.cards[39]
        self.assertEqual("Clubs", doc.Card.suit_as_string(card_clubs))
        self.assertEqual("Diamonds", doc.Card.suit_as_string(card_diamonds))
        self.assertEqual("Hearts", doc.Card.suit_as_string(card_hearts))
        self.assertEqual("Spades", doc.Card.suit_as_string(card_spades))

    def test_value_as_string(self):
        deck = doc.Deck()
        card_ace = deck.cards[0]
        card_jack = deck.cards[10]
        card_queen = deck.cards[11]
        card_king = deck.cards[12]
        card_number = deck.cards[1]
        self.assertEqual("Ace", doc.Card.value_as_string(card_ace))
        self.assertEqual("Jack", doc.Card.value_as_string(card_jack))
        self.assertEqual("Queen", doc.Card.value_as_string(card_queen))
        self.assertEqual("King", doc.Card.value_as_string(card_king))
        self.assertEqual("2", doc.Card.value_as_string(card_number))

    def test_to_string(self):
        deck = doc.Deck()
        card_ace_clubs = deck.cards[0]
        card_jack_diamonds = deck.cards[23]
        card_ten_hearts = deck.cards[35]
        card_three_spades = deck.cards[41]
        self.assertEqual("Ace of Clubs", doc.Card.to_string(card_ace_clubs))
        self.assertEqual("Jack of Diamonds", doc.Card.to_string(card_jack_diamonds))
        self.assertEqual("10 of Hearts", doc.Card.to_string(card_ten_hearts))
        self.assertEqual("3 of Spades", doc.Card.to_string(card_three_spades))


class TestDeck(unittest.TestCase):
    def test_deck_init(self):
        deck = doc.Deck()
        self.assertEqual(doc.cards_number, len(deck.cards))

    def test_shuffle(self):
        deck_before = doc.Deck()
        deck_after = deck_before.shuffle()
        self.assertNotEqual(deck_after, deck_before)

    def test_card_deal(self):
        deck = doc.Deck()
        origin_cards_number = len(deck.cards)
        dealt_card = deck.deal()
        self.assertEqual(origin_cards_number, len(deck.cards) + 1)

    def test_remaining(self):
        deck = doc.Deck()
        self.assertEqual(doc.cards_number, doc.Deck.remaining(deck))
        deck.deal()
        self.assertEqual(doc.cards_number - 1, doc.Deck.remaining(deck))


class TestHand(unittest.TestCase):
    def test_hand_init(self):
        hand = []
        init_hand = doc.Hand()
        self.assertCountEqual(hand, init_hand.hand)

    def test_add_cart(self):
        hand = [doc.Card("Clubs", 3), doc.Card("Hearts", 1)]
        init_hand = doc.Hand()
        init_hand.add_card(doc.Card("Clubs", 3))
        init_hand.add_card(doc.Card("Hearts", 1))
        self.assertCountEqual(hand, init_hand.hand)

    def test_remove_card(self):
        hand = [doc.Card("Clubs", 3)]
        init_hand = doc.Hand()
        init_hand.add_card(doc.Card("Clubs", 3))
        init_hand.add_card(doc.Card("Hearts", 1))
        init_hand.remove_card(doc.Card("Hearts", 1))
        self.assertCountEqual(hand, init_hand.hand)

    def test_sort_by_suit(self):
        sort_hand = [doc.Card("Clubs", 3), doc.Card("Diamonds", 11), doc.Card("Hearts", 1), doc.Card("Spades", 6)]
        init_hand = doc.Hand()
        init_hand.add_card(doc.Card("Spades", 6))
        init_hand.add_card(doc.Card("Clubs", 3))
        init_hand.add_card(doc.Card("Hearts", 1))
        init_hand.add_card(doc.Card("Diamonds", 11))
        init_hand.sort_by_suit()
        [self.assertEqual(sort_hand[idx].to_string(), card.to_string()) for idx, card in enumerate(init_hand.hand)]

    def test_sort_by_value(self):
        sort_hand = [doc.Card("Clubs", 2), doc.Card("Spades", 2), doc.Card("Diamonds", 11), doc.Card("Hearts", 11)]
        init_hand = doc.Hand()
        init_hand.add_card(doc.Card("Hearts", 11))
        init_hand.add_card(doc.Card("Clubs", 2))
        init_hand.add_card(doc.Card("Diamonds", 11))
        init_hand.add_card(doc.Card("Spades", 2))
        init_hand.sort_by_value()
        [self.assertEqual(sort_hand[idx].to_string(), card.to_string()) for idx, card in enumerate(init_hand.hand)]


if __name__ == '__main__':
    unittest.main()
