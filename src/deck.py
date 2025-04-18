from cards import Card

class Deck():

    def create_deck():
        ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

        deck = []

        for i in range(len(suits)):
            for j in range(len(ranks)):
                card = Card(ranks[j], suits[i])
                deck.append(card)
        
        return deck

    def shuffle(self):
        # shuffles cards
        pass

    def deal(self):
        # deals cards
        pass

    def get_deck(self):
        return Deck.deck
