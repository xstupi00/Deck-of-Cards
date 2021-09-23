# Deck of Cards

Assignment:

Please complete the following programming exercise in the language of your choice. The program must compile (as applicable), but you do not need to provide tools/scripts to compile it. In addition to completing the exercise, please also include a test suite.

The exercise should take between 60 and 90 minutes, but it's not an explicit requirement. In other words, completeness trumps time spent.

Implement a Deck of Cards, which can be used to fill Hands of Cards

      - Card

            - Has two attributes, the value and rank

            - There are 4 supported suits - spades, hearts, diamonds, clubs.

            - Each of the following suits (spade, heart, diamond, and club) has one of 13 possible ranks: ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, or king. Ranks are not duplicated within a suit. Ace is the lowest rank with king being highest rank.

            - The 'special' suit Joker does not need to be supported, but there may be a future requirement to include it. Please consider this in your design.

            - Supports the following contract

                  - [S] suit() : returns the suit of this card, with [S] being the type you used in defining suit. For example, it could be an integer or an instance of a class of your own creation.

                  - int value() : returns the value, which is one of the numbers 1 through 13, inclusive for a regular card.

                  - String suitAsString() : Returns a String representation of the card's suit. ("Spades", "Clubs")

                  - String valueAsString() : Returns a String representation of the card's value (e.g. "Ace", "2")

                  - String toString() : Returns a string representation of this card, including both its suit and its value. (e.g. "Queen of Hearts", "10 of Diamonds")

      - Deck

            - Composed of 52 cards, no duplicates

            - Once a card has been dealt from a deck, it cannot be dealt again until the deck has been shuffled.

            - Supports the following contract

                  - shuffle() : Put all the used cards back into the deck, and shuffle it into a random order.

                  - remaining() : As cards are dealt from the deck, the number of cards remaining decreases. This function returns the number of cards remaining in the deck.           

                  - Card deal() :  Deals one card from the deck and returns it. If no more cards are left, an exception is thrown.

      - Hand

            - A set of cards, which have been dealt from a Deck.

            - The number of cards in a hand is only restricted by the number of cards contained in a Deck (e.g. 0 to 52)

            - Supports the following contract

                  - addCard(Card) : add a Card to the hand

                  - removeCard(Card) : removes a Card from the hand

                  - sortBySuit() : Sorts the cards in the hand so that cards of the same suit are grouped together, and within a suit the cards are sorted by rank.

                  - sortByValue() : Sorts the cards in the hand so that cards are sorted into order of increasing rank. Cards with the same rank are sorted by suit.

            - Design assumptions

                  - Aces are considered to have the lowest rank.

                  - Order of suits are alphabetical based, e.g. lowest is clubs and highest is spades.