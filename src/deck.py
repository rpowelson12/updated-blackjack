from cards import Card
import random

class Deck():

    def __init__(self):
        self.deck = []

    def create_deck(self):
        ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

        

        for i in range(len(suits)):
            for j in range(len(ranks)):
                card = Card(ranks[j], suits[i])
                self.deck.append(card)

        random.shuffle(self.deck)
        
        return self.deck
    
    def __repr__(self):
        return repr(self.deck)