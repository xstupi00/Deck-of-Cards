"""deck_of_cards.py module"""

import random

# supported suits
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
# ranks of the special cards
cards_rank = {
    1: "Ace",
    11: "Jack",
    12: "Queen",
    13: "King",
    14: "Joker"
}
cards_number = 52
suit_cards = 13


class EmptyDeck(Exception):
    """EmptyDeck Exception class"""

    def __init__(self):
        self.message = "No more cards are left in the Deck."


class Card:
    """Card class."""

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Card):
            return NotImplemented
        return self._suit == other._suit and self._value == other._value

    @property
    def suit(self):
        """Gets the suit of this Card."""
        return self._suit

    @suit.setter
    def suit(self, suit):
        """Sets the suit of this Card.

        :param suit: The suit of this Card.
        :type suit: str
        """
        self._suit = suit

    @property
    def value(self):
        """Gets the value of this Card."""
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Card.

        :param value: The value of this Card.
        :type value: int
        """
        self._value = value

    def suit_as_string(self):
        """Returns a String representation of the card's suit. ("Spades", "Clubs")."""
        return self._suit

    def value_as_string(self):
        """Returns a String representation of the card's value (e.g. "Ace", "2")."""
        return cards_rank.get(self._value, str(self._value))

    def to_string(self):
        """
            Returns a string representation of this card, including both its suit and its value.
            (e.g. "Queen of Hearts", "10 of Diamonds").
        """
        return self.value_as_string() + " of " + self.suit_as_string()


class Deck:
    """Deck class."""

    def __init__(self):
        self.cards = [Card(suit, value) for suit in suits for value in range(1, suit_cards + 1)]

    def shuffle(self):
        """Put all the used cards back into the deck, and shuffle it into a random order."""
        random.shuffle(self.cards)

    def remaining(self):
        """Returns the number of cards remaining in the deck."""
        return len(self.cards)

    def deal(self):
        """
            Deals one card from the deck and returns it.
            If no more cards are left, an exception is thrown.
        """
        if len(self.cards):
            card = random.choice(self.cards)
            self.cards.remove(card)
            return card
        else:
            raise EmptyDeck()


class Hand:
    """Hand class."""

    def __init__(self):
        # A set of cards, which have been dealt from a Deck.
        self.hand = []

    def __repr__(self):
        return str(self.hand)

    def __eq__(self, other):
        if not isinstance(other, Hand):
            return NotImplemented
        return self.hand == other.hand

    def add_card(self, card):
        """Add a Card to the hand."""
        self.hand.append(card)

    def remove_card(self, card):
        """Removes a Card from the hand."""
        self.hand.remove(card)

    def sort_by_suit(self):
        """
            Sorts the cards in the hand so that cards of the same suit are grouped
            together, and within a suit the cards are sorted by rank.
        """
        self.hand.sort(key=lambda k: (k.suit, k.value))

    def sort_by_value(self):
        """
            Sorts the cards in the hand so that cards are sorted into order
            of increasing rank. Cards with the same rank are sorted by suit.
        """
        self.hand.sort(key=lambda k: (k.value, k.suit))
